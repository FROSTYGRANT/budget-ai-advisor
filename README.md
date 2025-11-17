# Budget AI Advisor

[![Python](https://img.shields.io/badge/Python-3.10+-blue)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-2.1+-green)](https://flask.palletsprojects.com/)
[![OpenAI](https://img.shields.io/badge/OpenAI-API-orange)](https://openai.com/)

---

## Table of Contents

- [Project Overview](#project-overview)
- [SDG Alignment](#sdg-alignment)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Installation](#installation)
- [Database Setup](#database-setup)
- [Running the App](#running-the-app)
- [Screenshots](#screenshots)
- [Usage](#usage)
- [Notes](#notes)
- [License](#license)

---

## Project Overview

**Budget AI Advisor** is a simple web application that helps users track daily expenses and receive personalized savings advice powered by AI. The project uses a MySQL database to store expenses and connects to the OpenAI API to provide actionable, local-context financial tips.  

This beginner-friendly project demonstrates how AI can assist in practical personal finance management.

---

## SDG Alignment

This project contributes to the following **Sustainable Development Goals (SDGs)**:

- **SDG 1: No Poverty** – By helping users track spending and get saving advice, it empowers individuals to better manage finances and avoid unnecessary financial stress.
- **SDG 8: Decent Work & Economic Growth** – Encourages responsible financial habits that support economic stability and growth.

---

## Features

- Add daily expenses with:
  - Name of expense
  - Amount (KES)
  - Category
- View all expenses in a table with totals
- AI-powered savings advice based on recent expenses
- Beginner-friendly, simple UI with HTML, CSS, and Flask

---

## Tech Stack

- **Frontend:** HTML, CSS
- **Backend:** Python (Flask)
- **Database:** MySQL
- **AI Integration:** OpenAI API
- **Version Control:** GitHub

---

## Installation

1. Clone this repository:
    ```bash
    git clone https://github.com/YOUR_USERNAME/budget-ai-advisor.git
    cd budget-ai-advisor

2. Create a Python virtual environment:
    python3 -m venv venv
    source venv/bin/activate

3. Install dependencies:
    pip install -r requirements.txt

4. Create .env file:
    cp .env.example .env

5. OPENAI_API_KEY=sk-...
    OPENAI_API_KEY=sk-...

## Database Setup
1. Start your MySQL server.
2. Run the schema SQL file to create the database and table:
    mysql -u root -p < schema.sql
    # Enter password: R00t
Database: budget_app
Table: expenses

## Running the App
1. Start Flask:
    flask run
2. Open your browser:
    http://127.0.0.1:5000/
3. You can now add expenses, view expense history, and request AI savings advice.

## Usage
1. Add an Expense: Enter expense name, amount, and category.
2. View Expenses: Check the list of expenses and total spending.
3. Get AI Advice: Click the button to get personalized savings suggestions.

Screenshots:
/screenshots

Notes:
- .env contains sensitive information (OpenAI API key) — do not commit.
- The app is not hosted online; it runs locally.
- AI advice is guidance only and should not be taken as professional financial advice.
- Beginner-friendly — easy to extend with features like charts, CSV export, or category analysis.

License
This project is open-source and licensed under the MIT License.
