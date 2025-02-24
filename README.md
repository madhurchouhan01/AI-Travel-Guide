

---

# 🚀 AI Travel Guide - Setup Guide  

This guide will help you set up the **AI Travel Guide** project, including installing dependencies, initializing the model, starting the backend (Django), and running the frontend (React).  

---

## 1️⃣ **Installing Dependencies**  

Before proceeding, ensure you have **Python 3.8+**, **Node.js 16+**, and **Ollama** installed.  

🔹 **Backend (Django) dependencies:**  
Run the following command inside the **backend project directory**:  
```bash
pip install -r requirements.txt
```  

🔹 **Frontend (React) dependencies:**  
Navigate to the **frontend project directory** and install dependencies:  
```bash
npm install
```  

---

## 2️⃣ **Model Tuning**  

Ensure **Ollama** is installed and accessible.  

### ➤ **Create the AI Model**  
Navigate to the **model directory** in the project folder:  
```bash
cd path/to/your/model/directory  
```  
_(Example: `C:\Users\lenovo\Desktop\AI Travel Guide\AI_Travel_Guide\AI_Travel_Guide\model`)_

Run the command below to create the **travelbuddy** model:  
```bash
ollama create travelbuddy -f modelfile
```  

### ➤ **Test the Model**  
To check if the model is working correctly, run:  
```bash
ollama run travelbuddy
```  
If the model runs successfully and responds to queries, proceed to the next step.

---

## 3️⃣ **Model Initialization**  

Before running the backend, you need to start **Ollama Server**:  

Open the **command prompt (CMD)** in the **project directory** and run:  
```bash
set OLLAMA_HOST=127.0.0.1:11500
ollama serve
```  

🔹 **Important Notes:**  
- This will start the **Ollama Server** on your local machine.  
- **Minimum RAM required**: **8GB** (Make sure to free up unnecessary memory).  
- If running on **Linux or macOS**, use:  
  ```bash
  export OLLAMA_HOST=127.0.0.1:11500
  ollama serve
  ```

---
## 4️⃣ **Database Migrations** 
To apply database migrations, run the following commands:

```sh
python manage.py makemigrations AI_Travel_Guide
python manage.py migrate
```
## 5️⃣ **Backend (Django) Initialization**  

Navigate to the **backend project directory** (where `manage.py` is located):  
```bash
cd path/to/backend  
```  
_(Example: `C:\Users\lenovo\Desktop\AI Travel Guide\AI_Travel_Guide`)_

Start the **Django server**:  
```bash
python manage.py runserver
```  

🔹 **Backend should now be running on:** `http://127.0.0.1:8000/`  

---

## 5️⃣ **Frontend (React) Initialization**  

Navigate to the **frontend directory**:  
```bash
cd path/to/frontend
```  
_(Example: `C:\Users\lenovo\Desktop\AI Travel Guide\frontend\ai-travel-guide`)_

Start the **React development server**:  
```bash
npm start
```  

🔹 **Frontend should now be running on:** `http://localhost:3000/`  

---

## 6️⃣ **Testing the Full System**  

Once all components are running:  
✅ Open `http://localhost:3000/` in your browser.  
✅ Try chatting with the AI Travel Guide.  
✅ Check if the model responds correctly.  

---

## 🔥 **Troubleshooting & Tips**  

### 🛑 **Common Issues & Fixes**  

❌ **Ollama model not responding?**  
✔️ Ensure `ollama serve` is running in CMD.  
✔️ Run `ollama run travelbuddy` to check model response.  

❌ **Backend not working?**  
✔️ Run `python manage.py migrate` before starting Django.  
✔️ Check if the backend is running on `http://127.0.0.1:8000/`.  

❌ **Frontend not loading?**  
✔️ Run `npm install` if dependencies are missing.  
✔️ Restart React with `npm start`.  

---

## 🎯 **Final Setup Checklist**  

✅ **Ollama Model Running** (`ollama serve`)  
✅ **Backend Running** (`python manage.py runserver`)  
✅ **Frontend Running** (`npm start`)  
✅ **AI Chatbot is responding correctly**  

Now you are all set to use **AI Travel Guide!** 🎉  

---
