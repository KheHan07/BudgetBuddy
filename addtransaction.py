import customtkinter
from PIL import Image, ImageTk
from tkinter import messagebox

def add_transaction_face():
    # Set appearance mode and default color theme
    customtkinter.set_appearance_mode("dark")  # Modes: system (default), light, dark
    customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green
    
    # Create a CTk window instance
    app2 = customtkinter.CTk()
    app2.geometry("1000x700")
    app2.title("Your Finance Tracker")
    app2.iconbitmap("images.ico")

    image = Image.open("vecteezy_hundred-dollar-bills-on-wooden-floor-3d-render_33692798.jpg")
    image = image.resize((2000, 1000))
    photo = ImageTk.PhotoImage(image)
    background_label = customtkinter.CTkLabel(app2, image=photo, text="")
    background_label.place(x=0, y=0, relwidth=1, relheight=1)
    background_label.image = photo

    title_bar1 = customtkinter.CTkLabel(master=app2, text="💲    A   P E N N Y   S A V E D   I S   A   P E N N Y   E A R N E D      💲",
                                        fg_color="#dcdcbb", 
                                        height=70,
                                        text_color="#2c345c",font=("Berlin Sans FB Demi", 23, "bold"))
    title_bar1.pack(fill="x")
    title_bar2 = customtkinter.CTkLabel(master=app2, text='ADD A TRANSACTION',
                                        fg_color="#425e6a", 
                                        height=50,
                                        text_color="#dcdcbb",font=("Berlin Sans FB Demi", 16,'bold'))
    title_bar2.pack(fill="x")

    add_transaction = customtkinter.CTkLabel(master=app2,
                                            width=220,
                                            height=50, 
                                            text="Name of the transaction",
                                            text_color= "#244c3c",
                                            fg_color="#dcdcbb",
                                            corner_radius=5,
                                            bg_color="#716b55",
                                            font=("Berlin Sans FB Demi", 18,'bold'))
    add_transaction.place(relx=0.25, rely=0.27, anchor=customtkinter.CENTER)
    add_transaction1 = customtkinter.CTkLabel(master=app2,
                                            width=220,
                                            height=50, 
                                            text="Type of the transaction",
                                            text_color= "#244c3c",
                                            fg_color="#dcdcbb",
                                            corner_radius=5,
                                            bg_color="#716b55",
                                            font=("Berlin Sans FB Demi", 18,'bold'))
    add_transaction1.place(relx=0.25, rely=0.4, anchor=customtkinter.CENTER)
    add_transaction2 = customtkinter.CTkLabel(master=app2,
                                            width=220,
                                            height=50, 
                                            text="Amount of the transaction",
                                            text_color= "#244c3c",
                                            fg_color="#dcdcbb",
                                            corner_radius=5,
                                            bg_color="#716b55",
                                            font=("Berlin Sans FB Demi", 18,'bold'))
    add_transaction2.place(relx=0.25, rely=0.53, anchor=customtkinter.CENTER)
    add_transaction3 = customtkinter.CTkLabel(master=app2,
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
    q1 = customtkinter.CTkEntry(master=app2,                                       
                                width=300,
                                height=50,
                                placeholder_text="            E n t e r   t h e   n a m e",
                                text_color= "#244c3c",
                                fg_color="#dcdcbb",
                                corner_radius=5,
                                bg_color="#716b55",
                                font=("Berlin Sans FB Demi", 15))
    q1.place(relx=0.55, rely=0.27, anchor=customtkinter.CENTER)
    q2 = customtkinter.CTkEntry(master=app2,                                       
                                width=300,
                                height=50,
                                placeholder_text="            i n c o m e / e x p e n s e",
                                text_color= "#244c3c",
                                fg_color="#dcdcbb",
                                corner_radius=5,
                                bg_color="#716b55",
                                font=("Berlin Sans FB Demi", 15))
    q2.place(relx=0.55, rely=0.4, anchor=customtkinter.CENTER)
    q3 = customtkinter.CTkEntry(master=app2,                                       
                                width=300,
                                height=50,
                                placeholder_text="            E n t e r   a m o u n t",
                                text_color= "#244c3c",
                                fg_color="#dcdcbb",
                                corner_radius=5,
                                bg_color="#716b55",
                                font=("Berlin Sans FB Demi", 15))
    q3.place(relx=0.55, rely=0.53, anchor=customtkinter.CENTER)
    q4 = customtkinter.CTkEntry(master=app2,                                       
                                width=300,
                                height=50,
                                placeholder_text="            D a t e  :  Y Y Y Y-M M-D D",
                                text_color= "#244c3c",
                                fg_color="#dcdcbb",
                                corner_radius=5,
                                bg_color="#716b55",
                                font=("Berlin Sans FB Demi", 15))
    q4.place(relx=0.55, rely=0.66, anchor=customtkinter.CENTER)

    addbutton = customtkinter.CTkButton(master=app2,
                                        command=validate_input,
                                        width=300,
                                        height=50,
                                        bg_color="#000000",
                                        fg_color='#244c3c',
                                        hover_color="#000000",
                                        text_color="#dcdcbb",
                                        font=("Berlin Sans FB Demi", 18,'bold'),
                                        corner_radius=5,
                                        border_width=7,
                                        border_color="#dcdcbb",
                                        text="submit")
    addbutton.place(relx=0.55, rely=0.79, anchor=customtkinter.CENTER)

    title_frame = customtkinter.CTkFrame(master=app2)
    title_frame.pack(side="bottom", fill="x")

    title_bar3 = customtkinter.CTkLabel(
        master=title_frame,
        text=''' B e w a r e    Of    L i t t l e    E x p e n s e s
    A   S m a l l   L e a k   W i l l   S i n k   A   G r e a t    S h i p ''',
        fg_color="#244c3c",
        height=70,
        text_color="#dcdcbb",
        font=("Berlin Sans FB Demi", 20, 'bold')
    )
    title_bar3.pack(fill="x")

    app2.mainloop()

def validate_input():
        given_name = q1.get()
        if not given_name.isalpha():
            messagebox.showerror("Error, NAME of transaction","Error name must only contain alphabets")
        transaction_type = q2.get().lower()
        if transaction_type not in ['income', 'expense']:
            messagebox.showerror("Error, TYPE of transaction","enter 'income' or 'expense'")
        
        transaction_amount = q3.get()
        if type(transaction_amount) != float:
            messagebox.showerror("Error, AMOUNT of transaction","invalid input")

        transaction_date = q4.get()
        year, month, day = map(int, transaction_date.split('-'))
        if not (1000 <= year <= 9999 and 1 <= month <= 12 and 1 <= day <= 31):
            messagebox.showerror("Error, DATE of transaction","Enter a VALID DATE")

        print(f"{transaction_amount,transaction_date,transaction_type}")

add_transaction_face()
