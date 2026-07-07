# 📰 Multi-Agent News Analysis System

An AI-powered news analysis system that automatically fetches the latest news, cleans and processes the data, analyzes each article using LangChain with the Groq LLM, stores the results in PostgreSQL, and visualizes insights through an interactive Streamlit dashboard.

This project demonstrates an end-to-end AI data pipeline by combining data engineering, large language models, databases, and interactive dashboards.

---

## 📌 Project Overview

News websites publish hundreds of articles every day, making it difficult to quickly understand the latest trends and insights.

This project automates the complete workflow by:

- Fetching the latest news articles using NewsAPI
- Cleaning and preprocessing the data using Pandas
- Classifying each article into a news category
- Performing sentiment analysis
- Generating a concise AI summary
- Storing structured data in PostgreSQL
- Displaying insights through a Streamlit dashboard

---

## 🚀 Features

- 📰 Fetch latest news from NewsAPI
- 🧹 Data cleaning using Pandas
- 🤖 AI-powered news analysis using LangChain + Groq
- 📂 Automatic news categorization
- 😊 Sentiment analysis
- 📝 AI-generated summaries
- 🗄️ PostgreSQL database integration
- 📊 Interactive Streamlit dashboard
- 🔄 Duplicate news detection
- 📈 News statistics and visualizations

---

## 🛠️ Tech Stack

| Technology | Purpose |
|------------|---------|
| Python | Backend Development |
| LangChain | AI Workflow |
| Groq API (Llama 3.1) | Category, Sentiment & Summary |
| NewsAPI | News Collection |
| Pandas | Data Cleaning |
| PostgreSQL | Database |
| pgAdmin | Database Management |
| Streamlit | Dashboard |
| Plotly | Data Visualization |

---

## 🏗️ Project Workflow

```
                NewsAPI
                   │
                   ▼
          News Fetch Agent
                   │
                   ▼
      Data Cleaning Agent (Pandas)
                   │
                   ▼
          PostgreSQL Database
                   │
                   ▼
         AI Analysis Agent
     (Category + Sentiment + Summary)
                   │
                   ▼
          PostgreSQL Update
                   │
                   ▼
         Streamlit Dashboard
```

---

## 🤖 Agents Used

### 📰 News Fetch Agent
- Fetches the latest news articles from NewsAPI.
- Prevents duplicate articles from being stored.

### 🧹 Data Cleaning Agent
- Cleans missing values.
- Formats dates.
- Prepares structured data using Pandas.

### 🤖 AI Analysis Agent
Uses LangChain with the Groq LLM to analyze every news article and generate:
- News Category
- Sentiment
- Summary

### 🗄️ Database Agent
Stores processed news into PostgreSQL and updates analysis results.

---

## 📊 Dashboard Features

The Streamlit dashboard displays:

- Total News Articles
- Category Distribution
- Sentiment Distribution
- News Source Analysis
- Latest News Table
- Interactive Charts

---

## 💡 Challenges Faced & Solutions

### 1. Duplicate News

**Problem**

Refreshing the application repeatedly inserted the same articles into the database.

**Solution**

Implemented PostgreSQL unique constraints with:

```sql
ON CONFLICT(title) DO NOTHING;
```

Only newly published articles are stored.

---

### 2. Slow AI Processing

**Problem**

Initially, category, sentiment, and summary were processed separately, resulting in multiple AI requests for each article.

**Solution**

Combined the analysis into a single AI analysis workflow, reducing API calls and improving execution time.

---

### 3. Incorrect Categories

**Problem**

The LLM occasionally generated categories outside the predefined list.

Examples:

- Crime
- Finance
- Technology | Business

**Solution**

Added prompt constraints and output validation before storing results in PostgreSQL.

---

### 4. Database Growth

**Problem**

Every refresh continuously increased the database size.

**Solution**

Limited the number of fetched articles and implemented duplicate detection to keep the database manageable.

---

## 📂 Project Structure

```
multi-agent_news_analysis/

├── agents/
│   └── analysis_agent.py
│
├── dashboard/
│   └── app.py
│
├── database/
│   ├── db.py
│   └── news_repository.py
│
├── pipeline/
│   └── pipeline.py
│
├── utils/
│   ├── data_cleaner.py
│   └── news_update.py
│
├── news_fetcher.py
├── groq_llm.py
├── main_analysis.py
├── requirements.txt
└── README.md
```

---

## ▶️ Installation

Clone the repository

```bash
git clone https://github.com/bhavabgarg/multi-agent_news_anlysis.git
```

Move into the project directory

```bash
cd multi-agent_news_anlysis
```

Install dependencies

```bash
pip install -r requirements.txt
```

Create a `.env` file

```env
GROQ_API_KEY=your_groq_api_key
NEWS_API_KEY=your_newsapi_key

DB_HOST=localhost
DB_NAME=news_analysis
DB_USER=postgres
DB_PASSWORD=your_password
DB_PORT=5432
```

Run the Streamlit application

```bash
streamlit run dashboard/app.py
```

---

## 📈 Future Improvements

- Add support for multiple news sources
- Improve AI prompt engineering
- Export reports to PDF or Excel
- Deploy using Docker and cloud platforms

---

## 🎯 Learning Outcomes

This project helped me gain practical experience with:

- LangChain
- Large Language Models (Groq)
- Prompt Engineering
- PostgreSQL
- Pandas Data Processing
- API Integration
- Streamlit Dashboard Development
- End-to-End AI Pipeline Design
- Error Handling and Performance Optimization

---

## 👨‍💻 Author

**Bhava Garg**

GitHub: https://github.com/bhavabgarg

---

⭐ If you found this project interesting, feel free to star the repository!
