#D.P.K.L.Peiris 20232630
#Personal Finance Tracker(Using Dictionaries)
from tkinter import*
import json

transactions = {} #transactions is the global dictionary 
file_name = "transactions.json" #JSON file name as the transactions.json

#To load transactions data from the Json file 
def load_transactions():
    global transactions #To Manage transactions dictionary across the program
    try:
        with open(file_name, 'r') as Json_file:
            #Loading data from the JSON file into 'transactions' dictionary
            transactions = json.load(Json_file)
            print("Transaction data loaded successfully ✅.")
    except FileNotFoundError:
        print("File not found❗Proceeding with an empty list of transactions.")
    except json.JSONDecodeError:
        print("Error❗The file format is not valid JSON.")

#To save the transactions in the JSON file
def save_transactions():
    global transactions
    with open(file_name, 'w') as Json_file:
        #dumping the data into the JSON file
        json.dump(transactions, Json_file, indent = 4)

#To import data from another text file
def read_bulk_transactions_from_file(filename2):
    global transactions
    load_transactions()  # Ensure we are working with the latest data.
    # Append '.txt' to the filename if input doesn't already end with '.txt'
    if not filename2.endswith('.txt'):
        filename2 += '.txt'
    try:
        with open(filename2, "r") as file:
            content = file.read() #Reading the file
            data = json.loads(content)  # Load JSON data from file to dictionary
            for category, items in data.items():
                if category in transactions: #checks if category is already in the dictionary 
                    transactions[category].extend(items) #if the category exists, extend the existing list
                else:
                    transactions[category] = items
        print("Transactions imported successfully✅.")
    except FileNotFoundError:
        print(f"Error❗The file '{filename2}' does not exist.")
    except json.JSONDecodeError:
        print("Error❗parsing JSON. Please check the format of your file.")
    except IOError as e:
        print(f"An error❗occurred while reading from the file: {e}")
    save_transactions()
    view_transactions() #Once those data imported from the file, display the transactions dictionary

#To add new transactions to the transactions dictionary    
def add_transaction():
    global transactions
    while True:
        try:
            given_name = input("Enter a name for the transaction : ") #Getting an input for the transaction name
            if not given_name.isalpha():  # Checks if the given name contains only alphabets
                raise ValueError    
        except ValueError:
            print("The name should only include alphabetic characters❗.") # Print the error message and prompt again
        else:
            # If the input is valid, process the name and break the loop
            first_letter = given_name[0].upper()  # Capitalize the first letter
            rest_letters = given_name[1:].lower()  # Lowercase the rest of the letters
            transaction_name = first_letter + rest_letters #As the full name combine the first letter and rest
            break
    
    #Adding the transaction Type
    while True:
        #Asking the transaction type if it is an income or expense
        transaction_type = input("Enter 'income' or 'expense': ").lower()
        if transaction_type in ['income', 'expense']: #Checks if the given transaction type is an income or an expense
            break
        print("Input must be 'income' or 'expense' only❗please correct it.")

    #Adding a transaction Amount
    while True:
        try:
            #Getting a transaction amount as a float
            transaction_amount = float(input("Enter the amount for the transaction: "))
            break
        except ValueError:
            print("Input was incorrect❗Enter a valid amount.")

    #Adding a transaction Date
    while True:
        transaction_date = input("Enter the date of the transaction as YYYY-MM-DD : ")
        try:
            year, month, day = map(int, transaction_date.split('-')) #split the date by hyphens and convert each part as an integer
            if not (1000 <= year <= 9999 and 1 <= month <= 12 and 1 <= day <= 31): #Checks if it is a valid date
                raise ValueError
            break
        except ValueError:
            print("Input is incorrect❗Enter a date using the 'YYYY-MM-DD' format")

    if transaction_name in transactions: #If given transaction name is already in the dictionary append these data into that transaction
        transactions[transaction_name].append({"type": transaction_type, "amount": transaction_amount, "date": transaction_date})
        save_transactions()#save transactions
    else:
        transactions[transaction_name] = [] #If the transaction does not already in the dictionary create a new list in the dictionary 
        #And appending new transaction details into that
        transactions[transaction_name].append({"type": transaction_type, "amount": transaction_amount, "date": transaction_date})
        save_transactions()#save transactions
    print(f"Transaction successfully recorded ✅.")

#To view the transactions in the transactions deictionary
def view_transactions():
        if transactions: #Checks if the 'transactions' dictionary contains any entries
            for number, data in transactions.items(): #A Loop for each key and value in the transactions dictionary
                print(f"{number} : {data} ") #Print the transaction number key and its value
        else:
            print("No transactions available to view❎ ")
#To update transactions in the dictionary
def update_transaction():
    view_transactions()#let user to see the transactions in the dictionary
    if not transactions:#IF there are no transactions in the dictionary
        print("No transactions are available to update❎.")
        return

    # Asking for the category name that user wants to update
    category = input("Enter the category of the transaction you wish to update⬆⬆⬆: ")
    if category not in transactions:#checks if the category in the transactions 
        print("The specified category does not exist❎.")
        return
    
    #Displaying transactions under the chosen category
    #Prints each transaction under the same category with an index number from 1
    for i, trans in enumerate(transactions[category]):
        print(f"{i + 1}: {trans}")

    #Getting the index of the transaction under the same category
    while True:
        try:
            transaction_index = int(input("Enter the number of the transaction you want to update⬆⬆⬆: ")) - 1
            if 0 <= transaction_index < len(transactions[category]):#Check the validity of the index that is given
                break
            else:
                print("The transaction number does not exist❗Please enter a valid number: ")
        except ValueError:
            print("Input was invalid❗Please enter a number: ")
    
    #To update the transaction by accessing the category and index within the dictionary
    transaction_to_update = transactions[category][transaction_index]
    #Updating the type of the transaction
    while True:
        new_type = input("Enter 'income' or 'expense': ").lower()
        if new_type in ['income', 'expense']:
            transaction_to_update['type'] = new_type
            break
    print("Input must be 'income' or 'expense' only❗please correct it.")

    # Updating the amount of the transaction 
    while True:
        try:
            new_amount = float(input("Type a new transaction amount: "))
            transaction_to_update['amount'] = float(new_amount)
            break
        except ValueError:
            print("Input was invalid❗Please enter a number: ")
                
                

    # Updating the date of the transaction 
    while True:
        try:
            new_date = input("Enter a new date as YYYY-MM-DD for the transaction: ")
            year, month, day = map(int, new_date.split('-'))
            if not (1000 <= year <= 9999 and 1 <= month <= 12 and 1 <= day <= 31):
                raise ValueError
            transaction_to_update['date'] = new_date
            break
        except ValueError:
            print("Input is incorrect❗Enter a date using the 'YYYY-MM-DD' format.")
    
    # Saving the updated transaction
    transactions[category][transaction_index] = transaction_to_update
    print("The transaction updated successfully✅:")
    print(transactions[category][transaction_index])
    save_transactions()   
    
#To delete a transaction from the transactions list
def delete_transaction():
    view_transactions()#Showing the transactions list
    if not transactions:#If there are no transactions to delete let the user know it
        print("No transactions available to delete🗑️.")
        return

    category = input("Enter the category of the transaction you wish to delete🗑️: ")
    if category in transactions:#asking the category of the transaction that user wish to delete
        if transactions[category]:#If category is there show the transactions inside the category with index numbers
            for i, transac in enumerate(transactions[category]):
                print(f"{i + 1}: {transac}")
            try:
                transaction_index = int(input("Enter the number of the transaction you wish to delete🗑️: ")) - 1
                if 0 <= transaction_index < len(transactions[category]):#Check the validity of the index the user gave
                    del transactions[category][transaction_index]
                    print(f"The transaction deleted successfully✅")
                    # delete the category if no more transactions exist in this category
                    if not transactions[category]:
                        del transactions[category]
                    save_transactions()#saving
                else:
                    print("Invalid transaction number❗Please enter a valid number: ")
            except ValueError:
                print("Invalid input❗Please enter a number: ")
        else:
            print(f"No transactions found in category {category}❗.")
    else:
        print("Given category does not exist❗.")


#To display a summary about income and expenses of all transactions 
def display_summary():
    if not transactions:#If there are no transactions in the dictionary
        print("No transactions available to display❎.")
        return
    total_income = 0 #total income as 0
    total_expense = 0 #total expense as 0

    # Checks the types of all the transactions if it is an income or an expense 
    # Add incomes to the total_income and add expenses to the total_expense
    for category, transaction_list in transactions.items():
        for transaction in transaction_list:
            if 'type' in transaction and transaction['type'] == 'income':
                total_income += transaction['amount']
            elif 'type' in transaction and transaction['type'] == 'expense':
                total_expense += transaction['amount']

    # Print the total incomes and expenses
    print(f"The total income is😀: {total_income}$")
    print(f"The total expenses are☹️: {total_expense}$")
    #A mood for the user
    if total_income > total_expense:
        print("🤑😃")
    elif total_expense > total_income:
        print("😞😭")

#Main menu function    
def main_menu():
    load_transactions()
    while True:
        print('''🤑 Track your personal finances 💵
        1. Add Transaction 💰
        2. View Transactions 👁
        3. Update Transaction ⬆
        4. Delete Transaction ❎
        5. Display Summary 🖥
        6. Import Transactions from a Text File 📩
        7. Exit 🚶🏻''')       
        choice = input("Enter a given choice (1/2/3/4/5/6/7) : ")
        if choice == '1':
            add_transaction()
        elif choice == '2':
            view_transactions()
        elif choice == '3':
            update_transaction()
        elif choice == '4':
            delete_transaction()
        elif choice == '5':
            display_summary()
        elif choice == '6':
            filename2 = input("Enter the filename to load transactions from :")
            read_bulk_transactions_from_file(filename2)
            save_transactions()           
        elif choice == '7':
            print("Exiting the program🚶🏻.")
            break
        else:
            print("Invalid input❗Please Enter a choice from 1/2/3/4/5/6/7.")

#Callng the main menu
main_menu()

