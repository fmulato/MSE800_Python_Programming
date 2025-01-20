import json

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

    def save_json_file(self):
        data = {
            "customer_id": self._customer_id,
            "name": self._name,
            "email": self._email,
            "phone": self._phone
        }
        print(f"Data saved successfully")
        print(f"Here are the data:")
        with open("customer.json", "a") as file:
            json.dump(data, file)
            file.write('\n')