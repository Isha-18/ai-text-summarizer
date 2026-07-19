# 📝 AI Text Summarizer

An AI-powered text summarization application built using **Python**, **Streamlit**, and the **Groq API**. The application generates concise summaries, key bullet points, and important keywords from long-form text using a Large Language Model (LLM).

---

## 🚀 Features

- 📄 Summarizes long articles into concise text
- 📌 Extracts key bullet points
- 🏷 Generates relevant keywords
- ⚡ Fast inference using Groq's Llama 3.3 model
- 🎨 Interactive Streamlit interface
- 🔒 Secure API key management using environment variables

---

## 🛠 Tech Stack

- Python
- Streamlit
- Groq API
- Llama 3.3 70B Versatile
- python-dotenv

---

## 📂 Project Structure

```text
AI-Text-Summarizer/
│
├── app.py               # Streamlit UI
├── ai_client.py         # Groq API interaction
├── prompts.py           # Prompt templates
├── requirements.txt
├── .gitignore
├── README.md
└── .env                 # API key (not committed)
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/<your-username>/ai-text-summarizer.git
```

### 2. Navigate to the project

```bash
cd ai-text-summarizer
```

### 3. Create a virtual environment

**Windows**

```bash
python -m venv venv
```

Activate it:

```bash
venv\Scripts\activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Create a `.env` file

```env
GROQ_API_KEY=your_api_key_here
```

### 6. Run the application

```bash
streamlit run app.py
```

---

## 📸 Demo

> Add screenshots of the application here.

Suggested screenshots:

- Home screen
- Article input
- Generated summary
- Bullet points and keywords

---

## 📖 Concepts Learned

This project helped me understand:

- API Keys & Environment Variables
- Large Language Models (LLMs)
- Prompt Engineering
- Temperature & Tokens
- Structured JSON Outputs
- Streamlit UI Development
- API Integration
- JSON Parsing
- Exception Handling
- Project Structuring

---

## 🔮 Future Improvements

- PDF summarization
- Multi-language support
- AI Translation
- Download summary as PDF
- Multiple summarization styles
- RAG-based document summarization

---

## 👩‍💻 Author

**Isha Parab**

Software Engineer | Learning AI Engineering by building practical projects.

Feel free to connect with me on LinkedIn and explore more of my projects!
