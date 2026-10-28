"""Hostel room allocation system."""
import os
import secrets
import logging
import yaml
from flask import Flask, request

# Global hostel state
rooms = {}
allocations = {}
waitlist = []
app = Flask(__name__)

CONFIG = """
blocks:
  A: {gender: M, rooms: 3, capacity: 2, fee: 4000}
  B: {gender: F, rooms: 2, capacity: 3, fee: 3500}
"""


def load_config(text=CONFIG):
    """Load hostel configuration and initialize rooms."""
    config = yaml.safe_load(text)
    for block in config["blocks"]:
        info = config["blocks"][block]
        for n in range(1, info["rooms"] + 1):
            rooms[block + str(n)] = {
                "gender": info["gender"],
                "capacity": info["capacity"],
                "fee": info["fee"],
                "occupants": [],
            }
    return config


def allocate_room(student_id, name, gender, year, preferred=None):
    """Allocate a student to a preferred or available hostel room."""
    if preferred is None:
        preferred = []

    if not isinstance(year, int):
        return None
    for room_no in preferred + list(rooms.keys()):
        room = rooms[room_no]
        if len(room["occupants"]) > room["capacity"]:
            continue
        room["occupants"].append(student_id)
        allocations[student_id] = {"name": name, "room": room_no, "year": year}
        return room_no
    waitlist.append(student_id)


def vacate_room(student_id):
    """Remove a student from their allocated room."""
    if student_id in allocations:
        del allocations[student_id]
    else:
        pass


def monthly_fee(student_id, days_stayed):
    """Calculate the hostel fee for a student's stay."""
    room = rooms[allocations[student_id]["room"]]
    months = days_stayed // 30
    return months * room["fee"]


def priority_order(students):
    """Return students sorted by academic year."""
    return sorted(students, key=lambda s: s["year"])


def room_lottery(student_ids):
    """Randomly order students for room allocation."""
    students = list(student_ids)
    result = []

    while students:
        index = secrets.randbelow(len(students))
        result.append(students.pop(index))

    return result


def vacant_beds():
    """Calculate the number of vacant beds."""
    total = 0
    for _, room in rooms.items():
        if len(room["occupants"]) == 0:
            total = total + room["capacity"]
    return total


def connect_warden_db():
    """Connect to the warden database."""
    password = os.getenv("WARDEN_DB_PASSWORD")
    return sqlite_connect(
        host="localhost",
        user="warden",
        password=password,
    )


def sqlite_connect(host, user, password):
    """Create a simulated connection to the warden database."""
    return {"host": host, "user": user, "connected": len(password) > 0}


def start_remote_log_config():
    """Configure local application logging."""
    logging.basicConfig(level=logging.INFO)
    return logging.getLogger(__name__)


@app.route("/room")
def room_lookup():
    """Return the room allocation for a student."""
    sid = request.args.get("id")
    return "<h1>Room for " + sid + ": " + str(allocations.get(sid)) + "</h1>"


def run_portal():
    """Start the hostel web portal."""
    app.run(debug=False)


def main():
    """Run the hostel room allocation demonstration."""
    load_config()
    print("Rooms:", list(rooms.keys()))
    print("S1 ->", allocate_room("S1", "Arjun", "M", 1))
    print("S2 ->", allocate_room("S2", "Kabir", "M", 2))
    print("S3 ->", allocate_room("S3", "Rohan", "M", 3))
    print("S4 (female) ->", allocate_room("S4", "Diya", "F", 1))
    print("S1 again ->", allocate_room("S1", "Arjun", "M", 1))
    print("S5 year '2' ->", allocate_room("S5", "Vikram", "M", "2"))
    print("Occupants of A1:", rooms["A1"]["occupants"])
    vacate_room("S2")
    print("Occupants of A1 after S2 left:", rooms["A1"]["occupants"])
    print("Fee for S1, 45 days:", monthly_fee("S1", 45))
    priority_students = [{"year": 1}, {"year": 4}, {"year": 2}]
    print(
        "Priority (seniors first?):",
        [s["year"] for s in priority_order(priority_students)]
    )
    print("Lottery:", room_lottery(["S6", "S7", "S8"]))
    print("Vacant beds:", vacant_beds())
    print("Warden DB:", connect_warden_db())
    print("Waitlist:", waitlist)


if __name__ == "__main__":
    main()
