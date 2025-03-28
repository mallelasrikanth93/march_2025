# mode = 'r' --> read operations
# file = open("demo.txt",mode = 'r')
# read_data = file.read()
# print(read_data)
# file.close()


# file = open("demo.txt",mode = 'r')
# read_data = file.readline()
# print(read_data)
# file.close()

# file = open("demo.txt",mode = 'r')
# read_data = file.readlines()
# print(read_data)
# file.close()


#mode = 'a' --.> append operations
# file = open("demo.txt",mode = 'a')
# write_data = file.write("\nthis is write operation perfoming using mode = 'a'")
# file.close()

# file = open("demo123.txt",mode = 'a')
# file.close()

# mode = 'w'--> write operations
# file= open("demo.txt", mode = 'w')
# write_data = file.write("welcome to pythonlife")
# file.close()


# voter_id = ['123\n','456\n','789\n','1234\n','1245']
# file= open("demo.txt", mode = 'w')
# write_data = file.writelines(voter_id)
# file.close()

# file = open("strings.txt",mode = 'w')
# write_data = file.write("welcome to pythonlife")
# file.close()



# mode = 'w+'
# file = open("sample.txt",mode = 'w+')
# write_data = file.write("pythonlife")
# print(file.tell())
# file.seek(0)
# read_data = file.read()
# print(read_data)
# file.close()


# file = open("C:\\Users\\tarak\\Desktop\\python12345.txt",mode='w')
# file.close()


# file --> delete python programming use
# file --> rename python programming 
# import os
# old_name = "sample1.txt"
# new_name = "vasu123.txt"
# os.rename(old_name,new_name)

#############################
# import csv

# csv_file = "students.csv"
# data = [
#     ["ID","NAME","GRADE"],
#     ["123","PAVAN","A+"],
#     ["12345","PAVAN1","A"],
#     ["123456","PAVAN123","A"],
# ]
# file = open(csv_file,mode='w',newline="")
# write = csv.writer(file)
# write.writerows(data)
# file.close()


#hint--> pypdf --> 
# gtts

#install --> pip install packagename
# import pypdf
# import gtts
# import math
# import os
# import csv
# import tkinter


# venv create
# venv activate
# 3rd party modules pip install packagename
#import modules




balance = 0
transaction_file = "transactions.txt"

def display_menu():
    print("\nATM Menu:")
    print("1. Credit")
    print("2. Debit")
    print("3. Balance")
    print("4. Mini Statement")
    print("5. Exit")

def get_choice():
    return input("Enter your choice (1-5): ")

def log_transaction(transaction):
    """Append a transaction to the transactions.txt file."""
    file = open(transaction_file, "a")  # Open file in append mode
    file.write(transaction + "\n")  # Write transaction
    file.close()  # Close file manually

def credit():
    global balance
    amount = float(input("Enter amount to credit: "))
    if amount <= 0:
        print("Please enter a positive amount.")
    else:
        balance += amount
        transaction = f"Credited: ${amount}"
        log_transaction(transaction)
        print(f"${amount} credited to your account.")

def debit():
    global balance
    amount = float(input("Enter amount to debit: "))
    if amount <= 0:
        print("Please enter a positive amount.")
    elif amount > balance:
        print("Insufficient balance.")
    else:
        balance -= amount
        transaction = f"Debited: ${amount}"
        log_transaction(transaction)
        print(f"${amount} debited from your account.")

def show_balance():
    print(f"Your current balance is: ${balance}")

def mini_statement():
    print("\nMini Statement (Last 5 Transactions):")
    try:
        file = open(transaction_file, "r")  # Open file in read mode
        transactions = file.readlines()  # Read all lines
        file.close()  # Close file manually

        if not transactions:
            print("No transactions yet.")
        else:
            for txn in transactions[-5:]:  # Show last 5 transactions
                print(txn.strip())
    except FileNotFoundError:
        print("No transactions found.")

def main():
    while True:
        display_menu()
        choice = get_choice()
        
        if choice == '1':
            credit()
        elif choice == '2':
            debit()
        elif choice == '3':
            show_balance()
        elif choice == '4':
            mini_statement()
        elif choice == '5':
            print("Thank you for using the ATM. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

main()
