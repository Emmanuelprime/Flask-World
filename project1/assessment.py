from flask import Flask,render_template,request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/report")
def report():
    msg =''
    username = request.args.get('username')
    has_upper = any(char.isupper() for  char in username)
    has_lower = any(char.islower() for char in username)
    ends_with = username[-1].isdigit()
    
    if has_upper and has_lower and ends_with:
        msg = "passed the name check"
    elif has_upper and has_lower and not ends_with:
        msg="must end with a number"
    elif has_upper and not has_lower and ends_with:
        msg = "must contain a lower case letter"
    
    elif not has_upper and has_lower:
        msg="must contain upper case"
            
        
        
    return render_template("report.html",msg=msg, username=username)

# @app.errorhandler(404)
# def page_not_found(e):
#     return render_template("404.html"),404


if __name__ == '__main__':
    app.run(debug=True)