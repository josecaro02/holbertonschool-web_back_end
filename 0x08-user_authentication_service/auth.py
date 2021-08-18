#!/usr/bin/env python3
""" auth file for user authentication service """

import bcrypt


def _hash_password(password: str) -> str:
    """takes in a password string arguments and returns bytes. """
    encoded = password.encode()
    hashed = bcrypt.hashpw(encoded, bcrypt.gensalt())

    return str(hashed)
