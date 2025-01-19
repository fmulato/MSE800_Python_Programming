class Customer:
    def __init__(self, customer_id, name="", email="", phone=""): #valores default para nao dar erro caso seja chamado sem parametros
        self._customer_id = customer_id  # Encapsulation using _
        self._name = name
        self._email = email
        self._phone = phone

    def create_user(self): #nome corrigido
        self._name = input("Input your full name: ")
        self._email = input("Input your email: ")
        self._phone = input("Input your phone number: ")

    def display_info(self): #metodo para exibir as informações
        print(f"ID: {self._customer_id}")
        print(f"Name: {self._name}")
        print(f"Email: {self._email}")
        print(f"Phone: {self._phone}")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    try:
        customer_id = int(input("Input your customer ID: ")) #recebe o id do usuário
        cst = Customer(customer_id) #instancia o objeto com o id
        cst.create_user() #chama a função para receber os outros dados
        cst.display_info() #chama a função para exibir os dados
    except ValueError:
        print("Invalid customer ID. Please enter a number.")
