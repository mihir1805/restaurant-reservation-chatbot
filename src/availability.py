import json

def load_availability():
    with open("data/availability.json", "r") as file:
        return json.load(file)

def check_availability(date, time):
    availability = load_availability()
    try:
        return availability[date][time]
    except KeyError:
        return None
