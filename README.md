# 📝 Blog Generation using LLaMA-2 and Streamlit

## 📌 Project Overview

This project is a Streamlit-based application that uses a locally hosted LLaMA-2 (7B Chat) model for interactive text and blog generation. The application runs entirely on your local machine without relying on external APIs.

Users can enter a topic or prompt and generate blog-style content in real time through a simple Streamlit interface. This project demonstrates how large language models can be deployed locally using GGML weights and integrated into lightweight Python applications.

---

## 🚀 Steps to Run the Program

### 1️⃣ Download the Model

Download the model from the link below and place it in the project directory:

👉 https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGML/tree/main

After downloading, update the model path accordingly in `app.py`.

---

### 2️⃣ Create a Conda Environment

```bash
conda create -p venv python=3.10 -y

conda activate venv/

python -m pip install -r requirements.txt

streamlit run app.py
