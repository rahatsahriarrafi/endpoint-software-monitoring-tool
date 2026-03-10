import time
from scanner import scan_system
from policy_manager import check_process, ask_user_policy
from notifier import send_alert, send_warning
from config import SCAN_INTERVAL


def start_monitor():

    print("\n===== Endpoint Software Monitoring Tool =====\n")
    print("Monitoring system processes...\n")

    while True:

        data = scan_system()

        processes = data["processes"]

        for process in processes:

            name = process["name"]
            pid = process["pid"]

            if not name:
                continue

            status = check_process(name)

            if status == "ALLOW":
                continue

            elif status == "BLOCK":
                send_alert(f"Blacklisted software detected: {name} (PID {pid})")

            elif status == "UNKNOWN":

                send_warning(f"Unknown software detected: {name} (PID {pid})")

                # ask user decision
                ask_user_policy(name)

        time.sleep(SCAN_INTERVAL)


if __name__ == "__main__":
    start_monitor()