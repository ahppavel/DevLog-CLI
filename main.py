import json
import os
from datetime import datetime


def save_data(sessions):
    with open("data.json", "w") as f:
        json.dump(sessions, f, indent=2)

def load_data():
    if os.path.exists("data.json"):
        with open("data.json", "r") as f:
            return json.load(f)
    return []

def log_session(subject, minutes):
    sessions = load_data()
    session = {
        "subject": subject,
        "minutes": minutes,
        "date": datetime.now().strftime("%Y-%m-%d"),
        "time": datetime.now().strftime("%H:%M")
    }
    
    sessions.append(session)
    save_data(sessions)
    print("Logged:", subject, "-", minutes, "mins")
    
def view_sessions():
    sessions = load_data()
    if len(sessions) == 0:
        print("No sessions yet!")
        return
    print("\nYour Study Sessions")
    for session in sessions:
        print(session["date"], "|", session["time"], "|", session["subject"], "-", session["minutes"], "mins")


while True:
    print("\nWhat do you want to do?")
    print("1 - Log a session")
    print("2 - View all sessions")
    print("3 - Quit")

    choice = input("Enter choice: ")

    if choice == "1":
        while True:
            try:
                count = int(input("How many subjects did you study?\n -"))
                if count <= 0:
                    print("Please enter a number greater than 0!")
                    continue
                break
            except ValueError:
                print("Invalid! Please enter a number only!")

        for i in range(count):
            print(f"\nSubject {i + 1}:")
            subject = input("Subject name: ")
            while True:
                try:
                    minutes = int(input("Minutes: "))
                    if minutes <= 0:
                        print("Please enter a number greater than 0!")
                        continue
                    break
                except ValueError:
                    print("Invalid! Please enter a number only")
            log_session(subject, minutes)

    elif choice == "2":
        view_sessions()

    elif choice == "3":
        print("Goodbye.Keep studying")
        break

    else:
        print("Please enter 1, 2 or 3 only!")