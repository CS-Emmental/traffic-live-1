from flask import Flask
from flask import request
app = Flask(__name__)

@app.route('/')
def hello():
    cookies_session = request.cookies.get('session')
    if cookies_session == "imagine_this_to_be_a_complicated_token_for_the_admin_session":
        return "Welcome admin <br/> Congratulations, the token to validate this challenge is the following : BimBamBoum"
    if cookies_session == "imagine_this_to_be_a_complicated_token_for_a_user_session":
        return "Welcome user <br/> It seems you managed to connect as a user but you're don't have the administrator rights"
    return "Welcome Guest, you need to be connected to continue"
