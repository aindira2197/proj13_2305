from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///foods.db'

db = SQLAlchemy(app)


class Food(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))


@app.route('/')
def home():

    foods = Food.query.all()

    text = ""

    for food in foods:
        text += f"{food.name}<br>"

    return text


@app.route('/add/<name>')
def add(name):

    food = Food(name=name)

    db.session.add(food)
    db.session.commit()

    return "Food Added"


if __name__ == '__main__':

    with app.app_context():
        db.create_all()

    app.run(debug=True)
