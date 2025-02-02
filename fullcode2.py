import customtkinter
import tkinter as tk
from PIL import Image, ImageTk
from tkinter import messagebox
from tkinter import*
import json

transactions = {}
file_name = "transactions.json"

class WindowManager:
    def __init__(self, root):
        self.root = root
        self.windows_stack = []

    def show_window(self, window):
        # Hide the current window if there's any
        if self.windows_stack:
            current_window = self.windows_stack[-1]
            current_window.pack_forget()

        # Show the new window
        window.pack(fill=tk.BOTH, expand=True)
        self.windows_stack.append(window)

    def go_back(self):
        # Pop the top window from the stack
        if len(self.windows_stack) > 1:
            self.windows_stack.pop().pack_forget()

            # Show the previous window
            prev_window = self.windows_stack[-1]
            prev_window.pack(fill=tk.BOTH, expand=True)
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

def save_transactions():
    global transactions
    try:
        with open(file_name, 'w') as Json_file:
            json.dump(transactions, Json_file, indent=4)
            print("Transactions saved successfully ✅.")
    except Exception as e:
        print("Error occurred while saving transactions:", e)

def update_label_text(label, text):
    label.configure(text=text)


def view_transactions(label):
    global transactions
    if transactions: 
        # Initialize an empty string to store transaction information
        transactions_text = ""
        for number, data in transactions.items():
            transactions_text += f"{number} : {data}\n"
        update_label_text(label, transactions_text)
    else:
        update_label_text(label, "No transactions available to view❎")

def validate_input():
        global transactions

        # Retrieve input data
        given_name = q1.get().strip()
        transaction_type = q2.get().lower().strip()
        transaction_amount = float(q3.get().strip())
        transaction_date = q4.get().strip()

        # Check if all fields are filled
        if given_name == "" or transaction_type == "" or transaction_amount == "" or transaction_date == "":
            messagebox.showerror("Error", "All fields are required")
            return

        # Check validity of the date
        try:
            year, month, day = map(int, transaction_date.split('-'))
            if not (1000 <= year <= 9999 and 1 <= month <= 12 and 1 <= day <= 31):
                raise ValueError
        except ValueError:
            messagebox.showerror("Error", "Enter a valid date in the format YYYY-MM-DD")
            return

        # Create a new transaction entry
        new_transaction = {
            "type": transaction_type,
            "amount": transaction_amount,
            "date": transaction_date
        }

        # Add the transaction to the appropriate category or create a new category
        if given_name in transactions:
            transactions[given_name].append(new_transaction)
        else:
            transactions[given_name] = [new_transaction]

        # Save transactions to the JSON file
        save_transactions()

        # Update label to display the new transaction
        view_transactions()

        # Confirmation message
        messagebox.showinfo("Success", "Transaction saved successfully")

        # Optional: Clear input fields after saving
        q1.delete(0, tk.END)
        q2.delete(0, tk.END)
        q3.delete(0, tk.END)
        q4.delete(0, tk.END)




def button_function():
    print("Button pressed")

def main():
    customtkinter.set_appearance_mode("system")  # Modes: system (default), light, dark
    customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green
    root = customtkinter.CTk()
    root.geometry("1366x768")
    root.title("Your Finance Tracker")
    
    load_transactions()
    
    def is_savetransactions():  
        save_transactions()

    title_bar1 = customtkinter.CTkLabel(master=root, text="💲  Y O U R    P E R S O N A L    F I N A N C E    M A N A G E R  💲",
                                        fg_color="#dcdcbb", 
                                        height=70,
                                        text_color="#2c345c",font=("Berlin Sans FB Demi", 23, "bold"))
    title_bar1.pack(fill="x")
    title_bar2 = customtkinter.CTkLabel(master=root, text='"  T H E   A R T   I S   N O T   M A K I N G   M O N E Y  ,   B U T   I N   M A N A G I N G   I T  !  "',
                                        fg_color="#425e6a", 
                                        height=50,
                                        text_color="#dcdcbb",font=("Berlin Sans FB Demi", 16,'bold'))
    title_bar2.pack(fill="x")

    title_frame = customtkinter.CTkFrame(master=root)
    title_frame.pack(side="bottom", fill="x")
    title_bar3 = customtkinter.CTkLabel(
        master=title_frame,
        text='"  S A V E   M O N E Y   A N D   M O N E Y   W I L L   S A V E   Y O U  "',
        fg_color="#244c3c",
        height=70,
        text_color="#dcdcbb",
        font=("Berlin Sans FB Demi", 20, 'bold'))
    title_bar3.pack(fill="x")

    window_manager = WindowManager(root)

    window1 = customtkinter.CTkFrame(root, width=1366, height=768)

    button = customtkinter.CTkButton(master=window1,
                                    width=200,
                                    height=65,
                                    bg_color="#716b55",
                                    fg_color='#244c3c',
                                    hover_color="#000000",
                                    text_color="#dcdcbb",
                                    font=("Berlin Sans FB Demi", 18,'bold'),
                                    corner_radius=5,
                                    border_width=7,
                                    border_color="#dcdcbb",
                                    text="Add a Transaction💰",
                                    command=lambda: window_manager.show_window(window2))
    button.place(relx=0.25, rely=0.37, anchor=customtkinter.CENTER)


    button2 = customtkinter.CTkButton(master=window1,
                                    text="View Transactions👁",
                                    width=200,
                                    height=65,
                                    bg_color="#000000",
                                    fg_color='#244c3c',
                                    hover_color="#000000",
                                    text_color="#dcdcbb",
                                    font=("Berlin Sans FB Demi", 18,'bold'),
                                    corner_radius=5,
                                    border_width=7,
                                    border_color="#dcdcbb",
                                    command=lambda: window_manager.show_window(window3))
    button2.place(relx=0.5, rely=0.37, anchor=customtkinter.CENTER)

    # Create Button 3
    button3 = customtkinter.CTkButton(master=window1,
                                    width=200,
                                    height=65,
                                    bg_color="#000000",
                                    fg_color='#244c3c',
                                    hover_color="#000000",
                                    text_color="#dcdcbb",
                                    font=("Berlin Sans FB Demi", 18,'bold'),
                                    corner_radius=5,
                                    border_width=7,
                                    border_color="#dcdcbb",
                                    text="Update a Transaction⬆",
                                    command=lambda: window_manager.show_window(window4))
    button3.place(relx=0.75, rely=0.37, anchor=customtkinter.CENTER)

    # Create Button 4
    button4 = customtkinter.CTkButton(master=window1, 
                                    width=200,
                                    height=65,
                                    bg_color="#000000",
                                    fg_color='#244c3c',
                                    hover_color="#000000",
                                    text_color="#dcdcbb",
                                    font=("Berlin Sans FB Demi", 18,'bold'),
                                    corner_radius=5,
                                    border_width=7,
                                    border_color="#dcdcbb",
                                    text="Delete Transaction❎", 
                                    command=lambda: window_manager.show_window(window7))
    button4.place(relx=0.25, rely=0.52, anchor=customtkinter.CENTER)

    # Create Button 5
    button5 = customtkinter.CTkButton(master=window1, 
                                    width=200,
                                    height=65,
                                    bg_color="#000000",
                                    fg_color='#244c3c',
                                    hover_color="#000000",
                                    text_color="#dcdcbb",
                                    font=("Berlin Sans FB Demi", 18,'bold'),
                                    corner_radius=5,
                                    border_width=7,
                                    border_color="#dcdcbb",
                                    text="Display Summary🖥",
                                    command=lambda: window_manager.show_window(window9))
    button5.place(relx=0.5, rely=0.52, anchor=customtkinter.CENTER)

    # Create Button 6
    button6 = customtkinter.CTkButton(master=window1, 
                                    width=200,
                                    height=65,
                                    bg_color="#000000",
                                    fg_color='#244c3c',
                                    hover_color="#000000",
                                    text_color="#dcdcbb",
                                    font=("Berlin Sans FB Demi", 18,'bold'),
                                    corner_radius=5,
                                    border_width=7,
                                    border_color="#dcdcbb",
                                    text='''Import Transactions 
    from a Text File📩''', 
                                    command=button_function)
    button6.place(relx=0.75, rely=0.52, anchor=customtkinter.CENTER)

    button7 = customtkinter.CTkButton(master=window1,
                                    width=200,
                                    height=65,
                                    bg_color="#000000",
                                    fg_color='#244c3c',
                                    hover_color="#000000",
                                    text_color="#dcdcbb",
                                    font=("Berlin Sans FB Demi", 18,'bold'),
                                    corner_radius=5,
                                    border_width=7,
                                    border_color="#dcdcbb",
                                    text="Exit🚶🏻",
                                    command=exit)
    button7.place(relx=0.5, rely=0.67, anchor=customtkinter.CENTER)


    window2 = customtkinter.CTkFrame(root, width=1366, height=768)

    add_transaction = customtkinter.CTkLabel(master=window2,
                                            width=220,
                                            height=50, 
                                            text="Name of the transaction",
                                            text_color= "#244c3c",
                                            fg_color="#dcdcbb",
                                            corner_radius=5,
                                            bg_color="#716b55",
                                            font=("Berlin Sans FB Demi", 18,'bold'))
    add_transaction.place(relx=0.25, rely=0.27, anchor=customtkinter.CENTER)
    add_transaction1 = customtkinter.CTkLabel(master=window2,
                                            width=220,
                                            height=50, 
                                            text="Type of the transaction",
                                            text_color= "#244c3c",
                                            fg_color="#dcdcbb",
                                            corner_radius=5,
                                            bg_color="#716b55",
                                            font=("Berlin Sans FB Demi", 18,'bold'))
    add_transaction1.place(relx=0.25, rely=0.4, anchor=customtkinter.CENTER)
    add_transaction2 = customtkinter.CTkLabel(master=window2,
                                            width=220,
                                            height=50, 
                                            text="Amount of the transaction",
                                            text_color= "#244c3c",
                                            fg_color="#dcdcbb",
                                            corner_radius=5,
                                            bg_color="#716b55",
                                            font=("Berlin Sans FB Demi", 18,'bold'))
    add_transaction2.place(relx=0.25, rely=0.53, anchor=customtkinter.CENTER)
    add_transaction3 = customtkinter.CTkLabel(master=window2,
                                            width=220,
                                            height=50, 
                                            text="Date of the transaction",
                                            text_color= "#244c3c",
                                            fg_color="#dcdcbb",
                                            corner_radius=5,
                                            bg_color="#716b55",
                                            font=("Berlin Sans FB Demi", 18,'bold'))
    add_transaction3.place(relx=0.25, rely=0.66, anchor=customtkinter.CENTER)
    global q1
    global q2
    global q3
    global q4
    q1 = customtkinter.CTkEntry(master=window2,                                       
                                width=300,
                                height=50,
                                placeholder_text="            E n t e r   t h e   n a m e",
                                text_color= "#244c3c",
                                fg_color="#dcdcbb",
                                corner_radius=5,
                                bg_color="#716b55",
                                font=("Berlin Sans FB Demi", 15))
    q1.place(relx=0.55, rely=0.27, anchor=customtkinter.CENTER)
    q2 = customtkinter.CTkEntry(master=window2,                                       
                                width=300,
                                height=50,
                                placeholder_text="            i n c o m e / e x p e n s e",
                                text_color= "#244c3c",
                                fg_color="#dcdcbb",
                                corner_radius=5,
                                bg_color="#716b55",
                                font=("Berlin Sans FB Demi", 15))
    q2.place(relx=0.55, rely=0.4, anchor=customtkinter.CENTER)
    q3 = customtkinter.CTkEntry(master=window2,                                       
                                width=300,
                                height=50,
                                placeholder_text="            E n t e r   a m o u n t",
                                text_color= "#244c3c",
                                fg_color="#dcdcbb",
                                corner_radius=5,
                                bg_color="#716b55",
                                font=("Berlin Sans FB Demi", 15))
    q3.place(relx=0.55, rely=0.53, anchor=customtkinter.CENTER)
    q4 = customtkinter.CTkEntry(master=window2,                                       
                                width=300,
                                height=50,
                                placeholder_text="            D a t e  :  Y Y Y Y-M M-D D",
                                text_color= "#244c3c",
                                fg_color="#dcdcbb",
                                corner_radius=5,
                                bg_color="#716b55",
                                font=("Berlin Sans FB Demi", 15))
    q4.place(relx=0.55, rely=0.66, anchor=customtkinter.CENTER)


    add_button = customtkinter.CTkButton(master=window2,
                                         command=lambda: (window_manager.show_window(window1),validate_input()),
                                         width=300,
                                         height=50,
                                         bg_color="#000000",
                                         fg_color='#244c3c',
                                         hover_color="#000000",
                                         text_color="#dcdcbb",
                                         font=("Berlin Sans FB Demi", 18, 'bold'),
                                         corner_radius=5,
                                         border_width=7,
                                         border_color="#dcdcbb",
                                         text="submit")
    add_button.place(relx=0.55, rely=0.79, anchor=customtkinter.CENTER)
    save_transactions()


    window3 = customtkinter.CTkFrame(root, width=1366, height=768)
    viewtransaction = customtkinter.CTkLabel(master=window3,
                                            width=500,
                                            height=500, 
                                            text="",
                                            text_color= "#244c3c",
                                            fg_color="#dcdcbb",
                                            corner_radius=5,
                                            bg_color="#716b55",
                                            font=("Berlin Sans FB Demi", 15,'bold'))
    viewtransaction.place(relx=0.5, rely=0.5, anchor=customtkinter.CENTER)
    view_transactions(viewtransaction)

    backbutton = customtkinter.CTkButton(master=window3,
                                         command=lambda: window_manager.show_window(window1),
                                         width=300,
                                         height=50,
                                         bg_color="#000000",
                                         fg_color='#244c3c',
                                         hover_color="#000000",
                                         text_color="#dcdcbb",
                                         font=("Berlin Sans FB Demi", 18, 'bold'),
                                         corner_radius=5,
                                         border_width=7,
                                         border_color="#dcdcbb",
                                         text="back")
    backbutton.place(relx=0.2, rely=0.2, anchor=customtkinter.CENTER)

    window4 = customtkinter.CTkFrame(root, width=1366, height=768)
    updatetransaction = customtkinter.CTkLabel(master=window4,
                                            width=220,
                                            height=50, 
                                            text="Enter the category of the transaction",
                                            text_color= "#244c3c",
                                            fg_color="#dcdcbb",
                                            corner_radius=5,
                                            bg_color="#716b55",
                                            font=("Berlin Sans FB Demi", 18,'bold'))
    updatetransaction.place(relx=0.25, rely=0.27, anchor=customtkinter.CENTER)

    textupdate = customtkinter.CTkEntry(master=window4,                                       
                                width=350,
                                height=50,
                                placeholder_text="            Enter the category name",
                                text_color= "#244c3c",
                                fg_color="#dcdcbb",
                                corner_radius=5,
                                bg_color="#716b55",
                                font=("Berlin Sans FB Demi", 15))
    textupdate.place(relx=0.5, rely=0.27, anchor=customtkinter.CENTER)

    add_button1 = customtkinter.CTkButton(master=window4,
                                         command=lambda: window_manager.show_window(window1),
                                         width=300,
                                         height=50,
                                         bg_color="#000000",
                                         fg_color='#244c3c',
                                         hover_color="#000000",
                                         text_color="#dcdcbb",
                                         font=("Berlin Sans FB Demi", 18, 'bold'),
                                         corner_radius=5,
                                         border_width=7,
                                         border_color="#dcdcbb",
                                         text="Menu")
    add_button1.place(relx=0.55, rely=0.79, anchor=customtkinter.CENTER)
    add_button2 = customtkinter.CTkButton(master=window4,
                                         command=lambda: window_manager.show_window(window5),
                                         width=300,
                                         height=50,
                                         bg_color="#000000",
                                         fg_color='#244c3c',
                                         hover_color="#000000",
                                         text_color="#dcdcbb",
                                         font=("Berlin Sans FB Demi", 18, 'bold'),
                                         corner_radius=5,
                                         border_width=7,
                                         border_color="#dcdcbb",
                                         text="submit")
    add_button2.place(relx=0.55, rely=0.59, anchor=customtkinter.CENTER)



    window5 = customtkinter.CTkFrame(root, width=1366, height=768)

    viewtransaction1 = customtkinter.CTkLabel(master=window5,
                                            width=300,
                                            height=300, 
                                            text="all the transactions",
                                            text_color= "#244c3c",
                                            fg_color="#dcdcbb",
                                            corner_radius=5,
                                            bg_color="#716b55",
                                            font=("Berlin Sans FB Demi", 18,'bold'))
    viewtransaction1.place(relx=0.2, rely=0.2, anchor=customtkinter.CENTER)

    submit = customtkinter.CTkButton(master=window5,
                                         command=lambda: window_manager.show_window(window6),
                                         width=300,
                                         height=50,
                                         bg_color="#000000",
                                         fg_color='#244c3c',
                                         hover_color="#000000",
                                         text_color="#dcdcbb",
                                         font=("Berlin Sans FB Demi", 18, 'bold'),
                                         corner_radius=5,
                                         border_width=7,
                                         border_color="#dcdcbb",
                                         text="submit")
    submit.place(relx=0.8, rely=0.8, anchor=customtkinter.CENTER)

    updatenewtransaction = customtkinter.CTkLabel(master=window5,
                                            width=220,
                                            height=50, 
                                            text="Enter the index inside the category",
                                            text_color= "#244c3c",
                                            fg_color="#dcdcbb",
                                            corner_radius=5,
                                            bg_color="#716b55",
                                            font=("Berlin Sans FB Demi", 18,'bold'))
    updatenewtransaction.place(relx=0.25, rely=0.6, anchor=customtkinter.CENTER)

    textupdateindex = customtkinter.CTkEntry(master=window5,                                       
                                width=350,
                                height=50,
                                placeholder_text="            Enter the index number",
                                text_color= "#244c3c",
                                fg_color="#dcdcbb",
                                corner_radius=5,
                                bg_color="#716b55",
                                font=("Berlin Sans FB Demi", 15))
    textupdateindex.place(relx=0.5, rely=0.6, anchor=customtkinter.CENTER)

    window6 = customtkinter.CTkFrame(root, width=1366, height=768)

    newadd_transaction1 = customtkinter.CTkLabel(master=window6,
                                            width=220,
                                            height=50, 
                                            text="NEW Type of the transaction",
                                            text_color= "#244c3c",
                                            fg_color="#dcdcbb",
                                            corner_radius=5,
                                            bg_color="#716b55",
                                            font=("Berlin Sans FB Demi", 18,'bold'))
    newadd_transaction1.place(relx=0.25, rely=0.4, anchor=customtkinter.CENTER)
    newadd_transaction2 = customtkinter.CTkLabel(master=window6,
                                            width=220,
                                            height=50, 
                                            text="NEW Amount of the transaction",
                                            text_color= "#244c3c",
                                            fg_color="#dcdcbb",
                                            corner_radius=5,
                                            bg_color="#716b55",
                                            font=("Berlin Sans FB Demi", 18,'bold'))
    newadd_transaction2.place(relx=0.25, rely=0.53, anchor=customtkinter.CENTER)
    newadd_transaction3 = customtkinter.CTkLabel(master=window6,
                                            width=220,
                                            height=50, 
                                            text="NEW Date of the transaction",
                                            text_color= "#244c3c",
                                            fg_color="#dcdcbb",
                                            corner_radius=5,
                                            bg_color="#716b55",
                                            font=("Berlin Sans FB Demi", 18,'bold'))
    newadd_transaction3.place(relx=0.25, rely=0.66, anchor=customtkinter.CENTER)
    global newq2
    global newq3
    global newq4
    newq2 = customtkinter.CTkEntry(master=window6,                                       
                                width=300,
                                height=50,
                                placeholder_text="           NEW  i n c o m e / e x p e n s e",
                                text_color= "#244c3c",
                                fg_color="#dcdcbb",
                                corner_radius=5,
                                bg_color="#716b55",
                                font=("Berlin Sans FB Demi", 15))
    newq2.place(relx=0.55, rely=0.4, anchor=customtkinter.CENTER)
    newq3 = customtkinter.CTkEntry(master=window6,                                       
                                width=300,
                                height=50,
                                placeholder_text="            NEW E n t e r   a m o u n t",
                                text_color= "#244c3c",
                                fg_color="#dcdcbb",
                                corner_radius=5,
                                bg_color="#716b55",
                                font=("Berlin Sans FB Demi", 15))
    newq3.place(relx=0.55, rely=0.53, anchor=customtkinter.CENTER)
    newq4 = customtkinter.CTkEntry(master=window6,                                       
                                width=300,
                                height=50,
                                placeholder_text="           NEW D a t e  :  Y Y Y Y-M M-D D",
                                text_color= "#244c3c",
                                fg_color="#dcdcbb",
                                corner_radius=5,
                                bg_color="#716b55",
                                font=("Berlin Sans FB Demi", 15))
    newq4.place(relx=0.55, rely=0.66, anchor=customtkinter.CENTER)


    add_button3 = customtkinter.CTkButton(master=window6,
                                         command=lambda: (window_manager.show_window(window1) , validate_input()),
                                         width=300,
                                         height=50,
                                         bg_color="#000000",
                                         fg_color='#244c3c',
                                         hover_color="#000000",
                                         text_color="#dcdcbb",
                                         font=("Berlin Sans FB Demi", 18, 'bold'),
                                         corner_radius=5,
                                         border_width=7,
                                         border_color="#dcdcbb",
                                         text="submit")
    add_button3.place(relx=0.55, rely=0.79, anchor=customtkinter.CENTER)
   
    window7 = customtkinter.CTkFrame(root, width=1366, height=768)

    deletetransaction = customtkinter.CTkLabel(master=window7,
                                            width=220,
                                            height=50, 
                                            text="Enter the category of the transaction to delete",
                                            text_color= "#244c3c",
                                            fg_color="#dcdcbb",
                                            corner_radius=5,
                                            bg_color="#716b55",
                                            font=("Berlin Sans FB Demi", 18,'bold'))
    deletetransaction.place(relx=0.25, rely=0.27, anchor=customtkinter.CENTER)

    textdelete = customtkinter.CTkEntry(master=window7,                                       
                                width=350,
                                height=50,
                                placeholder_text="            Enter the category name to delete",
                                text_color= "#244c3c",
                                fg_color="#dcdcbb",
                                corner_radius=5,
                                bg_color="#716b55",
                                font=("Berlin Sans FB Demi", 15))
    textdelete.place(relx=0.5, rely=0.27, anchor=customtkinter.CENTER)

    deletemenu = customtkinter.CTkButton(master=window7,
                                         command=lambda: window_manager.show_window(window1),
                                         width=300,
                                         height=50,
                                         bg_color="#000000",
                                         fg_color='#244c3c',
                                         hover_color="#000000",
                                         text_color="#dcdcbb",
                                         font=("Berlin Sans FB Demi", 18, 'bold'),
                                         corner_radius=5,
                                         border_width=7,
                                         border_color="#dcdcbb",
                                         text="Menu")
    deletemenu.place(relx=0.55, rely=0.79, anchor=customtkinter.CENTER)
    deletesubmit = customtkinter.CTkButton(master=window7,
                                         command=lambda: window_manager.show_window(window8),
                                         width=300,
                                         height=50,
                                         bg_color="#000000",
                                         fg_color='#244c3c',
                                         hover_color="#000000",
                                         text_color="#dcdcbb",
                                         font=("Berlin Sans FB Demi", 18, 'bold'),
                                         corner_radius=5,
                                         border_width=7,
                                         border_color="#dcdcbb",
                                         text="submit")
    deletesubmit.place(relx=0.55, rely=0.59, anchor=customtkinter.CENTER)
   
    window8 = customtkinter.CTkFrame(root, width=1366, height=768)
    viewtransaction2 = customtkinter.CTkLabel(master=window8,
                                            width=300,
                                            height=300, 
                                            text="all the transactions",
                                            text_color= "#244c3c",
                                            fg_color="#dcdcbb",
                                            corner_radius=5,
                                            bg_color="#716b55",
                                            font=("Berlin Sans FB Demi", 18,'bold'))
    viewtransaction2.place(relx=0.2, rely=0.2, anchor=customtkinter.CENTER)

    submitde = customtkinter.CTkButton(master=window8,
                                         command=lambda: window_manager.show_window(window1),
                                         width=300,
                                         height=50,
                                         bg_color="#000000",
                                         fg_color='#244c3c',
                                         hover_color="#000000",
                                         text_color="#dcdcbb",
                                         font=("Berlin Sans FB Demi", 18, 'bold'),
                                         corner_radius=5,
                                         border_width=7,
                                         border_color="#dcdcbb",
                                         text="Delete")
    submitde.place(relx=0.8, rely=0.8, anchor=customtkinter.CENTER)

    deleteetransaction = customtkinter.CTkLabel(master=window8,
                                            width=220,
                                            height=50, 
                                            text="Enter the index inside to delete",
                                            text_color= "#244c3c",
                                            fg_color="#dcdcbb",
                                            corner_radius=5,
                                            bg_color="#716b55",
                                            font=("Berlin Sans FB Demi", 18,'bold'))
    deleteetransaction.place(relx=0.25, rely=0.6, anchor=customtkinter.CENTER)

    textupdateindex = customtkinter.CTkEntry(master=window8,                                       
                                width=350,
                                height=50,
                                placeholder_text="           DELETE: Enter the index number ",
                                text_color= "#244c3c",
                                fg_color="#dcdcbb",
                                corner_radius=5,
                                bg_color="#716b55",
                                font=("Berlin Sans FB Demi", 15))
    textupdateindex.place(relx=0.5, rely=0.6, anchor=customtkinter.CENTER)

    window9 = customtkinter.CTkFrame(root, width=1366, height=768)
    viewtransaction3 = customtkinter.CTkLabel(master=window9,
                                            width=300,
                                            height=300, 
                                            text="summary",
                                            text_color= "#244c3c",
                                            fg_color="#dcdcbb",
                                            corner_radius=5,
                                            bg_color="#716b55",
                                            font=("Berlin Sans FB Demi", 18,'bold'))
    viewtransaction3.place(relx=0.2, rely=0.2, anchor=customtkinter.CENTER)

    summarymenu = customtkinter.CTkButton(master=window9,
                                         command=lambda: window_manager.show_window(window1),
                                         width=300,
                                         height=50,
                                         bg_color="#000000",
                                         fg_color='#244c3c',
                                         hover_color="#000000",
                                         text_color="#dcdcbb",
                                         font=("Berlin Sans FB Demi", 18, 'bold'),
                                         corner_radius=5,
                                         border_width=7,
                                         border_color="#dcdcbb",
                                         text="Menu")
    summarymenu.place(relx=0.55, rely=0.79, anchor=customtkinter.CENTER)

    window_manager.show_window(window1)
    root.mainloop()

if __name__ == "__main__":
    main()
