from flask import Flask, render_template, request, redirect
import sqlite3
from datetime import date

app = Flask(__name__)

def get_db():
    return sqlite3.connect("expenses.db")

@app.route("/")
def home():
    conn = get_db()
    cur = conn.cursor()
    today = str(date.today())

    # Sab expenses fetch karo
    cur.execute("SELECT * FROM expenses ORDER BY date DESC")
    expenses = cur.fetchall()

    # Aaj ka total
    cur.execute("SELECT SUM(amount) FROM expenses WHERE date=?", (today,))
    total = cur.fetchone()[0] or 0

    conn.close()
    return render_template("index.html", expenses=expenses, total=total)


@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        amount = request.form["amount"]
        category = request.form["category"]
        note = request.form["note"]
        today = str(date.today())

        conn = get_db()
        conn.execute(
            "INSERT INTO expenses (amount, category, note, date) VALUES (?,?,?,?)",
            (amount, category, note, today)
        )
        conn.commit()
        conn.close()

        return redirect("/")

    return render_template("add.html")
def get_db():
    conn = sqlite3.connect("expenses.db")
    conn.row_factory = sqlite3.Row   # <-- add this line
    return conn

app.run(debug=True, host="0.0.0.0", port=5000)
