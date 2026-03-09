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


log_session("Python", 45)
log_session("Mathematics", 60)
log_session("GRC", 30)
view_sessions()