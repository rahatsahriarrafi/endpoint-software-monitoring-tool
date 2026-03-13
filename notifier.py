import datetime
import os
from config import LOG_FILE

# ---------------------------------
# Write alert to log file
# ---------------------------------
def log_event(message):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_message = f"[{timestamp}] {message}\n"

    # Ensure logs directory exists
    os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)

    with open(LOG_FILE, "a") as log:
        log.write(log_message)


# ---------------------------------
# Console alert
# ---------------------------------
def console_alert(message):
    print("\n🚨 SECURITY ALERT")
    print(message)
    print()


# ---------------------------------
# Alert handler
# ---------------------------------
def send_alert(message):
    console_alert(message)
    log_event(message)


# ---------------------------------
# Warning handler
# ---------------------------------
def send_warning(message):
    print("\n⚠ WARNING")
    print(message)
    print()

    log_event("WARNING: " + message)


# ---------------------------------
# Info messages (real-time terminal output)
# ---------------------------------
def send_info(message):
    timestamp = datetime.datetime.now().strftime("%H:%M:%S")

    print(f"[{timestamp}] INFO → {message}")
    log_event("INFO: " + message)