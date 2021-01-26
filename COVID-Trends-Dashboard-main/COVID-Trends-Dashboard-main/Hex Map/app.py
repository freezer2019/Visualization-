# import necessary libraries
from models import create_classes
import os
from flask import (
    Flask,
    render_template,
    jsonify,
    request,
    redirect)

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

#################################################
# Database Setup
#################################################

from flask_sqlalchemy import SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', '') or "postgresql://postgres:postgres@localhost/mobility2_db"

# Remove tracking modifications
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

Mobility = create_classes(db)

# create route that renders index.html template
@app.route("/")
def home():
    
    return render_template("index.html")

@app.route("/api/data")
def data():

    # df=pd.read_sql
    receiveddata = db.session.query(Mobility.states, Mobility.dates, Mobility.sma_retail_recreation, Mobility.sma_grocery_pharmacy, Mobility.sma_parks, Mobility.sma_transit, Mobility.sma_workplaces, Mobility.sma_residential, Mobility.case_count, Mobility.new_case_count, Mobility.revenue_all, Mobility.revenue_ss60, Mobility.deaths).all()

    return jsonify(receiveddata)


# Creating routes for the rest of the pages
@app.route("/comparison")
def comparison():
    return render_template("comparison.html")  

@app.route("/tweets")
def tweets():
    return render_template("tweets.html") 

@app.route("/google")
def google():
    return render_template("google.html") 

@app.route("/pets")
def pets():
    return render_template("pets.html") 

if __name__ == "__main__":
    app.run()

