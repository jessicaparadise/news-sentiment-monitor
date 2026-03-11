# news-sentiment-monitor# 

🌍 Real-Time News Sentiment Monitor
An IoT device that fetches live news headlines, analyzes world sentiment,
and displays the result via physical LED indicators.

## 🔴🟡🟢 How It Works

1. **ESP-32** connects to WiFi and calls a REST API every 5 minutes
2. **AWS Lambda** fetches top US headlines from NewsAPI
3. **Sentiment analysis** scores the headlines as POSITIVE, NEUTRAL, or NEGATIVE
4. **DynamoDB** stores historical mood data
5. **Physical LEDs** light up based on the world's mood

## 🛠️ Tech Stack

- **Hardware:** ELEGOO ESP-32, LEDs, breadboard
- **Cloud:** AWS Lambda, API Gateway, DynamoDB
- **Language:** Python (Lambda), C++ (Arduino/ESP-32)
- **APIs:** NewsAPI.org

## 📐 Architecture

NewsAPI → AWS Lambda → DynamoDB↓
API Gateway (REST)
↓
ESP-32 (WiFi) → LED Display

## 📸 Demo
![Untitled](https://github.com/user-attachments/assets/343d6640-96a0-409b-97f0-9c9a30af24db)

## 🚀 What I Learned
- Serverless cloud architecture with AWS
- IoT device programming with ESP-32
- End-to-end system design from hardware to cloud
