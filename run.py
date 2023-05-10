from flask import Flask, request

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

if __name__ == '__main__':
    app.run(debug=True)