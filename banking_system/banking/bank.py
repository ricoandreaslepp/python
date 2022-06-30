from datetime import datetime as dt
import hashlib
import stdiomask
import glob
import os

users_file = open("users.txt", "r+")
users = list(map(str.strip, users_file.readlines()))

def validChoice(validChoices, choice):

    if choice in validChoices:
        return True

    return False

def save_data(balance, history, user_file_name):
    with open(user_file_name, "r+", encoding="UTF-8") as file:
        contents = file.readlines()
        contents[1] = str(balance) + "\n"
        contents += history
        file.truncate(0)
        file.seek(0)
        file.write("".join(contents))

    return None

def welcomeScreen():
    print("current time:", dt.now().isoformat(' ')[:19])
    choice = input("do you have an account (y/n): ").strip().lower()

    while not validChoice(["y", "n"], choice):
        choice = input("incorrect input, try again (y/n): ").strip()

    if choice == "y":
        
        while True:
            usr = hashlib.sha256(input("username: ").encode()).hexdigest()
            pwd = hashlib.sha256(stdiomask.getpass(prompt="password: ").encode()).hexdigest()

            if usr in users:

                with open("ID_" + str(users.index(usr)+1) + ".txt") as file:

                    user_data = list(map(str.strip, file.readlines()))

                    if pwd == user_data[0]:
                        print("successfully logged in!")
                        # use " ".join() instead for concatenating
                        choiceScreen("ID_" + str(users.index(usr)+1) + ".txt")
                        file.close()
                        return None
                
            print("wrong username or password. try again.")

    elif choice == "n":
        print("enter your credentials to sign up")
        while True:
            usr = hashlib.sha256(input("username: ").encode()).hexdigest()
            pwd = hashlib.sha256(stdiomask.getpass(prompt="password: ").encode()).hexdigest()

            if usr not in users:
                
                list_of_files = glob.glob('ID_*.txt')
                last_id = int(max(list_of_files, key=os.path.getctime)[3])+1 # potential exploit here
                users_file.write("\n" + usr)
                with open("ID_" + str(last_id) + ".txt", "w") as user_file:
                    user_file.write(pwd + "\n0")

                print("account successfully created!") # xd
                choiceScreen("ID_" + str(last_id) + ".txt")
                return None

            print("username already taken. try again.")
        
    return None

def choiceScreen(user_file_name):
    # read data from user file and close it
    user_file = open(user_file_name)
    user_data = list(map(str.strip, user_file.readlines()))
    balance = int(user_data[1])
    user_file.close()

    choices = ["withdraw", "deposit", "display", "exit"]
    history = []
    
    # could improve the formatting for sure
    print("###------------------------###")
    print("|  " + " ".join(choices[:3]) + "  |")
    print("|" + 12*" " + choices[3] + 12*" " + "|")
    print("###------------------------###\n")

    choice = None
    while choice != "exit":
        choice = input("what would you like to do: ").strip().lower()

        while not validChoice(choices, choice):
            choice = input("incorrect choice, try again: ").strip().lower()

        if choice == "withdraw":
            wdraw = input("Enter the amount to withdraw: ")

            while type(wdraw) != int:
                try:
                    wdraw = int(wdraw)
                except ValueError:
                    wdraw = input("Please enter a number: ")

            history.append("\nwithdrew " + str(wdraw) + " at " + dt.now().isoformat(' ')[:19])
            balance = balance - wdraw

        elif choice == "deposit":
            depo = input("Enter the amount to deposit: ")

            while type(depo) != int:
                try:
                    depo = int(depo)
                except ValueError:
                    depo = input("Please enter a number: ")

            history.append("\ndeposited " + str(depo) + " at " + dt.now().isoformat(' ')[:19])
            balance = balance + depo

        elif choice == "exit":
            print("bye")
            # edit user file before exiting
            save_data(balance, history, user_file_name)
            return None
   
        print("Current balance: " + str(balance) + " €")

    return None

def run():
    welcomeScreen()
    users_file.close()
    
try:
    run()
except KeyboardInterrupt:
    print("\nbye")
