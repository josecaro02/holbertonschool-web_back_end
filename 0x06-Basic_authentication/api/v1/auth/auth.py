#!/usr/bin/env python3
from flask import request
from typing import List, TypeVar
""" Auth file"""


class Auth():
    """ class auth from authentication file"""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ Require auth public method"""
        return False

    def authorization_header(self, request=None) -> str:
        """ authorized header public method"""
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        return None
