#!/usr/bin/env python3
""" basic session for auth"""
from api.v1.auth.auth import Auth
import uuid
from models.user import User


class SessionAuth(Auth):
    """ Session Auth Class"""
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """ creates a session ID for a user_id"""
        if user_id is None:
            return None
        if not isinstance(user_id, str):
            return None
        session_id = str(uuid.uuid4())
        self.user_id_by_session_id[session_id] = user_id

        return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """ return a user id based on a session id"""
        if session_id is None:
            return None
        if not isinstance(session_id, str):
            return None

        return self.user_id_by_session_id.get(session_id)

    def current_user(self, request=None):
        """ overload that returns user insacens based on cookie"""
        session_id = self.session_cookie(request)
        if session_id is None:
            return None

        user_id = self.user_id_for_session_id(session_id)

        return User.get(user_id)

    def destroy_session(self, request=None):
        """ deletes the user sesion logout"""
        if request is None:
            return False

        session_id = self.session_cookie(request)
        if session_id is None:
            return False

        user_id = self.user_id_for_session_id(session_id)

        if not user_id:
            return False

        try:
            del self.user_id_by_session_id[session_id]
        except Exception:
            pass

        return True
