#########################################
# Flask API
########################################
# Importing the required libraries
import numpy as np
import sqlalchemy
import datetime as dt
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, jsonify
from flask import render_template

########################################
# Database Setup
########################################
engine = create_engine("sqlite:///Resources/hawaii.sqlite",echo=False)


# reflect an existing database. into a new model
Base = automap_base()
# reflect the tablets
Base.prepare(engine, reflect=True)
# Mapping measurement class
Measurement = Base.classes.measurement
# Mapping ststion class
Station = Base.classes.station


#######################################
# Querying date in the database
######################################
# Create our session (link) from Python to the DB
session = Session(bind=engine)
# Let's count the total dates we have
total_dates = session.query(func.count(Measurement.date)).first()
# Find the earliest date

   