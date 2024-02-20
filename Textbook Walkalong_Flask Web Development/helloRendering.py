from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_moment import Moment


app = Flask(__name__)

Bootstrap = Bootstrap(app)
moment = Moment(app)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def page_not_found(e):
    return render_template('500.html'), 404

@app.route('/user1/<name>')
def user1(name):
    return render_template('user1.html', name=name)

if __name__ == '__main__':
    app.run()