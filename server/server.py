from flask import Flask, jsonify, send_from_directory
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
from scraper import scrape
import os
import connexion


# LOADING IN ENVIRONMENT VARIABLES
load_dotenv(verbose=True)
DB_CONFIG = {
        "MYSQL_HOST": os.getenv("DB_URI"),
        "MYSQL_USER": os.getenv("DB_USERNAME"),
        "MYSQL_PASSWORD": os.getenv("DB_PASSWORD"),
        "MYSQL_DB": os.getenv("DB_NAME")
}

ENV = os.getenv('PY_ENV')


# BOOTSTRAPPING APP WITH ENVIRONMENT VARIABLES
def create_app(config=None):
    app = Flask(__name__)
    if config:
        if ENV == 'PRODUCTION':
            if isinstance(config, dict):
                app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://%s:%s@%s/%s" % (
                    config["MYSQL_USER"],
                    config["MYSQL_PASSWORD"],
                    config["MYSQL_HOST"],
                    config["MYSQL_DB"]  
                )
        else:
            app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db = SQLAlchemy(app)
    return app, db



# GETTING INSTANCES OF API AND DB
app, db = create_app(DB_CONFIG)



#MODELS
class Listing(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    price = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return 'Listing(title=%s,price=%s)' % (self.title, self.price)


# CONTROLLERS


# ROOT ROUTE
@app.route('/')
def home():
    return jsonify({
        'success': True,
        'message': 'running'
    })

# ROUTE TO VERIFY DB CONNECTION
@app.route('/db-result', methods=['GET','POST'])
def dbresult():
    return jsonify({
        'success': True,
        'data': list(map(lambda x: {
            "title": x.title,
            "price": x.price
        }, Listing.query.all()))
    })

      
def seed():
    test_data = scrape()
    for x in test_data:
        db.session.add(Listing(title=x["title"], price=x["price"]))
    db.session.commit()


if __name__ == '__main__':
    db.create_all()
    if ENV != 'PRODUCTION':
        seed()
    app.run(debug=True)
