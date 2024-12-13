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

def main():
    name = input("\nPlease enter lead passenger name: ")

    choice, (location, price) = ticket_purchase()
    quantity = quantity_prompt()
    cost = price * quantity 
    print(f"\n{name}, \nYou have chosen {quantity} ticket(s) to {location}.")
    print(f"\nTotal cost: {quantity} x £{price:.2f} = £{cost:.2f}")
    
    while True:
        receipt_prompt = input("\nWould you like to print your receipt? (yes/no) ").lower()
    
        if receipt_prompt == 'yes': 
            receipt_name = name + '.txt'   
            receipt = open(receipt_name, "w")
            receipt.write(f"Receipt of ticket purchase\n")
            receipt.write(f"\nName of customer: {name}")
            receipt.write(f"\nDestination: {location} ")
            receipt.write(f"\nQuantity: {quantity} \n")
            receipt.write(f"\nTotal Cost: {quantity} x (£{price:.2f}) = £{cost:.2f}\n")
            receipt.write(f"\nThank you for your custom!")
            receipt.close()
            print("\nYour receipt has been generated!\nThank you for your custom!")
            break 

        elif receipt_prompt == 'no':    
            print("Thank you for your custom!")    
            break

        else:    
            print("Invalid choice, please try again")        

if __name__ == "__main__":
    main()