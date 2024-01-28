from flask import Flask,render_template,request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("home_form.html")

@app.route("/register")
def forms():
    return render_template("form.html")

@app.route("/thanks")
def thank_you():
    first = request.args.get("first")
    last = request.args.get("last")
    return render_template("thanks.html",first=first,last=last)

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"),404


if __name__ == '__main__':
    app.run(debug=True)