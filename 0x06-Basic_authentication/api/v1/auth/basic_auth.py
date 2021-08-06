#!/usr/bin/env python3
""" basic authentication for auth"""
from api.v1.auth.auth import Auth
from base64 import b64decode


class BasicAuth(Auth):
    """ Basic authentication class"""

    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """ Extract base64 authorization header"""
        if authorization_header is None:
            return None

        if not isinstance(authorization_header, str):
            return None

        if not authorization_header.startswith('Basic '):
            return None

        return authorization_header[6:]

    def decode_base64_authorization_header(self,
                                           base64_authorization_header: str
                                           ) -> str:
        """ decode authorization header"""

        if base64_authorization_header is None:
            return None

        if not isinstance(base64_authorization_header, str):
            return None

        try:
            encoded = base64_authorization_header.encode('utf-8')
            decoded64 = b64decode(encoded)
            return decoded64.decode('utf-8')
        except BaseException:
            return None
