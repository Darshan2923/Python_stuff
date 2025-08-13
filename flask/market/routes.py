from market import app
from flask import render_template
from market.models import Item

@app.route("/")
@app.route("/home")
def home_page():
    return render_template('home.html')


@app.route('/market')
def market_page():
    # items = [
    #     {'id': 1, 'name': 'Phone', 'barcode': '893212299897', 'price': 500},
    #     {'id': 2, 'name': 'Laptop', 'barcode': '123985473165', 'price': 900},
    #     {'id': 3, 'name': 'Keyboard', 'barcode': '231985128446', 'price': 150}
    # ]
    items=Item.query.all()
    return render_template('market.html', items=items)

@app.route("/about/<username>")
def about_page(username):
    return f'<h1>About page for {username}</h1>'