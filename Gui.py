import tkinter as tk

# Define a function to open a new window
def open_encryption_mode_window():
    # Create a new window
    encryption_mode_window = tk.Toplevel(root)
    encryption_mode_window.title("Encryption Mode")

    encryption_mode_window.state('zoomed')
    # Add a label and a button to the new window
    label = tk.Label(encryption_mode_window, text="")
    label.pack()

    DesButton = tk.Button(encryption_mode_window, text="DES", command=open_DES_window,width=20, height=5,bg='red')
    DesButton.pack()
    AesButton = tk.Button(encryption_mode_window, text="AES", command="",width=20, height=5,bg='red')
    AesButton.pack()







def open_DES_window():
    # Create a new window
    DES_window = tk.Toplevel(root)
    DES_window.title("DES Mode")





    # DesButton = tk.Button(DES_window, text="DES", command="",width=20, height=5,bg='red')
    # DesButton.pack()
    # Add a text box to display the chat messages

# Initialize the main GUI window and maximize it
root = tk.Tk()
root.state('zoomed')
root.title("GraphicalUserInterFace")

# # Add a text box to display the chat messages
# chat_text = tk.Text(root)
# chat_text.pack()




# Add a button to open a new window for single key
SingleKeyButton = tk.Button(root, text="SingleKey", command=open_encryption_mode_window, width=20, height=5,bg='red')
SingleKeyButton.pack()

# Add a button to open a new window for two keys
TwoKeysButton = tk.Button(root, text="TwoKeys", command="", width=20, height=5,bg='red')
TwoKeysButton.pack()






# Start the GUI main loop
root.mainloop()



