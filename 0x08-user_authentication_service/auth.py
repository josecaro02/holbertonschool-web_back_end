#!/usr/bin/env python3
""" auth file for user authentication service """

import bcrypt
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound
import uuid


def _hash_password(password: str) -> str:
    """takes in a password string arguments and returns bytes. """
    encoded = password.encode()
    hashed = bcrypt.hashpw(encoded, bcrypt.gensalt())

    return str(hashed)


def _generate_uuid() -> str:
    """Returns a string representation of a new UUID"""
    UUID = uuid.uuid4()
    return str(UUID)


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """take mandatory email and password string arguments
        and return a User object."""
        try:
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            hashed_password = _hash_password(password)
            user = self._db.add_user(email, hashed_password)

            return user

        else:
            raise ValueError(f'User {email} already exists')

    def valid_login(self, email: str, password: str) -> bool:
        """expect email and password required arguments, return true"""
        if password is None or type(password) is not str:
            return False

        try:
            found_user = self._db.find_user_by(email=email)
        except NoResultFound:
            return False
        else:
            return bcrypt.checkpw(password.encode(),
                                  found_user.hashed_password)

    def create_session(self, email: str) -> str:
        """It takes an email string argument and returns
        the session ID as a string."""
        try:
            found_user = self._db.find_user_by(email=email)
        except NoResultFound:
            return None
        else:
            new_uuid = _generate_uuid()
            self._db.update_user(found_user.id, session_id=new_uuid)
            return new_uuid
