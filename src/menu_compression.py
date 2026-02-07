import json

def load_menu():
    with open("data/menu.json", "r") as file:
        return json.load(file)

def display_menu():
    menu = load_menu()
    response = "📖 Menu:\n"
    for code, item in menu.items():
        response += f"{code}: {item['name']} - ₹{item['price']}\n"
    return response
