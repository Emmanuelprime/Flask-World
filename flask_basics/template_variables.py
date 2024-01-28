from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def index():
    some_var = 'prime'
    letters = list(some_var)
    return render_template("template_var.html",some_var = some_var,letters=letters)



if __name__ == '__main__':
    app.run(debug=True)