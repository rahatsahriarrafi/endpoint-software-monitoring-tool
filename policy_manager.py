import os

WHITELIST_FILE = "data/whitelist.txt"
BLACKLIST_FILE = "data/blacklist.txt"


# -----------------------------
# Load whitelist
# -----------------------------
def load_whitelist():
    if not os.path.exists(WHITELIST_FILE):
        return set()

    with open(WHITELIST_FILE, "r") as f:
        return set(line.strip().lower() for line in f if line.strip())


# -----------------------------
# Load blacklist
# -----------------------------
def load_blacklist():
    if not os.path.exists(BLACKLIST_FILE):
        return set()

    with open(BLACKLIST_FILE, "r") as f:
        return set(line.strip().lower() for line in f if line.strip())


# -----------------------------
# Save to whitelist
# -----------------------------
def add_to_whitelist(process_name):
    with open(WHITELIST_FILE, "a") as f:
        f.write(process_name + "\n")


# -----------------------------
# Save to blacklist
# -----------------------------
def add_to_blacklist(process_name):
    with open(BLACKLIST_FILE, "a") as f:
        f.write(process_name + "\n")


# -----------------------------
# Ask user decision
# -----------------------------
def ask_user_policy(process_name):

    print(f"\nNew process detected: {process_name}")

    print("Choose action:")
    print("1 → Allow (Whitelist)")
    print("2 → Block (Blacklist)")
    print("3 → Ignore")

    choice = input("Enter choice: ")

    if choice == "1":
        add_to_whitelist(process_name)
        print(f"[✔] Added to whitelist → {process_name}")

    elif choice == "2":
        add_to_blacklist(process_name)
        print(f"[🚫] Added to blacklist → {process_name}")

    else:
        print("[i] Ignored")


# -----------------------------
# Check policy
# -----------------------------
def check_process(process_name):

    whitelist = load_whitelist()
    blacklist = load_blacklist()

    process_name = process_name.lower()

    if process_name in blacklist:
        return "BLOCK"

    elif process_name in whitelist:
        return "ALLOW"

    else:
        return "UNKNOWN"