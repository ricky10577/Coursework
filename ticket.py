print("Welcome to our Railway Online Ticket Shop!")

def quantity_prompt():
    while True:
        try:
            quantity = int(input("\nHow many tickets would you like to purchase? "))
            if quantity > 0:
                return quantity
            print("Invalid input. Please enter a whole positive number.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def ticket_purchase():
    locations = {
            '1': ("London", 10.15),
            '2': ("Birmingham", 21.40),
            '3': ("Manchester", 22.50)
        }
    
    while True:
        print("\nWhere are you travelling to?\n ")
        for key, (location, price) in locations.items():
            print(f"{key} - {location} (£{price:.2f})")
        choice = input("\nPlease enter your choice (1-3): ")
        if choice in locations:
            return choice, locations[choice]
        print("Invalid choice. Please try again.")