# 🔐 Secure IoT Node with Hardware-Based Trust (ESP32 + ATECC)

🚀 A prototype of a **Secure IoT Architecture** implementing device identity, secure communication, data integrity, and tamper detection.

---

## 📌 Overview

This project demonstrates how to build a **secure IoT system** using:

- ESP32 microcontroller  
- ATECC secure element (hardware crypto)  
- MQTT over TLS  
- ECC digital signatures  
- Backend verification (Python)  
- Real-time dashboard  

👉 Only **cryptographically verified data** is accepted and visualized.

---

## 🧠 Architecture
ESP32 + ATECC
↓ (TLS + MQTT)
Secure Broker
↓
Python Backend (Verification Engine)
↓
Flask Dashboard (Live Monitoring)

---

## 🔐 Security Features

✔ Hardware-based device identity (ATECC)  
✔ TLS encrypted communication  
✔ ECC digital signature verification  
✔ Replay attack detection  
✔ Sensor tamper detection  
✔ Device offline detection  

---

## 🚨 Tamper Detection Logic

- ❌ Unknown device → Rejected  
- ❌ Invalid signature → Rejected  
- ❌ Replay attack → Rejected  
- ❌ Abnormal sensor values → Rejected  
- ❌ Device offline → Alert  

---

## 📊 Dashboard Features

- Real-time temperature & humidity  
- Separate charts for visualization  
- Device status (online/offline)  
- Attack detection counter  
- Live system stats  

---

## ⚙️ Technologies Used

### Embedded
- ESP32 (Arduino IDE)
- ATECC608A (Secure Element)
- DHT11 Sensor

### Communication
- MQTT (broker.hivemq.com)
- TLS (port 8883)

### Backend
- Python
- Flask
- Paho MQTT
- Cryptography (ECC verification)

---
## 📁 Project Structure
📦 Secure-IoT
┣ 📜 securenode_draft.ino # ESP32 firmware
┣ 📜 server.py # Backend verification + dashboard
┣ 📁 templates/
┃ ┗ 📜 index.html # Dashboard UI
┣ 📜 README.md

Actually this is my project structure but here i didnt include all!PLEASE IGNORE!:)
---

## 🚀 How to Run

### 1️⃣ ESP32 Setup
- Open `securenode_draft.ino` in Arduino IDE  
- Install required libraries:
  - WiFi
  - PubSubClient
  - ArduinoECCX08
  - DHT  
- Upload to ESP32  

---

### 2️⃣ Backend Setup
pip install flask paho-mqtt cryptography
python3 server.py

---

### 3️⃣ Open Dashboard
http://localhost:5000




