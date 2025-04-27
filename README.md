# 🌦️ Weather Tracker Bot ⚡

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green)](LICENSE)

An automated weather monitoring system that fetches real-time data and sends email alerts for extreme conditions.

## Features ✨
- **Scheduled Checks**: Runs every 5 minutes (configurable).
- **Email Alerts**: Notifies when temperature exceeds a threshold.
- **Extensible**: Easy to add alerts for rain, storms, etc.
- **API Integration**: Uses [WeatherAPI.com](https://www.weatherapi.com/).

## 📦 Installation
1. Clone the repo:
   ```bash
   git clone https://github.com/your-username/weather-tracker-bot.git
   cd weather-tracker-bot

2. Install dependencies:

   bash
   pip install -r requirements.txt
3. Configure:

4. Rename config.example.py to config.py.

5. Add your WeatherAPI key and email credentials.


🚀 Usage
bash
python src/scheduler.py
(Runs continuously; press Ctrl+C to stop.)

📂 Project Structure
src/
├── scheduler.py       # Main scheduler
├── weather_alert.py   # Email alert logic
└── weather_data.py    # API data fetcher


---

### **Bonus: `.gitignore`**
```gitignore
# Python
__pycache__/
*.pyc

# Config
config.py

# Environment
.env