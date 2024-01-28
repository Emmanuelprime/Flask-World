from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "<h1> hello Puppy!</h1>"

@app.route("/on")
def new():
    return "This is the second page"

if __name__ == '__main__':
    app.run(debug=True)