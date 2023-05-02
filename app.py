# import flask instance from flask package 
from flask import Flask,render_template

# initialize the instace of the flask with given argument __name__
app = Flask(__name__)

# decorator - one step before the function is executed 
@app.route("/")
@app.route("/home")
def home_page():
    return render_template('home.html')

@app.route("/market")
def market_page():
    items = [
        {'id':1,'name':'Phone','barcode': '87875443332','price':500},
         {'id':1,'name':'Laptop','barcode': '87873856765','price':1100},
          {'id':1,'name':'Keyboard','barcode': '87878213456','price':1800},
    ]
    return render_template('market.html', items = items)
