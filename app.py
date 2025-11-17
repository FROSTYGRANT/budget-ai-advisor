from flask import Flask, render_template, request, redirect, url_for, flash
import mysql.connector
from mysql.connector import Error
from datetime import date
import openai
from config import MYSQL_HOST, MYSQL_USER, MYSQL_PASSWORD, MYSQL_DB, OPENAI_API_KEY

app = Flask(__name__)
app.secret_key = "dev_secret_key_change_for_prod"

openai.api_key = OPENAI_API_KEY

def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="MYSQL_DB"
    )

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/add", methods=["POST"])
def add_expense():
    name = request.form.get("name", "").strip()
    amount = request.form.get("amount", "").strip()
    category = request.form.get("category", "").strip()
    if not name or not amount or not category:
        flash("Please fill all fields.", "error")
        return redirect(url_for("index"))

    try:
        amt = float(amount)
    except ValueError:
        flash("Amount must be a number.", "error")
        return redirect(url_for("index"))

    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute(
            "INSERT INTO expenses (name, amount, category, date) VALUES (%s, %s, %s, %s)",
            (name, amt, category, date.today())
        )
        conn.commit()
        flash("Expense added.", "success")
    except Error as e:
        flash(f"Database error: {e}", "error")
    finally:
        cursor.close()
        conn.close()

    return redirect(url_for("index"))

@app.route("/expenses")
def expenses():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    try:
        cursor.execute("SELECT * FROM expenses ORDER BY date DESC, id DESC")
        rows = cursor.fetchall()
        total = sum([float(r["amount"]) for r in rows]) if rows else 0.0
    except Error as e:
        flash(f"Database error: {e}", "error")
        rows = []
        total = 0.0
    finally:
        cursor.close()
        conn.close()
    return render_template("expenses.html", expenses=rows, total=total)

@app.route("/advice", methods=["GET", "POST"])
def advice():
    if request.method == "GET":
        return render_template("advice.html", advice_text=None)

    # POST: generate advice
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    try:
        cursor.execute("SELECT * FROM expenses ORDER BY date DESC LIMIT 100")
        rows = cursor.fetchall()
    except Error as e:
        flash(f"Database error: {e}", "error")
        rows = []
    finally:
        cursor.close()
        conn.close()

    if not OPENAI_API_KEY:
        flash("OpenAI API key not configured. Put it in the .env file.", "error")
        return render_template("advice.html", advice_text=None)

    # Build a compact summary of expenses
    if not rows:
        advice_text = "No expenses found. Add some expenses first to receive tailored advice."
        return render_template("advice.html", advice_text=advice_text)

    summary_lines = []
    total = 0.0
    for r in rows:
        summary_lines.append(f"{r['date']} - {r['name']} ({r['category']}): KES {r['amount']}")
        total += float(r['amount'])

    summary = "\n".join(summary_lines)
    prompt = (
        "You are a financially practical assistant. A user in Kenya has the following recent expenses (KES):\n\n"
        f"{summary}\n\n"
        f"Total spending shown: KES {total:.2f}\n\n"
        "Please produce:\n"
        "1) A short (5-8 bullet) list of practical, realistic saving suggestions tailored to this list (no medical/illegal advice),\n"
        "2) Identify the top 2 expense categories the user should consider reducing and why,\n"
        "3) Offer one low-effort immediate action the user can take today to save money.\n"
        "Keep answers concise and actionable. Use local context where helpful (e.g., transport, food, airtime)."
    )

    try:
        # Use chat completion (gpt-3.5-turbo) for reliability
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You give concise, practical personal finance advice."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=400,
            temperature=0.6
        )
        advice_text = response["choices"][0]["message"]["content"].strip()
    except Exception as e:
        advice_text = f"Error contacting AI service: {e}"

    return render_template("advice.html", advice_text=advice_text)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)