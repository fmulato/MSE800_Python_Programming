class Customer:
    def __init__(self, customer_id, name="", email="", phone=""):
        self._customer_id = customer_id
        self._name = name
        self._email = email
        self._phone = phone

    def create_user(self):
        self._name = input("Input your full name: ")
        self._email = input("Input your email: ")
        self._phone = input("Input your phone number: ")

    def display_info(self):
        print(f"ID: {self._customer_id}")
        print(f"Name: {self._name}")
        print(f"Email: {self._email}")
        print(f"Phone: {self._phone}")


if __name__ == '__main__':
    try:
        customer_id = int(input("Input your customer ID: "))
        cst = Customer(customer_id)
        cst.create_user()
        cst.display_info()
    except ValueError:
        print("Invalid customer ID. Please enter a number.")
