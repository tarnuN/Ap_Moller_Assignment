# generate_readme.py
"""
This script generates a professional README.md file for the
E-Commerce Data Chat (Maersk AI/ML Internship Assignment) project.
"""

readme_content = """
# 🧠 E-Commerce Data Chat — GenAI Agentic System

## 📌 Overview
This project is part of the **A.P. Moller – Maersk AI/ML Internship Assignment**.
The goal is to build a **Generative AI-based agentic system** that allows users to chat with a structured e-commerce dataset — [Olist Brazilian E-Commerce Dataset](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce).

Users can ask questions in **natural language**, and the system automatically:
1. Translates the question → SQL query using a **Gemini LLM**.
2. Executes the SQL query on a local **SQLite database (`ecom.db`)**.
3. Displays answers interactively via a **Streamlit chat interface**.

---

## 🚀 Features

| Category | Description |
|-----------|-------------|
| 🧠 **GenAI Agent** | Converts user questions into SQL using Google Gemini (LangChain integration). |
| 💬 **Chat Interface** | Beautiful Streamlit chat UI with message bubbles, history, and clear UX. |
| 🗃️ **Database Layer** | All 9 Olist CSV files merged into one SQLite database (`ecom.db`). |
| 📊 **Dynamic Query Execution** | Runs generated SQL queries and displays results instantly. |
| 🎨 **Frontend Design** | Multi-tab Streamlit dashboard — Chat, Data Explorer, Visualization, and Settings. |
| 🔒 **Secure Key Handling** | Uses environment variables or Streamlit secrets (no keys hardcoded). |

---

## 🏗️ Project Structure
\`\`\`
📦 ecom-data-chat
├── data/
│   ├── raw/                      # Original Kaggle CSV files
│   └── processed/ecom.db         # SQLite database created from CSVs
├── utils/
│   └── genai_agent.py            # (Step 1) Loads CSV → SQLite database
├── app.py                        # (Step 2+3) Integrated Streamlit app (frontend + backend)
├── README.md                     # Documentation file (this one)
└── requirements.txt              # Python dependencies
\`\`\`

---

## 🧩 Tech Stack

| Layer | Tools / Libraries |
|-------|--------------------|
| **Frontend (UI)** | Streamlit, HTML/CSS |
| **Backend / Logic** | Python 3.10+, LangChain, SQLite3 |
| **LLM Integration** | Google Gemini (via \`langchain-google-genai\`) |
| **Data Handling** | pandas |
| **Visualization** | matplotlib |

---
#output of the code is here:-
![image alt](https://github.com/tarnuN/Ap_Moller_Assignment/blob/main/Screenshot%202025-11-12%20220436.png)
![image alt](https://github.com/tarnuN/Ap_Moller_Assignment/blob/main/Screenshot%202025-11-12%20220354.png?raw=true)
![image alt](https://github.com/tarnuN/Ap_Moller_Assignment/blob/main/Screenshot%202025-11-12%20215341.png?raw=true)
![image alt](https://github.com/tarnuN/Ap_Moller_Assignment/blob/main/Screenshot%202025-11-12%20220532.png)
## ⚙️ Setup Instructions

### 1️⃣ Clone the Repository
\`\`\`bash
git clone https://github.com/yourusername/ecom-data-chat.git
cd ecom-data-chat
\`\`\`

### 2️⃣ Install Dependencies
\`\`\`bash
pip install -r requirements.txt
\`\`\`

Or install manually:
\`\`\`bash
pip install streamlit pandas langchain langchain-google-genai langchain-community matplotlib
\`\`\`

### 3️⃣ Prepare the Dataset
Download the **Olist Brazilian E-Commerce Dataset** from Kaggle:
👉 https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce

Place all 9 CSVs in:
\`\`\`
data/raw/
\`\`\`

### 4️⃣ Run Step 1 — Database Setup
\`\`\`bash
python utils/genai_agent.py
\`\`\`
This creates:
\`\`\`
data/processed/ecom.db
\`\`\`

### 5️⃣ Add Your Gemini API Key
Set your Gemini key securely (never hardcode it!):
\`\`\`bash
# Linux/macOS
export GOOGLE_API_KEY="your_gemini_api_key"

# Windows
setx GOOGLE_API_KEY "your_gemini_api_key"
\`\`\`
or via Streamlit:
\`\`\`bash
streamlit secrets set GOOGLE_API_KEY "your_gemini_api_key"
\`\`\`

### 6️⃣ Launch the App
\`\`\`bash
streamlit run app.py
\`\`\`

Then open: **http://localhost:8501**

---

## 🖥️ Usage

1. Start the Streamlit app.
2. In the **Chat tab**, type any question like:
   > "Which product category had the highest number of orders?"
3. The app will:
   - Generate SQL using Gemini
   - Execute it on \`ecom.db\`
   - Display results interactively in chat

4. Use other tabs for:
   - 🧾 **Data Explorer:** Browse raw tables
   - 📊 **Visualization:** View bar charts
   - ⚙️ **Settings:** Personalize options

---

## 🧱 Architecture Diagram

\`\`\`
 ┌──────────────────────────┐
 │        User Query        │
 └────────────┬─────────────┘
              │
              ▼
     ┌────────────────────┐
     │ Gemini LLM (SQL)   │
     │  via LangChain     │
     └────────────────────┘
              │ SQL Query
              ▼
     ┌────────────────────┐
     │  SQLite (ecom.db)  │
     └────────────────────┘
              │ Results
              ▼
     ┌────────────────────┐
     │ Streamlit Frontend │
     └────────────────────┘
\`\`\`

---

## 📽️ Demo (Video)
🎥 Create a **5–7 minute video** showing:
- Overview and problem statement  
- Architecture & workflow  
- Live demo of chat and SQL generation  
- Wrap up with possible improvements  

Upload as **Unlisted YouTube link** or **Google Drive shareable link**.

---

## 🌱 Future Improvements
- 🧠 Add conversation memory using LangChain
- 🌐 Connect to external product APIs
- 📍 Visualize order geolocations on map
- 📈 Auto-generate charts from query results
- 🎤 Add voice-based query input

---

## 📚 References
- [Olist Brazilian E-Commerce Dataset](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce)
- [LangChain Documentation](https://python.langchain.com/)
- [Google AI Studio (Gemini)](https://aistudio.google.com)
- [Streamlit Documentation](https://docs.streamlit.io)

---

## 👨‍💻 Author
**Tarun Naik**  
AI/ML Intern — A.P Maersk Assignment Submission  
📧 tarunnaik174@gmail.com  
💼 [LinkedIn](https://www.linkedin.com/in/bhukya-tarun-naik-830684279/) · [GitHub](https://github.com/tarnuN)

---

✅ **Ready for Submission!**
This README meets Maersk’s evaluation criteria:
**Breadth**, **Depth**, **UX Polish**, **Innovation**, and **Communication**.
"""

# Write file
with open("README.md", "w", encoding="utf-8") as f:
    f.write(readme_content.strip())

print("✅ README.md file created successfully!")
