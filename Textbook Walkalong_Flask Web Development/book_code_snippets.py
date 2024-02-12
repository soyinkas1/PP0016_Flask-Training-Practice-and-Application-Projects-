
from flask import Flask

app = Flask(__name__)

# The following example creates a response object and then sets a cookie in it"
from flask import make_response

@app.route("/")
def index():
    response = make_response('<h1>This document carries a cookie!,</h1>')
    response.set_cookie('answer', '42')
    return response

# The following function returns a 400 status cose, the code for a bad request error
@app.route('/')
def index():
    return '<h1>Bad Request</h1>', 400

# Flask provide a redirect() helper function that creates the redirect response
from flask import redirect

@app.route
def index():
    return redirect('http://www.example.com')

# A special response is issued by abort() function. This example returns status code 404 if the id dynamic argument given in the URL does not represent a valid user
from flask import abort

@app.route('/user/<id>')
def get_user(id):
    user = load_user(id)
    if not user:
        abort(404)
    return '<h1>Hello, {}</h1>'.format(user.name)





