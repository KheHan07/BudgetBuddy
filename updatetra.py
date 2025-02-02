import customtkinter
from PIL import Image, ImageTk

# Set appearance mode and default color theme
customtkinter.set_appearance_mode("dark")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green



# Create a CTk window instance
appo = customtkinter.CTk()
appo.geometry("1366x768")
appo.title("Your Finance Tracker")

image = Image.open("vecteezy_hundred-dollar-bills-on-wooden-floor-3d-render_33692798.jpg")  # Replace "background.jpg" with your image file

# Resize the image to match the window dimensions
image = image.resize((2000, 1000))

# Convert the image to a format that tkinter can use
photo = ImageTk.PhotoImage(image)

# Set the window background to the image
background_label = customtkinter.CTkLabel(appo, image=photo,text="")
background_label.place(x=0, y=0, relwidth=1, relheight=1)  # Fill the entire window with the label
background_label.image = photo  # Keep a reference to the image to prevent garbage collection


title_bar1 = customtkinter.CTkLabel(master=appo, text="💲  Y O U R    P E R S O N A L    F I N A N C E    M A N A G E R  💲",
                                     fg_color="#dcdcbb", 
                                     height=70,
                                     text_color="#2c345c",font=("Berlin Sans FB Demi", 23, "bold"))
title_bar1.pack(fill="x")
title_bar2 = customtkinter.CTkLabel(master=appo, text='"  T H E   A R T   I S   N O T   M A K I N G   M O N E Y  ,   B U T   I N   M A N A G I N G   I T  !  "',
                                     fg_color="#425e6a", 
                                     height=50,
                                     text_color="#dcdcbb",font=("Berlin Sans FB Demi", 16,'bold'))
title_bar2.pack(fill="x")

title_frame = customtkinter.CTkFrame(master=appo)
title_frame.pack(side="bottom", fill="x")

title_bar3 = customtkinter.CTkLabel(
    master=title_frame,
    text='"  S A V E   M O N E Y   A N D   M O N E Y   W I L L   S A V E   Y O U  "',
    fg_color="#244c3c",
    height=70,
    text_color="#dcdcbb",
    font=("Berlin Sans FB Demi", 20, 'bold')
)
title_bar3.pack(fill="x")

updatetransaction = customtkinter.CTkLabel(master=appo,
                                            width=220,
                                            height=50, 
                                            text="Enter the category of the transaction",
                                            text_color= "#244c3c",
                                            fg_color="#dcdcbb",
                                            corner_radius=5,
                                            bg_color="#716b55",
                                            font=("Berlin Sans FB Demi", 18,'bold'))
updatetransaction.place(relx=0.25, rely=0.27, anchor=customtkinter.CENTER)

textupdate = customtkinter.CTkEntry(master=appo,                                       
                                width=350,
                                height=50,
                                placeholder_text="            Enter the category name",
                                text_color= "#244c3c",
                                fg_color="#dcdcbb",
                                corner_radius=5,
                                bg_color="#716b55",
                                font=("Berlin Sans FB Demi", 15))
textupdate.place(relx=0.5, rely=0.27, anchor=customtkinter.CENTER)

appo.iconbitmap("images.ico")  # Replace "your_icon.png" with the path to your PNG icon

appo.mainloop()

