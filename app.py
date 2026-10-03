import os 
import sqlite3

from flask import Flask, request, render_template

app = Flask(__name__)

con = sqlite3.connect("app.db")
cur = con.cursor()

SCHEMA = """
CREATE TABLE IF NOT EXISTS messages (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL, 
    mail TEXT NOT NULL,
    message TEXT NOT NULL,
    send_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP  
)
"""

cur.execute(SCHEMA)
con.commit()

# Routes 

@app.route("/")
def index():
    return render_template("index.html")