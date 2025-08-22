# 🔐 CRYPTOGRAPHY-BASED NETWORK SECURITY ANALYSIS USING SECURE HASHED IDENTITY MESSAGE AUTHENTICATION AND MACHINE LEARNING  

## 📌 PROJECT OVERVIEW  
This project integrates Cryptography and  Machine Learning  to enhance network security.  
It provides a dual-layer defense mechanism:  
- Cryptography (SHA-256, HMAC): Ensures identity authentication and message integrity.  
- Machine Learning (SVM, Random Forest): Detects anomalies and network intrusions in real time.  

✅ GOAL:  A scalable, secure, and intelligent system to prevent unauthorized access and detect cyber threats effectively.  
---
## 🚀 FEATURES  
- 🔑 Secure Login with SHA-256 Hashed Identity
- 🕵️ Anomaly Detection using ML models (SVM, Random Forest)  
- 📊 Real-time Dashboard to monitor traffic & alerts  
- 🛡️ HMAC for message authentication  
- 🔒 Replay & Spoofing attack protection
- 📈 Supports visualization of network logs & threats 

---
## 🏗️ SYSTEM ARCHITECTURE  
1. User Authentication (SHA-256 Hashing)
2. Packet Capture & Feature Extraction
3. Machine Learning-based Intrusion Detection
4. Dashboard (Flask Web App)
---
## ⚙️ TECH STACK  
- Programming Language: Python  
- Frontend: Flask, HTML, CSS  
- Backend: Python (Cryptography + ML models)  
- Machine Learning: Scikit-learn, TensorFlow (optional)  
- Data Handling: Pandas, Numpy  
- Tools: Scapy, Wireshark  
- Dataset: NSL-KDD (Network Security Benchmark Dataset)  
---
## 📂 PROJECT STRUCTURE  
crypto-project/
│── app.py # Flask app (dashboard)
│── train_model.py # Train ML model
│── packet_analyzer.py # Packet sniffing + feature extraction
│── crypto_utils.py # Hashing & HMAC functions
│── static/ # CSS, JS, images
│── templates/ # HTML templates
│── models/ # Saved ML models
│── dataset/ # NSL-KDD dataset
│── README.md # Project Documentation

---
## 📊 DATASET (NSL-KDD)  
- Standard benchmark dataset for **Intrusion Detection Systems (IDS)**  
- Contains **labeled traffic**: normal, DoS, Probe, U2R, R2L attacks  
- Used for training and evaluating ML models  
---
## ▶️ HOW TO RUN  
### 1. Clone the Repository
git clone https://github.com/hema0253/crypto-project.git
cd crypto-project

### 2. Install Dependencies
pip install -r requirements.txt

### 3. Train the Model
python train_model.py

### 4. Run the Web App
python app.py

### 5. Open in Browser
Go to: http://127.0.0.1:5000/

📈 RESULTS
ML Accuracy: ~ [Insert % after training]
Real-time alerts: Shown in dashboard
Attack types detected: DoS, Probe, U2R, R2L

🌍 REAL-WORLD APPLICATIONS
Enterprise Security: Intrusion Detection + Secure Login
Banking & Finance: Fraud detection with crypto-authentication
IoT Security: Authenticate devices + detect anomalies
Government Defense: AI + Cryptography for secure communication

🔮 FUTURE ENHANCEMENTS
Use Deep Learning (LSTM, CNN) for improved detection
Cloud deployment with advanced logging & monitoring
Role-based access for multi-user systems

👨‍💻 CONTRIBUTORS 
B. HEMA PRIYA
CH. THARASRI
K. ANU

📜 LICENSE
This project is for educational and research purposes only.
