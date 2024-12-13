print("Welcome to our Railway Online Ticket Shop!")
#funtion for quantity input
def quantity_prompt():
    while True: 
        try:
            quantity = int(input("\nHow many tickets would you like to purchase? "))
            if quantity > 0:
                return quantity
            print("Invalid input. Please enter a whole positive number.")
        except ValueError:
            print("Invalid input. Please enter a number.")

#funcion for ticket options display and retrieval of user choice
def ticket_purchase():
    locations = { #set wit locations and prices
            '1': ("London", 10.15),
            '2': ("Birmingham", 21.40),
            '3': ("Manchester", 22.50)
        }
    
    while True:#loop to capture user's input
        print("\nWhere are you travelling to?\n ")
        for key, (location, price) in locations.items(): # iteration to print options to user
            print(f"{key} - {location} (£{price:.2f})")
        choice = input("\nPlease enter your choice (1-3): ")
        if choice in locations:#if statement to check validity of input
            return choice, locations[choice]
        print("Invalid choice. Please try again.")

#main function of the program
def main():
    name = input("\nPlease enter lead passenger name: ")

    choice, (location, price) = ticket_purchase()
    quantity = quantity_prompt()
    cost = price * quantity 
    print(f"\n{name}, \nYou have chosen {quantity} ticket(s) to {location}.")
    print(f"\nTotal cost: {quantity} x £{price:.2f} = £{cost:.2f}")
    #summary of purchase shown to user
    
    while True:#loop to create receipt for user
        receipt_prompt = input("\nWould you like to print your receipt? (yes/no) ").lower()
    
        if receipt_prompt == 'yes': 
            receipt_name = name + '.txt'   #variable to store receipt name
            receipt = open(receipt_name, "w") # creation of receipt file
            receipt.write(f"Receipt of ticket purchase\n") # receipt content
            receipt.write(f"\nName of customer: {name}")
            receipt.write(f"\nDestination: {location} ")
            receipt.write(f"\nQuantity: {quantity} \n")
            receipt.write(f"\nTotal Cost: {quantity} x (£{price:.2f}) = £{cost:.2f}\n")
            receipt.write(f"\nThank you for your custom!")
            receipt.close() # closing receipt file
            print("\nYour receipt has been generated!\nThank you for your custom!") #thank you message
            break 

        elif receipt_prompt == 'no':    
            print("Thank you for your custom!")    
            break

        else:    
            print("Invalid choice, please try again")        
        #options if uses does not want receipt or mistype answer

if __name__ == "__main__":
    main()