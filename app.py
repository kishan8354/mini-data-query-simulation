from flask import Flask, request, jsonify
import sqlite3

# Database Setup
def setup_db():
    conn = sqlite3.connect("mock.db")  # Mock Database File
    cursor = conn.cursor()

    # Create sales table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS sales (
            year INTEGER,
            revenue INTEGER
        )
    ''')

    # Insert dummy sales data
    cursor.execute('INSERT OR IGNORE INTO sales VALUES (2024, 50000)')
    conn.commit()
    conn.close()

# Fetch Data from Mock DB
def fetch_from_db(sql_query):
    conn = sqlite3.connect("mock.db")
    cursor = conn.cursor()
    cursor.execute(sql_query)
    result = cursor.fetchall()
    conn.close()
    return result

app = Flask(__name__)

@app.route('/')
def home():
    return "Backend is working! 🚀"

# Convert natural language to SQL
def convert_to_sql(nl_query):
    if "sales data" in nl_query.lower():
        return "SELECT * FROM sales WHERE year=2024;"
    elif "customer details" in nl_query.lower():
        return "SELECT name, email FROM customers;"
    else:
        return "Unsupported query format"

@app.route('/query', methods=['POST'])
def query():
    data = request.json
    query = data.get('query', '')
    sql_query = convert_to_sql(query)

    if "Unsupported query" not in sql_query:
        result = fetch_from_db(sql_query)
        return jsonify({"query": query, "sql_query": sql_query, "result": result})
    else:
        return jsonify({"error": "Unsupported query format"})

@app.route('/explain', methods=['POST'])
def explain():
    data = request.json
    query = data.get('query', '')
    return jsonify({"explanation": f"Query breakdown for: {query}"})

@app.route('/validate', methods=['POST'])
def validate():
    data = request.json
    query = data.get('query', '')
    if query:
        return jsonify({"valid": True, "message": "Query is valid!"})
    else:
        return jsonify({"valid": False, "message": "Invalid query!"})

if __name__ == '__main__':
    setup_db()  # Setup Mock DB
    app.run(debug=True)
