import json

AVAIL_FILE = "data/availability.json"

def reserve_table(date, time):
    with open(AVAIL_FILE, "r") as file:
        availability = json.load(file)

    if availability[date][time] > 0:
        availability[date][time] -= 1
        with open(AVAIL_FILE, "w") as file:
            json.dump(availability, file, indent=4)
        return True
    return False
