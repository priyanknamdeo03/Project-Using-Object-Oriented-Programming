# Parent Class
class User():
    def __init__(self, name: str, age: int, gender: str) -> None:
        self.name = name
        self.age = age
        self.gender = gender
    
    def show_user_details(self) -> None:
        print("Personal Details ...........\n")
        print("Name : ", self.name)
        print("Age : ", self.age)
        print("Gender : ", self.gender)

    # ----------------------------------------------------------------------

# Child Class
class Bank(User):
    def __init__(self, name: str, age: int, gender: str) -> None:
        super().__init__(name, age, gender)
        self.balance = 0

    def deposit(self, amount: int) -> None:
        self.amount = amount
        self.balance = self.balance + self.amount
        print("Acoount Balance Updated........ ")
    
    def withdraw(self, amount: int) -> None:
        self.amount = amount

        if(self.balance >= self.amount):
            self.balance = self.balance - self.amount
            print("Withdrawl Successful : ")
        else:
            print("\nInsufficient Balance In Account To Withdraw : ", self.balance)
            
    def view_balance(self) -> None:
        self.show_user_details()
        print("Current Account Balance : ", self.balance)
    
    def display_menu(self) -> None:
        while(True):
            print("\nWelcome To Bank {}. Enter Choice To Continue : ".format(self.name))
            print("\n1. View Account Balance And Details ")
            print("2. Deposit Balance ")
            print("3. Withdraw Balance ")
            print("4. EXIT\n")
            user_choice = int(input())

            if user_choice == 1:
                self.view_balance()
            elif user_choice == 2:  
                deposit_amount = int(input("Enter Amount To Deposit : "))
                self.deposit(deposit_amount)
            elif user_choice == 3:
                withdrawl_amount = int(input("Enter Amount To Withdraw : "))
                self.withdraw(withdrawl_amount)
            elif user_choice == 4:
                print("Thanks Visit Again ")
                exit()
            else:
                print("Invalid Choice Enter Again : ")
                continue

    # ----------------------------------------------------------------------


def main() -> None:
    priyank = Bank('Priyank', 16, 'M')
    priyank.display_menu()

    # ----------------------------------------------------------------------


if __name__ == '__main__':
    main()






