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
