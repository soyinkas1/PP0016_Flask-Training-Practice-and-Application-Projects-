from flask import Flask


app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Hello World!</h1>'

# app.add_url_rule('/', 'index', index)

if __name__ == "__main__":
    app.run()