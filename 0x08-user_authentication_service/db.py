#!/usr/bin/env python3
"""DB module for project user authentication
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.exc import InvalidRequestError

from user import Base, User


class DB:
    """DB class for project user authentication
    """

    def __init__(self) -> None:
        """Initialize a new DB instance
        """
        self._engine = create_engine("sqlite:///a.db", echo=False)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -> Session:
        """Memoized session object
        """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """ method, which has two required string arguments:
         email and hashed_password, and returns a User object"""
        user = User(email=email, hashed_password=hashed_password)
        self._session.add(user)
        self._session.commit()

        return user

    def find_user_by(self, **kwargs) -> User:
        """find user by method return first row founded"""
        if not kwargs:
            raise InvalidRequestError

        column_names = User.__table__.columns.keys()
        for key in kwargs.keys():
            if key not in column_names:
                raise InvalidRequestError

        user = self._session.query(User).filter_by(**kwargs).first()

        if user is None:
            raise NoResultFound

        return user

    def update_user(self, user_id: int, **kwargs) -> None:
        """ takes as argument a required user_id integer and
        arbitrary keyword arguments, and returns None. """
        foundUser = self.find_user_by(id=user_id)

        if not kwargs:
            raise ValueError

        for key, value in kwargs.items():
            if hasattr(foundUser, key):
                setattr(foundUser, key, value)
            else:
                raise ValueError

        self._session.commit()
        return None
