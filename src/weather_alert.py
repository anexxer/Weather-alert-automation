# weather_alert.py
import smtplib
from email.mime.text import MIMEText
from weather_data import get_weather  # Import the get_weather function

def send_email(subject, body):
    sender = "your_email@gmail.com"
    receiver = "receiver_email@gmail.com"
    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = sender
    msg["To"] = receiver

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(sender, "your_email_password")
            server.sendmail(sender, receiver, msg.as_string())
    except Exception as e:
        print(f"Error sending email: {e}")

def check_weather_and_alert(city, api_key, threshold=30):
    weather_data = get_weather(city, api_key)
    print(weather_data)
    if weather_data and weather_data['temperature'] > threshold:
        send_email("Weather Alert", f"Temperature in {city} has exceeded {threshold}°C! Current Temperature: {weather_data['temperature']}°C")
