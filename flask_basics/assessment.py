from flask import Flask,request

app = Flask(__name__)

@app.route('/')
def index():
    
    return '<h1>The Puppy Website</h1'

@app.route('/puppy_latin/<name>')
def puppy_latin(name):
    name_list = list(name.lower())
    if name_list[-1] == 'y':
        name_list.pop()
        name_list = name_list + list('iful')
        #name_list = name_list.append('iful')
        name_list = ''.join(name_list)
        return f"<h1> the puppy name in latin is {name_list}"
    elif name_list[-1] != 'y':
        name_list.append('y')
        name_list = ''.join(name_list)
        return f"<h1> the puppy name in latin is {name_list}"


if __name__ == '__main__':
    app.run(debug=True)