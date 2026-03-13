# ---------------------------------
# Scan Configuration
# ---------------------------------

# Time interval between scans (seconds)
SCAN_INTERVAL = 10


# ---------------------------------
# File Paths
# ---------------------------------

WHITELIST_FILE = "data/whitelist.txt"
BLACKLIST_FILE = "data/blacklist.txt"

LOG_FILE = "logs/monitor.log"


# ---------------------------------
# Notification Settings
# ---------------------------------

EMAIL_ALERTS = False
TELEGRAM_ALERTS = False


# ---------------------------------
# Email Configuration (User Input)
# ---------------------------------

EMAIL_SENDER = None
EMAIL_PASSWORD = None
EMAIL_RECEIVER = None


# ---------------------------------
# Telegram Configuration (User Input)
# ---------------------------------

TELEGRAM_BOT_TOKEN = None
TELEGRAM_CHAT_ID = None


# ---------------------------------
# Setup Notifications (Interactive)
# ---------------------------------

def setup_notifications():
    global EMAIL_ALERTS
    global TELEGRAM_ALERTS
    global EMAIL_SENDER
    global EMAIL_PASSWORD
    global EMAIL_RECEIVER
    global TELEGRAM_BOT_TOKEN
    global TELEGRAM_CHAT_ID

    print("\n===== Notification Setup =====")

    # Email alerts
    email_choice = input("Enable Email Alerts? (y/n): ").strip().lower()

    if email_choice == "y":
        EMAIL_ALERTS = True
        EMAIL_SENDER = input("Enter sender email: ")
        EMAIL_PASSWORD = input("Enter email app password: ")
        EMAIL_RECEIVER = input("Enter receiver email: ")

    # Telegram alerts
    telegram_choice = input("Enable Telegram Alerts? (y/n): ").strip().lower()

    if telegram_choice == "y":
        TELEGRAM_ALERTS = True
        TELEGRAM_BOT_TOKEN = input("Enter Telegram Bot Token: ")
        TELEGRAM_CHAT_ID = input("Enter Telegram Chat ID: ")

    print("\nNotification setup complete.\n")