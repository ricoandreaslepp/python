from datetime import datetime as dt
from colors import TerminalColors
import hashlib
import stdiomask
import glob
import os

tc = TerminalColors()

class Bank:

    users_file = open("users.txt", "r+")
    users = list(map(str.strip, users_file.readlines()))

    def __init__(self):
        pass

    def validChoice(self, validChoices, choice):
        return choice in validChoices

    def save_data(self, balance, history, user_file_name):
        with open(user_file_name, "r+", encoding="UTF-8") as file:
            contents = file.readlines()
            contents[1] = str(balance) + "\n"
            contents += history
            file.truncate(0)
            file.seek(0)
            file.write("".join(contents))

        return None

    def welcomeScreen(self):
        print(f"current time: {dt.now().isoformat(' ')[:19]}")
        choice = input("do you have an account (y/n): ").strip().lower()

        while not self.validChoice(["y", "n"], choice):
            choice = input("incorrect input, try again (y/n): ").strip()

        if choice == "y":
            
            while True:

                # ADD SALT
                salt = os.urandom(32)
                usr = hashlib.sha256(input("username: ").encode()).hexdigest()
                pwd = hashlib.sha256(stdiomask.getpass(prompt="password: ").encode()).hexdigest()

                if usr in self.users:

                    with open(f"ID_{str(self.users.index(usr)+1)}.txt") as file:

                        user_data = list(map(str.strip, file.readlines()))

                        if pwd == user_data[0]:
                            print("successfully logged in!")
                            self.choiceScreen(f"ID_{str(self.users.index(usr)+1)}.txt")
                            file.close()
                            return None
                    
                print("wrong username or password. try again.")

        elif choice == "n":
            print("enter your credentials to sign up")
            while True:

                # ADD SALT
                salt = os.urandom(32) # 32 byte salt
                usr = hashlib.sha256(input("username: ").encode()).hexdigest()
                pwd = hashlib.sha256(f"{stdiomask.getpass(prompt='password: ').encode()}{salt}").hexdigest()

                if usr not in self.users:
                    
                    list_of_files = glob.glob('ID_*.txt')
                    last_id = int(max(list_of_files, key=os.path.getctime)[3])+1 # potential exploit here
                    self.users_file.write("\n" + usr)
                    with open(f"ID_{str(last_id)}.txt", "w") as user_file:
                        user_file.write(pwd + "\n0")

                    print("account successfully created!") # xd
                    self.choiceScreen(f"ID_{str(last_id)}.txt")
                    return None

                print("username already taken. try again.")
            
        return None

    def choiceScreen(self, user_file_name):
        # read data from user file and close it
        user_file = open(user_file_name)
        user_data = list(map(str.strip, user_file.readlines()))
        balance = int(user_data[1])
        user_file.close()

        choices = ["withdraw", "deposit", "display", "exit"]
        history = []
        
        print("###------------------------###")
        print(f"|  {' '.join(choices[:3])}  |")
        print(f"|{12*' '}{choices[3]}{12*' '}|")
        print("###------------------------###\n")

        choice = None
        while choice != "exit":
            choice = input("what would you like to do: ").strip().lower()

            while not self.validChoice(choices, choice):
                choice = input("incorrect choice, try again: ").strip().lower()

            if choice == "withdraw":
                wdraw = input("Enter the amount to withdraw: ")

                while type(wdraw) != int:
                    try:
                        wdraw = int(wdraw)
                    except ValueError:
                        wdraw = input("Please enter a number: ")

                history.append(f"\nwithdrew {str(wdraw)} at {dt.now().isoformat(' ')[:19]}")
                balance = balance - wdraw

            elif choice == "deposit":
                depo = input("Enter the amount to deposit: ")

                while type(depo) != int:
                    try:
                        depo = int(depo)
                    except ValueError:
                        depo = input("Please enter a number: ")

                history.append(f"\ndeposited {str(depo)} at {dt.now().isoformat(' ')[:19]}")
                balance = balance + depo

            elif choice == "exit":
                print("bye")
                # edit user file before exiting
                save_data(balance, history, user_file_name)
                return None
       
            print(f"Current balance: {str(balance)} €")

        return None

    def run(self):
        try:
            self.welcomeScreen()
        except KeyboardInterrupt:  
            pass
        except EOFError:
            pass
                 
        print("\nbye") 
        self.users_file.close()


if __name__=='__main__':
    b = Bank()
    b.run()
