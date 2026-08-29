# 🩸 AI Health Analyzer

AI Health Analyzer is a Generative AI-powered web application that analyzes blood test reports and presents the results in an easy-to-understand format.

The application uses **Google Gemini, LangChain, and Streamlit** to identify important blood test values, summarize the report in simple language, and provide general dietary suggestions based on the supplied report.

> **Disclaimer:** This project is intended for educational and demonstration purposes only. It does not provide medical diagnosis or replace professional medical advice.

---

## ✨ Features

- 🩸 **Blood Report Analysis** – Analyzes blood test values from a pasted report.
- 📊 **Value Classification** – Identifies values as HIGH, LOW, or NORMAL using reference ranges provided in the report.
- 🧠 **AI Health Summary** – Generates a concise and easy-to-understand summary of important findings.
- 🥗 **Diet Suggestions** – Provides practical Indian dietary suggestions including:
  - Food to avoid
  - Food to eat more of
- ⚡ **Single LLM Call** – Uses a consolidated prompt to reduce API calls and improve response time.
- 🖥️ **Interactive UI** – Simple web interface built using Streamlit.

---

## 🛠️ Tech Stack

- **Python**
- **Google Gemini API**
- **LangChain**
- **Streamlit**
- **python-dotenv**
- **uv** – Python package and environment management

---

## ⚙️ How It Works

```text
Blood Report
     │
     ▼
Streamlit Interface
     │
     ▼
LangChain
     │
     ▼
Google Gemini
     │
     ├── Identifies important blood values
     ├── Classifies values using report reference ranges
     ├── Generates a health summary
     └── Generates dietary suggestions
     │
     ▼
Results displayed in Streamlit
```

---

## 📁 Project Structure

```text
AI-Health-Analyser/
│
├── app.py
├── sample_blood_report.txt
├── Health_analysis.ipynb
├── pyproject.toml
├── uv.lock
├── .python-version
├── .gitignore
└── README.md
```

> `.env` and `.venv` are intentionally excluded from GitHub.

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone <your-repository-url>
cd AI-Health-Analyser
```

### 2. Install dependencies

If you have `uv` installed:

```bash
uv sync
```

### 3. Configure the Gemini API key

Create a `.env` file in the project root:

```env
GOOGLE_API_KEY=your_google_api_key
```

Do not commit your `.env` file to GitHub.

### 4. Run the application

```bash
uv run streamlit run app.py
```

The Streamlit application will open in your browser.

---

## 🔒 Privacy & Safety

API keys are stored using environment variables and are excluded from version control through `.gitignore`.

The AI is instructed to use the reference ranges supplied in the report and not to diagnose medical conditions.

---

## 🔮 Future Improvements

- Upload PDF blood reports
- Automatic report text extraction
- Structured output using LangChain
- Improved report visualization
- Support for additional report formats
- Export analysis as PDF

---

## 👩‍💻 Author

**Mahak Bansal**

Built as a hands-on Generative AI project using Gemini, LangChain, and Streamlit.