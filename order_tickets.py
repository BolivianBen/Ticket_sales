#A user should be shown the number of tickets left remaing
#users should feel they have a personalized experiance
#Users should have error reported in a friendly, easy to read manner
# users should determine how many tickets they want and the total price
# users should see the final before they confirm to ensure accurate amount
#users should be told they can't buy more once tickets are out
# users should be able to purchase with credit cards and bitcoin

#Additionally, the program should not be able to sell more tickets than are currently available for sale



TICKET_PRICE = 10
SERVICE_CHARGE = 2

tickets_remaining = 100


def calculate_price(num_of_ticket):
    return (num_of_ticket * TICKET_PRICE) + SERVICE_CHARGE
    
    


# Run this code continuously until we run out of tickets
while tickets_remaining >= 1:
    print("There are {} tickets remaining.".format(tickets_remaining))
    # Gather the user's name and assign it to a new variable
    name = input("What is your name?  ")
    num_tickets = input("How many tickets would you like, {}?  ".format(name))
    #Expect and catch errors
    try:
        num_tickets = int(num_tickets)
        if num_tickets > tickets_remaining:
            raise ValueError("There are only {} tickets remaining".format(tickets_remaining))
    except ValueError as err:
        print("Oh no, we have an issue, {}. please try again".format(err))
    else:
        amount_due = calculate_price(num_tickets)
        print("The total due is ${}".format(amount_due))
        should_proceed = input("Do you want to proceed?  Y/N  ")
        if should_proceed.lower() == "y":
            # TODO: Gather credit card information and process it.
            print("SOLD!")
            tickets_remaining -= num_tickets
        else:
            print("Thank you anyways, {}!".format(name))
# Notify user that the tickets are sold out    
print("Sorry the tickets are all sold out!!! :(")


            

