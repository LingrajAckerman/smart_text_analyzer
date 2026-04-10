# 🚀 Smart Text Analyzer

A production-ready full-stack application that analyzes input text and provides useful insights such as word count, sentence count, top frequent words, and estimated reading time.

---

## 📌 Live Demo

* 🌐 Frontend: https://your-frontend-url
* 🔗 Backend API Docs: https://your-backend-url/docs

---

## 🧠 Features

* ✅ Word count calculation
* ✅ Character count calculation
* ✅ Sentence detection
* ✅ Top 5 most frequent words (case-insensitive)
* ✅ Estimated reading time (based on 200 words/minute)
* ✅ Input validation and error handling
* ✅ Clean and responsive UI
* ✅ Fully deployed application

---

## 🛠️ Tech Stack

* **Backend:** FastAPI
* **Frontend:** Streamlit
* **Language:** Python
* **Deployment:** Render (Backend), Streamlit Cloud (Frontend)

---

## ⚙️ API Endpoint

### `POST /analyze`

#### Request Body:

```json
{
  "text": "Enter your text here"
}
```

#### Response:

```json
{
  "word_count": 0,
  "character_count": 0,
  "sentence_count": 0,
  "top_words": [],
  "reading_time_minutes": 0.0
}
```

---

## 🖥️ Local Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```

---

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 3. Run Backend (FastAPI)

```bash
uvicorn main:app --reload
```

Backend will run at:

```
http://127.0.0.1:8000
```

---

### 4. Run Frontend (Streamlit)

```bash
streamlit run app.py
```

---

## 📂 Project Structure

```
.
├── main.py           # FastAPI backend
├── app.py            # Streamlit frontend
├── requirements.txt  # Dependencies
├── README.md         # Project documentation
```

---

## 🚧 Error Handling

* Handles empty input text
* Prevents API crashes with proper validation
* Returns meaningful error messages

---

## 🔮 Future Improvements

* Stopword removal for better word frequency analysis
* File upload support (.txt, .pdf)
* Enhanced UI/UX
* User authentication and history tracking

---

## 👨‍💻 Author

**Lingraj Jamkhandi**

---

## ✅ Notes

* This project was built as part of a time-bound technical assessment.
* Focus was on **code quality, functionality, and production readiness** rather than feature breadth.

---
