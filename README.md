# 🚀 Mini Data Query Simulation Engine

This project is a lightweight backend service that simulates a Gen AI-powered data query system.

---

## 📚 Project Overview
- **/query:** Converts natural language queries to SQL and fetches data.
- **/explain:** Provides a breakdown of the query.
- **/validate:** Validates query format.

---

## ⚙️ Tech Stack
- **Backend:** Flask (Python)
- **Database:** SQLite (Mock DB)
- **API Testing:** Postman

---

## 🛠️ Setup Instructions

### 1. Clone the Repository
git clone [https://github.com/kishan8354/mini-data-query-simulation]

### 2. Navigate to the Project Folder
cd mini-data-query-simulation

### 3. Create a Virtual Environment
python -m venv venv

### 4. Activate the Virtual Environment
#### On Windows:
venv\Scripts\activate
#### On macOS/Linux:
source venv/bin/activate

### 5. Install Required Dependencies
pip install -r requirements.txt

### 6. Run the Flask Application
python app.py

## 🔥 API Documentation
### 1. /query (POST)
Description: Accepts a natural language query and returns the translated SQL query with mock results.
Endpoint:
POST /query

Request Body:
{
  "query": "Show me sales data for 2024"
}
Response:
{
  "query": "Show me sales data for 2024",
  "sql_query": "SELECT * FROM sales WHERE year=2024;",
  "result": [(2024, 50000)]
}

### 2. /explain (POST)
Description: Returns a simulated query breakdown.
Endpoint:
POST /explain

Request Body:
{
  "query": "Show me sales data for 2024"
}
Response:
{
  "explanation": "Query breakdown for: Show me sales data for 2024"
}

### 3. /validate (POST)
Description: Checks if the query is valid.
Endpoint:
POST /validate

Request Body:
{
  "query": "Show me sales data for 2024"
}
Response:
{
  "valid": true,
  "message": "Query is valid!"
}

## 📝 Sample Query Example
To test APIs, use Postman or curl:
Using curl:
curl -X POST -H "Content-Type: application/json" -d '{"query":"Show me sales data for 2024"}' http://127.0.0.1:5000/query

## 🚀 Deployment Instructions
### 1. Push to GitHub
git add .
git commit -m "Initial commit"
git push origin main

### 2. Deploy on Render / Heroku / Railway
Follow the platform's instructions for Flask deployment.
Make sure to define the PORT environment variable if required.

## 📄 License
This project is licensed under the MIT License.
