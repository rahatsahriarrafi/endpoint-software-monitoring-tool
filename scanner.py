import psutil

# ---------------------------------
# Get Running Processes
# ---------------------------------
def get_running_processes():
    """
    Returns a list of running processes with basic information.
    """

    processes = []

    for process in psutil.process_iter(['pid', 'name', 'username']):
        try:
            process_info = {
                "pid": process.info['pid'],
                "name": process.info['name'],
                "user": process.info['username']
            }

            processes.append(process_info)

        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass

    return processes


# ---------------------------------
# Get Running Services (Linux)
# ---------------------------------
def get_running_services():
    """
    Detect running services using systemctl (Linux only).
    """

    services = []

    try:
        import subprocess

        result = subprocess.run(
            ["systemctl", "list-units", "--type=service", "--state=running"],
            capture_output=True,
            text=True
        )

        lines = result.stdout.split("\n")

        for line in lines:
            if ".service" in line:
                service_name = line.split()[0]
                services.append(service_name)

    except Exception:
        pass

    return services


# ---------------------------------
# Full System Scan
# ---------------------------------
def scan_system():
    """
    Performs a full system scan and returns processes and services.
    """

    processes = get_running_processes()
    services = get_running_services()

    return {
        "processes": processes,
        "services": services
    }


# ---------------------------------
# Test Mode (run scanner directly)
# ---------------------------------
if __name__ == "__main__":

    data = scan_system()

    print("\n===== Running Processes =====\n")

    for p in data["processes"][:20]:
        print(f"{p['pid']} | {p['name']} | {p['user']}")

    print("\n===== Running Services =====\n")

    for s in data["services"][:20]:
        print(s)