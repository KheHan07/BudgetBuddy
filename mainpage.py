import customtkinter
from PIL import Image, ImageTk

# Set appearance mode and default color theme
customtkinter.set_appearance_mode("dark")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green



# Create a CTk window instance
app = customtkinter.CTk()
app.geometry("1000x700")
app.title("Your Finance Tracker")

image = Image.open("vecteezy_hundred-dollar-bills-on-wooden-floor-3d-render_33692798.jpg")  # Replace "background.jpg" with your image file

# Resize the image to match the window dimensions
image = image.resize((2000, 1000))

# Convert the image to a format that tkinter can use
photo = ImageTk.PhotoImage(image)

# Set the window background to the image
background_label = customtkinter.CTkLabel(app, image=photo,text="")
background_label.place(x=0, y=0, relwidth=1, relheight=1)  # Fill the entire window with the label
background_label.image = photo  # Keep a reference to the image to prevent garbage collection


title_bar1 = customtkinter.CTkLabel(master=app, text="💲  Y O U R    P E R S O N A L    F I N A N C E    M A N A G E R  💲",
                                     fg_color="#dcdcbb", 
                                     height=70,
                                     text_color="#2c345c",font=("Berlin Sans FB Demi", 23, "bold"))
title_bar1.pack(fill="x")
title_bar2 = customtkinter.CTkLabel(master=app, text='"  T H E   A R T   I S   N O T   M A K I N G   M O N E Y  ,   B U T   I N   M A N A G I N G   I T  !  "',
                                     fg_color="#425e6a", 
                                     height=50,
                                     text_color="#dcdcbb",font=("Berlin Sans FB Demi", 16,'bold'))
title_bar2.pack(fill="x")



def button_function():
    print("Button pressed")

# Set the window icon with a PNG image (may not work on all systems)
app.iconbitmap("images.ico")  # Replace "your_icon.png" with the path to your PNG icon

# Use CTkButton instead of tkinter Button
button = customtkinter.CTkButton(master=app,
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
                                 command=button_function)
button.place(relx=0.25, rely=0.37, anchor=customtkinter.CENTER)


button2 = customtkinter.CTkButton(master=app,
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
                                 command=button_function)
button2.place(relx=0.5, rely=0.37, anchor=customtkinter.CENTER)

# Create Button 3
button3 = customtkinter.CTkButton(master=app,
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
                                 command=button_function)
button3.place(relx=0.75, rely=0.37, anchor=customtkinter.CENTER)

# Create Button 4
button4 = customtkinter.CTkButton(master=app, 
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
                                 command=button_function)
button4.place(relx=0.25, rely=0.52, anchor=customtkinter.CENTER)

# Create Button 5
button5 = customtkinter.CTkButton(master=app, 
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
                                 command=button_function)
button5.place(relx=0.5, rely=0.52, anchor=customtkinter.CENTER)

# Create Button 6
button6 = customtkinter.CTkButton(master=app, 
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

button7 = customtkinter.CTkButton(master=app,
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

title_frame = customtkinter.CTkFrame(master=app)
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

# Adjust any additional styling for the title_frame if needed

app.mainloop()
