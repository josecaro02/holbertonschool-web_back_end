#!/usr/bin/env python3
""" auth file for user authentication service """

import bcrypt
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound
import uuid
from typing import Union


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

    def get_user_from_session_id(self, session_id: str) -> Union[str, None]:
        """It takes a single session_id string argument and
        returns the corresponding User or None."""
        if session_id is None:
            return None

        try:
            user = self._db.find_user_by(session_id=session_id)
        except NoResultFound:
            return None

        return user

    def destroy_session(self, user_id: int) -> None:
        """Updates the corresponding user's session ID to None"""
        try:
            user = self._db.find_user_by(id=user_id)
        except NoResultFound:
            return None

        self._db.update_user(user.id, session_id=None)

        return None

    def get_reset_password_token(self, email: str
                                 ) -> str:
        """Generates a reset password token if user exists"""
        try:
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            raise ValueError

        reset_token = _generate_uuid()

        self._db.update_user(user.id, reset_token=reset_token)

        return reset_token

    def update_password(self, reset_token: str,
                        password: str) -> None:
        """Uses reset token to validate update of users password"""
        if reset_token is None or password is None:
            return None

        try:
            user = self._db.find_user_by(reset_token=reset_token)
        except NoResultFound:
            raise ValueError

        hashed_password = _hash_password(password)
        self._db.update_user(user.id,
                             hashed_password=hashed_password,
                             reset_token=None)
