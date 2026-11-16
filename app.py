from flask import Flask, jsonify, request, send_from_directory
from flask_cors import CORS
import sqlite3
from threat_analyzer import calculate_risk

app = Flask(__name__)
CORS(app)

DATABASE = "database.db"

def get_db():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/login', methods=['POST'])
def login():
    data = request.json

    if data['username'] == "admin" and data['password'] == "admin123":
        return jsonify({
            "status": "success",
            "message": "Login Successful"
        })

    return jsonify({
        "status": "failed",
        "message": "Invalid Credentials"
    })

@app.route('/threats')
def threats():

    conn = get_db()

    threats = conn.execute("""
    SELECT * FROM threats
    """).fetchall()

    conn.close()

    return jsonify([dict(i) for i in threats])

@app.route('/analytics')
def analytics():

    conn = get_db()

    data = conn.execute("""
    SELECT severity,COUNT(*) total
    FROM threats
    GROUP BY severity
    """).fetchall()

    conn.close()

    return jsonify([dict(i) for i in data])

if __name__ == '__main__':
    app.run(debug=True)