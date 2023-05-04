from market import app
from flask import render_template
from market.models import Item
# from market import db
# with app.app_context():
#     db.create_all()
# decorator - one step before the function is executed 
@app.route("/")
@app.route("/home")



def home_page():
    return render_template('home.html')

@app.route("/market")
def market_page():
    items = Item.query.all()
    return render_template('market.html', items = items)
