from flask import Flask, request, jsonify, redirect, url_for
from requests_oauthlib import OAuth2Session
import json

app = Flask(__name__)

CLIENT_ID = 'your-client-id'
CLIENT_SECRET = 'your-client-secret'
REDIRECT_URI = 'http://localhost:5000/callback'

@app.route('/')
def home():
    return "Welcome to the Email Engine!"

@app.route('/login')
def login():
    outlook = OAuth2Session(CLIENT_ID, redirect_uri=REDIRECT_URI)
    authorization_url, state = outlook.authorization_url(
        'https://login.microsoftonline.com/common/oauth2/v2.0/authorize',
        access_type="offline", prompt="select_account")
    return redirect(authorization_url)

@app.route('/callback')
def callback():
    outlook = OAuth2Session(CLIENT_ID, redirect_uri=REDIRECT_URI)
    token = outlook.fetch_token(
        'https://login.microsoftonline.com/common/oauth2/v2.0/token',
        client_secret=CLIENT_SECRET,
        authorization_response=request.url)
    # Save token and user details securely
    return jsonify({'message': 'Logged in successfully', 'token': token})

if __name__ == '__main__':
    app.run(debug=True)
