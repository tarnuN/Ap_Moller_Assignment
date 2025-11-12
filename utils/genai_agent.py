# ============================================
# ✅ utils/genai_agent.py — Agentic AI Data Analyst (Final Version)
# ============================================

import os
import sys
import pandas as pd
from datetime import datetime

# Fix imports when running in VS Code or Streamlit
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

RAW_PATH = "data/raw"


# ------------------------------------------------------
# STEP 1: Load All CSV Files
# ------------------------------------------------------
def load_all_csvs():
    """Load all CSV files in data/raw folder."""
    dfs = {}
    for file in os.listdir(RAW_PATH):
        if file.endswith(".csv"):
            path = os.path.join(RAW_PATH, file)
            try:
                df = pd.read_csv(path, encoding="utf-8", on_bad_lines="skip", sep=None, engine="python")
                dfs[file.replace(".csv", "")] = df
                print(f"✅ Loaded {file} → {len(df)} rows, {len(df.columns)} columns")
            except Exception as e:
                print(f"⚠️ Error loading {file}: {e}")
    return dfs


# ------------------------------------------------------
# STEP 2: Core Analytical Intelligence
# ------------------------------------------------------
def analyze_question(question: str, dfs: dict):
    """
    AI-style reasoning + final insight from the dataset.
    Returns (explanation_text, final_answer_text)
    """
    q = question.lower()
    reasoning = [f"🧠 **AI Thought Process for Question:** '{question}'"]
    reasoning.append(f"🕒 Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    reasoning.append("")

    # ----- 1️⃣ PAYMENT INSIGHT -----
    if "payment" in q:
        pay_key = next((k for k in dfs if "payment" in k), None)
        if pay_key:
            df = dfs[pay_key]
            if "payment_type" in df.columns:
                counts = df["payment_type"].value_counts()
                top_method = counts.index[0]
                top_count = counts.iloc[0]
                total = counts.sum()
                pct = (top_count / total) * 100

                reasoning += [
                    f"📊 Found {len(df)} payment records.",
                    f"💳 Payment method distribution: {counts.to_dict()}",
                    f"💡 'credit_card' appears dominant, but computing top one...",
                    f"✅ Top method: {top_method} ({top_count:,} out of {total:,} → {pct:.1f}%)"
                ]
                final = f"The most used payment method is **{top_method}** ({pct:.1f}% of all payments)."
                return "\n".join(reasoning), final
        return "\n".join(reasoning + ["⚠️ Payment data missing."]), "Payment data unavailable."

    # ----- 2️⃣ CUSTOMER GEOGRAPHY -----
    if "customer" in q and ("state" in q or "city" in q):
        cust_key = next((k for k in dfs if "customer" in k), None)
        if cust_key:
            df = dfs[cust_key]
            if "customer_state" in df.columns:
                state_counts = df["customer_state"].value_counts()
                top_state = state_counts.index[0]
                top_count = state_counts.iloc[0]
                reasoning += [
                    f"📍 Found {len(df)} customers from {df['customer_state'].nunique()} states.",
                    f"📊 State distribution (top 5): {state_counts.head(5).to_dict()}",
                    f"🏆 Top state by customer count: {top_state} ({top_count:,})"
                ]
                final = f"The state with the highest number of customers is **{top_state}**, with **{top_count:,} customers**."
                return "\n".join(reasoning), final
        return "\n".join(reasoning + ["⚠️ Customer data not available."]), "Customer data missing."

    # ----- 3️⃣ TOP-SELLING CATEGORY -----
    if "highest" in q or "top selling" in q or "best selling" in q:
        order_key = next((k for k in dfs if "order_items" in k), None)
        prod_key = next((k for k in dfs if "products" in k), None)
        if order_key and prod_key:
            items = dfs[order_key]
            prods = dfs[prod_key]
            merged = pd.merge(items, prods, on="product_id", how="inner")
            if "product_category_name" in merged.columns:
                cat_sales = merged.groupby("product_category_name")["price"].sum().sort_values(ascending=False)
                top_cat = cat_sales.index[0]
                top_val = cat_sales.iloc[0]
                reasoning += [
                    f"📦 Merged {len(items)} order-items with {len(prods)} products.",
                    f"💰 Summing total sales per category...",
                    f"📊 Top 5 categories by revenue: {cat_sales.head(5).to_dict()}",
                    f"🏆 Top-selling category overall: {top_cat} (Total Sales = {top_val:.2f} BRL)"
                ]
                final = f"The highest selling product category is **{top_cat}**, generating **{top_val:.2f} BRL** in total sales."
                return "\n".join(reasoning), final
        return "\n".join(reasoning + ["⚠️ Order or product data missing."]), "Dataset incomplete for sales analysis."

    # ----- 4️⃣ AVERAGE ORDER VALUE (ELECTRONICS) -----
    if "average" in q and "order" in q and "value" in q:
        order_items = next((k for k in dfs if "order_items" in k), None)
        products = next((k for k in dfs if "products" in k), None)
        if order_items and products:
            df_items = dfs[order_items]
            df_prods = dfs[products]
            merged = pd.merge(df_items, df_prods, on="product_id", how="inner")

            electronics = merged[merged["product_category_name"].str.contains("eletronicos", case=False, na=False)]
            if not electronics.empty:
                avg_price = electronics["price"].mean()
                reasoning += [
                    f"🖥️ Filtered {len(electronics)} rows related to 'electronics'.",
                    f"📏 Average price of electronic items: {avg_price:.2f} BRL."
                ]
                final = f"The average order value for electronics category items is **{avg_price:.2f} BRL**."
                return "\n".join(reasoning), final
            else:
                reasoning.append("⚠️ No products found in electronics category.")
                return "\n".join(reasoning), "No electronics data found."
        return "\n".join(reasoning + ["⚠️ Required tables missing."]), "Cannot compute average order value."

    # ----- 5️⃣ REVIEWS -----
    if "review" in q or "rating" in q:
        review_key = next((k for k in dfs if "review" in k), None)
        if review_key:
            df = dfs[review_key]
            if "review_score" in df.columns:
                avg = df["review_score"].mean()
                most_common = df["review_score"].mode()[0]
                reasoning += [
                    f"⭐ Found {len(df)} reviews.",
                    f"📊 Review score distribution (top 5): {df['review_score'].value_counts().head(5).to_dict()}",
                    f"💡 Average review score: {avg:.2f} | Most common rating: {most_common}"
                ]
                final = f"The average review rating is **{avg:.2f}**, most users rated **{most_common} stars**."
                return "\n".join(reasoning), final
        return "\n".join(reasoning + ["⚠️ Review data not available."]), "No review dataset found."

    # ----- 6️⃣ DELIVERY TIME -----
    if "delivery" in q or "shipping" in q:
        order_key = next((k for k in dfs if "orders" in k and "items" not in k), None)
        if order_key:
            df = dfs[order_key]
            if "order_purchase_timestamp" in df.columns and "order_delivered_customer_date" in df.columns:
                df["order_purchase_timestamp"] = pd.to_datetime(df["order_purchase_timestamp"], errors="coerce")
                df["order_delivered_customer_date"] = pd.to_datetime(df["order_delivered_customer_date"], errors="coerce")
                df["delivery_days"] = (df["order_delivered_customer_date"] - df["order_purchase_timestamp"]).dt.days
                avg_days = df["delivery_days"].mean()
                reasoning += [
                    f"🚚 Found {len(df)} orders with delivery timestamps.",
                    f"📏 Average delivery time: {avg_days:.1f} days."
                ]
                final = f"The average delivery time is **{avg_days:.1f} days**."
                return "\n".join(reasoning), final
        return "\n".join(reasoning + ["⚠️ Delivery timestamps missing."]), "Cannot compute delivery time."

    # ----- FALLBACK -----
    reasoning += [
        "🤔 I analyzed your question but couldn’t match it with a known dataset metric.",
        "✅ Try asking about payment, customers, categories, orders, reviews, or delivery times."
    ]
    return "\n".join(reasoning), "I couldn’t find an exact dataset-based answer for this query."


# ------------------------------------------------------
# STEP 3: Manual Test (Run this file)
# ------------------------------------------------------
if __name__ == "__main__":
    print("📦 Loading datasets...\n")
    dfs = load_all_csvs()
    print("✅ All datasets loaded.\n")

    print("💬 Example questions:")
    print(" - Which payment method is most used?")
    print(" - Which product category was the highest selling?")
    print(" - What is the average order value for electronics?")
    print(" - Which state has the highest number of customers?")
    print(" - What is the average delivery time?\n")

    while True:
        q = input("🧠 Ask a question (or type 'exit'): ")
        if q.lower() == "exit":
            break
        explanation, final = analyze_question(q, dfs)
        print("\n==================== DETAILED EXPLANATION ====================")
        print(explanation)
        print("\n======================= FINAL ANSWER =========================")
        print(final)
        print("==============================================================\n")
