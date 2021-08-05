#!/usr/bin/env python3
""" Auth file"""
from flask import request
from typing import List, TypeVar


class Auth:
    """ class auth from authentication file"""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ Require auth public method"""

        if path is None or excluded_paths is None or excluded_paths == []:
            return True

        lenPath = len(path)
        if lenPath == 0:
            return True

        slash_path = True if path[lenPath - 1] == '/' else False

        tmp_path = path
        if not slash_path:
            tmp_path += '/'

        for exc in excluded_paths:
            l_exc = len(exc)
            if l_exc == 0:
                continue

            if exc[l_exc - 1] != '*':
                if tmp_path == exc:
                    return False
            else:
                if exc[:-1] == path[:l_exc - 1]:
                    return False

        return True

    def authorization_header(self, request=None) -> str:
        """ authorized header public method"""
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        return None
