import datetime
from config import LOG_FILE


# ---------------------------------
# Write alert to log file
# ---------------------------------
def log_event(message):

    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    log_message = f"[{timestamp}] {message}\n"

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

    # print alert
    console_alert(message)

    # log alert
    log_event(message)


# ---------------------------------
# Warning handler
# ---------------------------------
def send_warning(message):

    print("\n⚠ WARNING")
    print(message)
    print()

    log_event("WARNING: " + message)