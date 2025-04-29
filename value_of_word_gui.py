import re
import customtkinter as ctk


# variable to keep track of history
counter = 0


# the function to run after  hitting submit
def display_value():
    # making coounter editable and adding 1 each time
    global counter
    counter += 1

    # takes the value from input -> strips it -> lowers all characters
    word = user_input.get().strip().lower()

    # variable to store the value
    value = 0

    # checks if the input is in correct format (e.g. a word)
    pattern = r"^[a-z]+$"
    if re.search(pattern, word):
        # calculates the value of the word using ASCII values
        for letter in word:
            value = value + (ord(letter) - 96)

        # create a labelon the scrollable frame and dhow the value
        result = str(counter) + ". " + word.capitalize() + " = " + str(value)
        label = ctk.CTkLabel(master=scrollable_frame, anchor="n", text=result)
        label.pack(anchor="w", padx=10)

        # empty the input field
        user_input.delete(0, "end")

    # if not then just returns(after emptying the input field)
    else:
        return   


# create the main window
ctk.set_appearance_mode("Dark")

root = ctk.CTk()
root.geometry("800x600")
root.title("Value of Words")

# title in the main window
title = ctk.CTkLabel(master=root, text="Value of Words",
                     font=("Arial", 24, "bold"), text_color="#1E90FF")
title.pack(pady=30)

# input field to get the word
user_input = ctk.CTkEntry(master=root, placeholder_text="Enter your word here")
user_input.pack(padx=20, pady=15, fill="x")

# submit button to take the word and calculate it's value and show it as a label
button = ctk.CTkButton(master=root, text="Check the value!", command=display_value,
                       fg_color="#2E8B57", hover_color="#3CB371", corner_radius=10)
button.pack(pady=20)

# making a scrollable frame to keep the values like history
scrollable_frame = ctk.CTkScrollableFrame(master=root, height=400, width=700)
scrollable_frame.pack()

history = ctk.CTkLabel(master=scrollable_frame, text="History:")
history.pack()


# creating a help button to explain the usage
def help():
    # creating the popup window
    help_window = ctk.CTkToplevel(master=root)
    help_window.geometry("600x400")
    help_window.title("Help & About")
    help_window.resizable(False, False)
    help_window.transient(master=root)
    help_window.grab_set()

    help_title = ctk.CTkLabel(master=help_window, text="Value of Words")
    help_title.pack(pady=20)

    # putting the text in the help window
    text = (
        "About: \n\n"
        "This application shows the value of a word by giving each English letter a numeric value.\n"
        "For example, a or A is 1 and b or B is 2 and so on, matching their order in alphabet.\n\n\n"

        "How to use:\n\n"
        "1. Put the word in the input field.\n"
        "2. Click 'Check the value!' and see the value.\n"
        "3. The previous checked words are available in history.\n"
    )
    help_label = ctk.CTkLabel(master=help_window, text=text, justify="left")
    help_label.pack()


# creating the help button
help_button = ctk.CTkButton(master=root, text="Help?", command=help)
help_button.place(relx=1.0, x=-10, y=10, anchor="ne")


# keep the main window running
root.mainloop()