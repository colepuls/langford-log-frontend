# File to track time spent on project for pay.

import json
import os
from datetime import datetime

LOG_FILE = "log.json"

def load_log():
    if not os.path.exists(LOG_FILE):
        return {}
    with open(LOG_FILE, "r") as file:
        return json.load(file)

def save_log(data):
    with open(LOG_FILE, "w") as file:
        json.dump(data, file, indent=4)

def clock_in(name):
    now = datetime.now().isoformat()
    log = load_log()
    log.setdefault(name, []).append({"action": "IN", "time": now})
    save_log(log)
    print(f"{name} clocked IN at {now}")

def clock_out(name):
    now = datetime.now().isoformat()
    log = load_log()
    log.setdefault(name, []).append({"action": "OUT", "time": now})
    save_log(log)
    print(f"{name} clocked OUT at {now}")

def show_status(name):
    log = load_log()
    entries = log.get(name)
    if not entries:
        print(f"No records for {name}.")
        return
    last = entries[-1]
    print(f"{name}'s last action: {last['action']} at {last['time']}")

def main():
    while True:
        print("\nClock In/Out System")
        print("1. Clock In")
        print("2. Clock Out")
        print("3. Show Last Status")
        print("4. Exit")
        choice = input("Select an option: ").strip()

        if choice not in {"1", "2", "3", "4"}:
            print("Invalid option.")
            continue

        if choice == "4":
            print("Exiting...")
            break

        name = input("Enter your name: ").strip()
        if choice == "1":
            clock_in(name)
        elif choice == "2":
            clock_out(name)
        elif choice == "3":
            show_status(name)

if __name__ == "__main__":
    main()