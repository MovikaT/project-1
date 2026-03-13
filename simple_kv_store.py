import json
import os

DB_FILE = "data.db"

# Load database if exists, else create empty file
db = {}
if os.path.exists(DB_FILE):
    try:
        with open(DB_FILE) as f:
            db = json.load(f)
    except json.JSONDecodeError:
        db = {}
else:
    with open(DB_FILE, "w") as f:
        json.dump(db, f)

# Main loop: read commands from stdin (no prompts)
while True:
    try:
        parts = input().strip().split()
    except EOFError:
        break  # End of input

    if not parts:
        continue

    cmd = parts[0]

    if cmd == "SET":
        if len(parts) < 3:
            continue  # Skip invalid SET
        key, value = parts[1], parts[2]
        db[key] = value
        with open(DB_FILE, "w") as f:
            json.dump(db, f)
        print("OK")

    elif cmd == "GET":
        if len(parts) < 2:
            print("")  # No key provided
            continue
        key = parts[1]
        print(db.get(key, ""))  # Return empty string if key missing

    elif cmd == "DELETE":
        if len(parts) < 2:
            continue
        key = parts[1]
        if key in db:
            del db[key]
            with open(DB_FILE, "w") as f:
                json.dump(db, f)
            print("OK")
        else:
            print("")  # Return empty string if key missing

    elif cmd == "EXIT":
        break
