# 🧠 Digit Recognizer ML App — Flask + Docker (MLOps Lab 7)

This project demonstrates how to **train, deploy, and containerize a machine learning model** using **Flask** and **Docker**.  
It serves as an MLOps practice lab showing end-to-end integration — from model training to containerized web deployment.

---

## 🚀 Project Overview

A **Digit Recognition Web App** trained on the MNIST handwritten digits dataset.  
Users can draw a digit (0–9) on the web interface, and the Flask API predicts it using a trained Random Forest model.

---

## 🧩 Tech Stack

- **Python 3.9**
- **Flask** – Web framework
- **scikit-learn** – Model training (RandomForest)
- **NumPy** – Data manipulation
- **Pillow** – Image processing
- **Docker** – Containerization platform

---

## ⚙️ Folder Structure

# 🧠 Digit Recognizer ML App — Flask + Docker (MLOps Lab 7)

This project demonstrates how to **train, deploy, and containerize a machine learning model** using **Flask** and **Docker**.  
It serves as an MLOps practice lab showing end-to-end integration — from model training to containerized web deployment.

---

## 🚀 Project Overview

A **Digit Recognition Web App** trained on the MNIST handwritten digits dataset.  
Users can draw a digit (0–9) on the web interface, and the Flask API predicts it using a trained Random Forest model.

---

## 🧩 Tech Stack

- **Python 3.9**
- **Flask** – Web framework
- **scikit-learn** – Model training (RandomForest)
- **NumPy** – Data manipulation
- **Pillow** – Image processing
- **Docker** – Containerization platform

---

## ⚙️ Folder Structure


Lab7_DockerFlaskApp/
├── app.py # Flask app serving predictions
├── train_model.py # Trains model and saves model.pkl
├── model.pkl # Trained RandomForest model
├── requirements.txt # Dependencies for Flask and ML
├── Dockerfile # Build instructions for container
├── templates/
│ └── index.html # Frontend with drawing canvas
└── README.md # Project overview and usage



---

## 🧠 How It Works

1️⃣ **Train the model**
```bash
python3 train_model.py
2️⃣ Run Flask app locally
python3 app.py
Visit: http://localhost:5000
3️⃣ Build Docker image
docker build -t baaja/digit-recognizer .
4️⃣ Run inside Docker
docker run -p 5000:5000 baaja/digit-recognizer
Then open again: http://localhost:5000



🧾 Author

Mohamed Bin Badhusha (Baaja)
M.Tech Data Engineering — IIT Jodhpur
Amazon | Business Analyst | Aspiring BIE / Data Engineer

