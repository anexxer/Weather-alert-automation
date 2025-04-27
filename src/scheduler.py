# scheduler.py
import schedule
import time
from weather_alert import check_weather_and_alert

def job():
    city = "London"
    api_key = "YOUR API KEY" 
    print(f"\n[{time.ctime()}] Running weather check for {city}...")
    check_weather_and_alert(city, api_key)
    print(f"[{time.ctime()}] Weather check completed")

# Schedule the job to run every 5 minutes for testing
schedule.every(5).minutes.do(job)

# Run the job immediately first time for testing
print("Starting weather monitoring system...")
job()

# Main loop to keep the scheduler running
print("Scheduler running (Ctrl+C to exit)...")
try:
    while True:
        schedule.run_pending()
        time.sleep(1)
except KeyboardInterrupt:
    print("\nScheduler stopped by user")
