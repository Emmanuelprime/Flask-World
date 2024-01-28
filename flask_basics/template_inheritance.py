from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("home.html")

@app.route("/somepage")
def somepage():
    return render_template("some_page.html")



if __name__ == '__main__':
    app.run(debug=True)