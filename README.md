# Essay Generator with Streamlit + FastAPI + Ollama

This project is a simple **Essay Generator** built with:

* **Streamlit** (frontend UI)
* **FastAPI + LangServe** (backend)
* **Ollama LLM (deepseek-r1)** for essay generation

The frontend allows users to enter a topic, sends the request to the backend, and returns an AI-generated essay.

---

## 🚀 Features

* Streamlit web UI for essay input/output.
* FastAPI backend serving a LangChain pipeline.
* Ollama LLM (`deepseek-r1:latest`) for text generation.
* Simple REST integration between frontend and backend.

---

## 📦 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/essay-generator.git
cd essay-generator
```

### 2. Create a Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate   # On Linux/Mac
venv\Scripts\activate      # On Windows
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

*(If you don’t have `requirements.txt`, see [Dependencies](#-dependencies) section below.)*

---

## ▶️ Running the Application

### Step 1: Start FastAPI Backend

Run the backend server with:

```bash
python app.py
```

This will start FastAPI at **[http://127.0.0.1:8000](http://127.0.0.1:8000)**

---

### Step 2: Start Streamlit Frontend

Run the frontend with:

```bash
streamlit run frontend.py
```

Then open the link provided (usually [http://localhost:8501](http://localhost:8501)).

---

### Step 3: Generate Essays 🎉

1. Enter a topic in the Streamlit input box.
2. Click **Generate Essay**.
3. The essay will appear below the input field.

---

## 🛠 Dependencies

If you don’t have a `requirements.txt`, here’s a minimal version:

```txt
fastapi
uvicorn
streamlit
requests
langchain-core
langchain-ollama
langserve
```

---

## 📂 Project Structure

```
essay-generator/
│── app.py          # FastAPI backend with LangServe + Ollama
│── frontend.py     # Streamlit frontend UI
│── requirements.txt
│── README.md
```

---

## ⚡ Notes

* Ensure **Ollama** is installed and running locally with the model `deepseek-r1:latest`.
* You can change the model name in `app.py`:

  ```python
  ollama_llm = OllamaLLM(model="deepseek-r1:latest")
  ```
* The backend must be running **before** starting Streamlit.

---

