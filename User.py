# your User class goes here
class User: 

    def __init__(self, email_address, driver_licence_number):
        self.name = email_address
        self.driver_licence_number = driver_licence_number

    def new_user(self):
        print(f"Hello {self.name}")

    def show_licence_number(self):
        print(f"Here is your Dirver Licence Number: {self.driver_licence_number}")



peach = User("peach@nintendo.com", "DTF987654")
# Mario = User("mariorules@nintendo.com", "DTF963852")
# Peach.new_user()
peach.show_licence_number()
# Mario.new_user()
# Mario.show_licence_number("DTF963852")
