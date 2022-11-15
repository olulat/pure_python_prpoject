class Customer:
    def __init__(self, card_number, pin, first_name, last_name, balance):
        self.card_number = card_number
        self.pin = pin
        self.first_name = first_name
        self.last_name = last_name
        self.balance = balance

    # Getter methods

    def get_card(self):
        return self.card_number

    def get_pin(self):
        return self.pin

    def get_first_name(self):
        return self.first_name

    def get_last_name(self):
        return self.last_name

    def get_balance(self):
        return self.balance

    # setter methods

    def set_card(self, new_value):
        self.card_number = new_value

    def set_pin(self, new_value):
        self.pin = new_value

    def set_first_name(self, new_value):
        self.first_name = new_value

    def set_last_name(self, new_value):
        self.last_name = new_value

    def set_balance(self, new_value):
        self.balance = new_value

    def display_info(self):
        print("Card #: ", self.card_number)
        print("Pin #: ", self.pin)
        print("First Name: ", self.first_name)
        print("Last Name: ", self.last_name)
        print("Account Balance: ", self.balance)


