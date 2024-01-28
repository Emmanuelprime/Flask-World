from flask import Flask

app = Flask(__name__)

@app.route('/people/<name>') # adding dynamic route
def index(name):
    return "User: {}".format(name[100])

if __name__ == '__main__':
    app.run(debug=True)