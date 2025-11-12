# ============================================
# utils/ai_agent.py  ✅ FIXED VERSION
# ============================================

import re
import pandas as pd
from utils.db_utils import run_query
from utils.openrouter_client import chat_with_openrouter

SYSTEM_PROMPT = """
You are a professional SQL data analyst working on an E-Commerce dataset.

Database tables:
- orders
- order_items
- products
- customers
- sellers
- payments
- reviews
- geolocation
- translation

Your task:
1️⃣ Read the user's question carefully.
2️⃣ Generate a **valid SQLite SQL query** to answer it.
3️⃣ Use the correct table names and columns.
4️⃣ Return only one query in this format:

\\```sql
SELECT ...
\\```

Never include explanations or markdown text outside the SQL block.
"""

def extract_sql(response_text: str):
    """Extract SQL query from model response."""
    if not response_text:
        return None
    match = re.search(r"```sql\s*(.*?)```", response_text, re.DOTALL | re.IGNORECASE)
    return match.group(1).strip() if match else None

def generate_sql_query(user_query: str):
    """Ask OpenRouter LLM to generate SQL query."""
    prompt = f"{SYSTEM_PROMPT}\n\nUser question: {user_query}"
    ai_response = chat_with_openrouter(prompt, temperature=0.3)
    sql_query = extract_sql(ai_response)
    if not sql_query:
        print("⚠️ No SQL detected in model response.")
        print("🔹 Model Response:\n", ai_response)
    return sql_query

def execute_sql(sql_query: str):
    """Execute SQL and summarize insights."""
    if not sql_query:
        return None, "⚠️ No SQL query provided."
    try:
        df = run_query(sql_query)
    except Exception as e:
        return None, f"❌ SQL Execution Error: {e}"
    if df.empty:
        return df, "⚠️ Query executed but returned no results."
    summary_prompt = f"""
You are a business analyst. Summarize the key insights from this result:

{df.head().to_markdown()}
"""
    insight = chat_with_openrouter(summary_prompt, temperature=0.4)
    return df, insight

if __name__ == "__main__":
    print("🔍 Testing AI Agent Module...\n")
    print("💬 Example questions you can try:")
    print("  • Which product category has the highest total sales?")
    print("  • How many unique customers placed orders?")
    print("  • What is the average payment value by category?")
    print("  • Which sellers have the most orders?\n")

    user_question = input("🧠 Enter your question: ")

    sql = generate_sql_query(user_question)
    print("\n🧠 SQL Generated:\n", sql)

    if sql:
        df, insight = execute_sql(sql)
        print("\n📊 Insight:\n", insight)
        if df is not None:
            print("\n📈 Data Preview:\n", df.head())
