from flask import Flask, jsonify
from scraper import scrape
from dotenv import load_dotenv
import os

load_dotenv(verbose=True)
DB_CONFIG = {
        "DB_URI": os.getenv("DB_URI"),
        "DB_USERNAME": os.getenv("DB_USERNAME"),
        "DB_PASSWORD": os.getenv("DB_PASSWORD")
}

app = Flask(__name__)

@app.route('/')
def root():
    return jsonify({
        "success": True,
        "message": "running"
    })

@app.route('/all-listings')
def getAllListings():
    return jsonify({
        "success": True,
        "data": scrape()
    })

if __name__ == '__main__':
    app.run()
