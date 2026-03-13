import json
import os

DB_FILE = "data.db"

# Load existing database or create a new one
if os.path.exists(DB_FILE):
    with open(DB_FILE) as f:
        db = json.load(f)
else:
    db = {}

while True:
    try:
        parts = input().strip().split()
    except EOFError:
        break

    if not parts:
        continue

    cmd = parts[0]

    if cmd == "SET":
        key = parts[1]
        value = parts[2]
        db[key] = value
        with open(DB_FILE, "w") as f:
            json.dump(db, f)
        print("OK")

    elif cmd == "GET":
        key = parts[1]
        print(db.get(key, "NULL"))

    elif cmd == "DELETE":
        key = parts[1]
        if key in db:
            del db[key]
            with open(DB_FILE, "w") as f:
                json.dump(db, f)
            print("OK")
        else:
            print("NULL")

    elif cmd == "EXIT":
        break
