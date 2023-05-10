from flask import Flask, request
from flask import render_template
app = Flask(__name__)

@app.route("/index")
@app.route("/")
def hello_world():
    return "<p>Hello, World!!</p>"

#http://127.0.0.1:5000/new/?greeting=ola
#http://127.0.0.1:5000/new/ -  default value = hello 
@app.route("/new/")
def query_strings(greeting = 'hello'):
    # get is a dictionary methdod
    # if the user dosent send any value the n 'hello' will be default value
    query_val = request.args.get('greeting',greeting)
    # print(query_val)
    return f"<h1>The greeting is: {query_val} </h1>"

#http://127.0.0.1:5000/user/Arsh
#http://127.0.0.1:5000/user - default value: Anupam
@app.route("/user")
@app.route("/user/<name>")
def no_query_strings(name = 'Anupam'):
    # query_val = request.args.get('greeting',greeting)
    return f"<h1>Hello there !: {name} </h1>"

# strings 
#http://127.0.0.1:5000/number/arsh
@app.route('/text/<string:name>')
def working_with_string(name):
    return f"<h1>Hello there !: {name} </h1>"

# numbers 
#http://127.0.0.1:5000/number/1
@app.route('/number/<int:num>')
def working_with_numbers(num):
    print(type(num))
    return f"<h1>Hello there !: {num} </h1>"

# numbers 
#http://127.0.0.1:5000/add/78/25
@app.route('/add/<int:num1>/<int:num2>')
def adding_integers(num1,num2):
    return f"<h1>Hello there !: { num1 + num2} </h1>"

# floats 
#http://127.0.0.1:5000/product/78.1/22.1
@app.route('/product/<float:num1>/<float:num2>')
def multiply_float(num1,num2):
    return f"<h1>Hello there !: { num1 * num2} </h1>"

# Using Template 
@app.route('/temp')
def using_template():
    print('a')
    return render_template('hello.html')

# jinja Template
@app.route('/watch')
def top_movies():
    movie_list = ['autopsy of jane doe','neon demon','ghost in a shell',
                  'skull island','jon wick-2','spiderman-homecoming']
    return render_template('movies.html',movies= movie_list,name='Harry')

# jinja-2 Template
@app.route('/tables')
def movies_plus():
    movie_dict = {'autopsy of jane doe':2.14,
                  'neon demon':3.20,
                  'ghost in a shell':9.01,
                  'skull island':6.78,
                  'jon wick-2':1.21,
                  'spiderman-homecoming':4.56}
    return render_template('table_data.html',movies= movie_dict,name='Sally')



if __name__ == '__main__':
    app.run(debug=True)