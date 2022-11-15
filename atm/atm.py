from customer import Customer


def home_page():
    print("Please select an action")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Balance")
    print("4. Exit")


def deposit(customer):
    try:
        deposit_amount = float(input("What is the amount you like to deposit: "))
        customer.set_balance(customer.get_balance() + deposit_amount)
        print("Thank you for your deposit. Your new balance is: ", str(customer.get_balance()))
    except:
        print("Invalid input")


def withdraw(customer):
    try:
        withdraw_amount = float(input("What is the amount you like to withdraw: "))

        if customer.get_balance() > withdraw_amount:
            customer.set_balance(customer.get_balance() - withdraw_amount)
            print(f" Your new balance is: {str(customer.get_balance())}")

        else:
            print(f"Your dont have up to {withdraw_amount} in your account,Please check your balance ")

    except:
        print("Invalid input")


def check_balance(customer):
    print(f" Your balance is: {customer.get_balance()}")


if __name__ == "__main__":
    current_customer = Customer("", "", "", "", "")

list_of_customer = [
    Customer("234567890123", 8899, "Lateef", "Olamilekan", 550),
    Customer("2345678908899", 2345, "John", "Smith", 50.80),
    Customer("2345678902345", 1234, "Paul", "James", 90.82)
]

customer_card_number = ""

# Check for card
while True:
    try:
        customer_card_number = input("Please insert your card: ")
        card_match = [card_holder for card_holder in list_of_customer if
                      card_holder.card_number == customer_card_number]
        if len(card_match) > 0:
            current_customer = card_match[0]

            break
        else:
            print("Card number not recognized. Please check the number")


    except:
        print("Card number not recognized. Please check the number")

# Check for Pin
while True:
    try:
        customer_pin = int(input("Please enter your pin: ").strip())
        if (current_customer.get_pin() == customer_pin):
            break
        else:
            print("Invalid PIN. Please try again")

    except:
        print("Invalid PIN. Please try again")

print(f"Welcome {current_customer.get_first_name()}")

option = 0

while True:
    home_page()
    try:
        option = int(input())
    except:
        print("Invalid input")

    if option == 1:
        deposit(current_customer)

    elif option == 2:
        withdraw(current_customer)
    elif option == 3:
        check_balance(current_customer)
    elif option == 4:
        break
    else:
        option = 0

print("Thank you have a wonderful day")
