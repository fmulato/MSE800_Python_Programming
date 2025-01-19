import customer

def run_app():
    try:
        customer_id = int(input("Input your customer ID: "))
        cust = customer.Customer(customer_id)
        cust.create_user()
        cust.save_json_file()
        cust.display_info()
        print("Thank you for using our system.")
    except ValueError:
        print("Invalid customer ID. Please enter a number.")

if __name__ == '__main__':
    run_app()