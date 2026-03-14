import json
import os

DB_FILE = "data.db"


def load_database(file_path):
    """Load the database from file, or create empty dict if file is missing or invalid."""
    if os.path.exists(file_path):
        try:
            with open(file_path, "r") as f:
                return json.load(f)
        except json.JSONDecodeError:
            return {}
    else:
        with open(file_path, "w") as f:
            json.dump({}, f)
        return {}


def save_database(file_path, db):
    """Save the database to file."""
    with open(file_path, "w") as f:
        json.dump(db, f)


def handle_set(db, parts):
    """Handle SET command."""
    if len(parts) < 3:
        return  # Invalid command
    key, value = parts[1], parts[2]
    db[key] = value
    save_database(DB_FILE, db)
    print("OK")


def handle_get(db, parts):
    """Handle GET command."""
    if len(parts) < 2:
        print("")  # Missing key
        return
    key = parts[1]
    print(db.get(key, ""))  

def handle_delete(db, parts):
    """Handle DELETE command."""
    if len(parts) < 2:
        return
    key = parts[1]
    if key in db:
        del db[key]
        save_database(DB_FILE, db)
        print("OK")
    else:
        print("")  


def main():
    db = load_database(DB_FILE)

    while True:
        try:
            parts = input().strip().split()
        except EOFError:
            break  # End of input

        if not parts:
            continue

        cmd = parts[0].upper()

        if cmd == "SET":
            handle_set(db, parts)
        elif cmd == "GET":
            handle_get(db, parts)
        elif cmd == "DELETE":
            handle_delete(db, parts)
        elif cmd == "EXIT":
            break
        else:
            continue  # Ignore unknown commands


if __name__ == "__main__":
    main()
