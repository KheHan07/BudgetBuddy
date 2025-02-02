import tkinter as tk
from tkinter import ttk
import json
import os

class FinanceTrackerGUI:
    def __init__(self, root):   
        self.root = root
        self.root.title("Personal Finance Manager")
        self.root.geometry("1366x768")
        self.root.configure(bg="#f0f8ff")  # Light blue background
        self.create_widgets()
        self.transactions = self.load_transactions("transactions.json")
        self.filtered_transactions = self.transactions
        self.display_transactions()
        self.display_file_details("transactions.json")

    def create_widgets(self):
        # Frame for search bar and buttons
        self.search_frame = ttk.Frame(self.root, padding=(10, 10))
        self.search_frame.pack(side=tk.TOP, fill=tk.X)

        self.search_var = tk.StringVar()
        self.search_entry = ttk.Entry(self.search_frame, textvariable=self.search_var, font=("Berlin Sans FB Demi", 10))
        self.search_entry.pack(side=tk.LEFT, padx=5, pady=5)

        self.search_button = ttk.Button(self.search_frame, text="Search", command=self.search_transactions, style='My.TButton')
        self.search_button.pack(side=tk.LEFT, padx=5, pady=5)

        self.reset_button = ttk.Button(self.search_frame, text="Reset", command=self.reset_transactions, style='My.TButton')
        self.reset_button.pack(side=tk.LEFT, padx=5, pady=5)

        # Style for scrollbar and buttons
        style = ttk.Style()
        style.theme_use('clam')
        style.configure('My.TButton', foreground='white', background='#001f3f', font=('Berlin Sans FB Demi', 10))
        style.configure("My.Horizontal.TScrollbar", troughcolor="#f0f8ff", bordercolor="#001f3f", darkcolor="#001f3f", lightcolor="#001f3f")

        # Frame for the treeview
        self.frame = ttk.Frame(self.root, borderwidth=2, relief=tk.RAISED)
        self.frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        self.tree = ttk.Treeview(self.frame, columns=("category", "Amount", "Type", "Date"), show="headings")
        self.tree.heading("category", text="Category", command=lambda: self.sort_by_column("category"))
        self.tree.heading("Amount", text="Amount", command=lambda: self.sort_by_column("Amount"))
        self.tree.heading("Type", text="Type", command=lambda: self.sort_by_column("Type"))
        self.tree.heading("Date", text="Date", command=lambda: self.sort_by_column("Date"))
        self.tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.scrollbar = ttk.Scrollbar(self.frame, orient=tk.VERTICAL, command=self.tree.yview)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.tree.configure(yscrollcommand=self.scrollbar.set)

        self.file_details_label = ttk.Label(self.root, text="", background="#f0f8ff")
        self.file_details_label.pack()

    def load_transactions(self, filename):
        try:
            with open(filename, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return {}

    def display_transactions(self):
        for item_id in self.tree.get_children():
            self.tree.delete(item_id)

        for category, items in self.filtered_transactions.items():
            for item in items:
                self.tree.insert('', 'end', values=(category, item['amount'], item['type'], item['date']))

    def search_transactions(self):
        search = self.search_var.get().lower()
        if search:
            filtered_transactions = {}
            for category, items in self.transactions.items():
                for item in items:
                    if (search in category.lower() or
                        search in item['type'].lower() or
                        search in item['date'] or
                        search in str(item['amount'])):
                        if category not in filtered_transactions:
                            filtered_transactions[category] = []
                        filtered_transactions[category].append(item)
        else:
            filtered_transactions = self.transactions

        self.filtered_transactions = filtered_transactions
        self.display_transactions()

    def reset_transactions(self):
        self.search_var.set("") 
        self.filtered_transactions = self.transactions
        self.display_transactions()

    def sort_by_column(self, col, reverse=False):
        transactions = [(self.tree.set(child, col), child) for child in self.tree.get_children("")]
        if all(value.replace('.', '', 1).isdigit() for value, _ in transactions): 
            transactions.sort(key=lambda x: float(x[0]), reverse=reverse)
        else:
            transactions.sort(key=lambda x: x[0].lower(), reverse=reverse)
        
        for index, (value, child) in enumerate(transactions):
            self.tree.move(child, "", index)

        self.tree.heading(col, command=lambda: self.sort_by_column(col, not reverse))

    def display_file_details(self, filename):
        file_details = f"File Name: {filename}\nFile Size: {os.path.getsize(filename)} bytes"
        self.file_details_label.config(text=file_details)

def main():
    root = tk.Tk()
    app = FinanceTrackerGUI(root)
    root.iconbitmap("images.ico")
    root.mainloop()

if __name__ == "__main__":
    main()
