#!/usr/bin/env python3
""" basic flask app"""
from flask import Flask, jsonify, request, abort
from auth import Auth


app = Flask(__name__)
AUTH = Auth()


@app.route('/', methods=['GET'], strict_slashes=False)
def welcome() -> str:
    """First route bienvenue"""
    return jsonify({"message": "Bienvenue"})


@app.route('/users', methods=['POST'])
def register_user() -> str:
    """ end-point to register a user"""
    try:
        email = request.form['email']
        password = request.form['password']
    except KeyError:
        abort(400)

    try:
        user = AUTH.register_user(email, password)
    except ValueError:
        return jsonify({"message": "email already registered"}), 400

    msg = {"email": email, "message": "user created"}
    return jsonify(msg)


@app.route('/sessions', methods=['POST'])
def login():
    """Login users"""
    req_par = request.form
    email = req_par.get('email')
    password = req_par.get('password')
    if AUTH.valid_login(email, password):
        session_id = AUTH.create_session(email)
        if not session_id:
            abort(401)
        msg = {"email": email, "message": "logged in"}
        output = jsonify(msg)
        output.set_cookie("session_id", session_id)
        return output
    else:
        abort(401)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
