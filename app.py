import os 
import sqlite3

from flask import Flask, request, render_template, redirect

app = Flask(__name__)

con = sqlite3.connect("app.db", check_same_thread=False)
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

@app.route("/skills")
def skills():
    return render_template("skills.html")

@app.route("/projects")
def projects():
    return render_template("projects.html")

@app.route("/contact", methods=["GET", "POST"])
def contact():

    if request.method == "GET":
        return render_template("contact.html")

    name = request.form.get("name")
    email = request.form.get("email")
    message = request.form.get("message")

    cur.execute(
        "INSERT INTO messages (name, mail, message) VALUES (?, ?, ?)",
        (name, email, message),
    )
    con.commit()

    return redirect("/")