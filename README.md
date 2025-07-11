# 📚 PDF Chat AI

![Python](https://img.shields.io/badge/Python-3.9+-blue.svg?logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Built%20With-Streamlit-orange?logo=streamlit)
![License](https://img.shields.io/badge/License-MIT-green.svg)

**PDF Chat AI** is an intelligent web app built with **Streamlit** that allows users to **interact with PDF documents through natural language**. Whether it's research papers, reports, or contracts — just upload your PDFs and start asking questions. The system leverages **advanced transformer-based models** to deliver fast, accurate, and context-aware answers.

---

## ✨ Features

- 📂 **Multi-PDF Upload** – Chat with one or multiple PDFs simultaneously.
- 🤖 **AI-Powered Q&A** – Powered by:
  - 🧠 `google/flan-t5-base` – For high-quality natural language generation.
  - 🧠 `hkunlp/instructor-xl` – For generating dense, semantically rich embeddings.
- 🔍 **Semantic Search with FAISS** – Retrieves the most relevant chunks of content from your PDFs.
- 💬 **Conversational Memory** – Keeps track of the current conversation for smoother interactions.
- 🎨 **Modern UI** – Clean, user-friendly interface with custom chat bubbles.

---

## 🧠 How It Works

1. **Upload PDFs**  
   Drop one or more PDFs into the app interface.

2. **Preprocessing**  
   The app extracts text using `PyPDF2`, chunks the content, and embeds it using the `Instructor-XL` model.

3. **Vector Search**  
   A **FAISS** index allows fast semantic retrieval of relevant chunks.

4. **Language Generation**  
   Retrieved context is passed to `FLAN-T5` to generate a helpful, human-like response.

---

## ⚙️ Tech Stack

| Technology | Purpose |
|------------|---------|
| [Streamlit](https://streamlit.io/) | Web app frontend |
| [LangChain](https://www.langchain.com/) | Document Q&A pipeline |
| [FAISS](https://github.com/facebookresearch/faiss) | Fast semantic search |
| [Hugging Face Transformers](https://huggingface.co/) | Embedding + generation models |
| [PyPDF2](https://pypi.org/project/PyPDF2/) | PDF text extraction |

---

## 🚀 Getting Started

### Prerequisites

- Python 3.9 or higher
- pip or conda
- Internet connection (for downloading models)

---

## ⚡ Model Configuration
The following models are used:

Embedding Model: hkunlp/instructor-xl

LLM for Answer Generation: google/flan-t5-base

##📝 Notes
🖥️ Running on CPU is supported but may be slower.

⚡ For best performance, run on a machine with GPU acceleration.

📁 Large PDF files may take longer to index; consider chunk size and overlap tuning for optimization.

---

##📄 License
This project is licensed under the MIT License.

---

##🤝 Contributing
Pull requests are welcome! For major changes, please open an issue first to discuss what you’d like to change.

# Create a new branch
git checkout -b feature/my-feature

# Commit your changes
git commit -m "Add new feature"

# Push to your fork
git push origin feature/my-feature

---

### Installation

```bash
# Clone the repository
git clone https://github.com/your-username/pdf-chat-pro.git
cd pdf-chat-pro

# Install required packages
pip install -r requirements.txt
```

##Running the App

streamlit run app.py
