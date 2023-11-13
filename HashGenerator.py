import hashlib

#Hashlibrary is the library which Have the function in python to check the hash of the Input value, over here we are going to see multiple options and also in 
#GUI version so It's easy to use, We will be creating the Application which will help us in Maintaining the INTEGRITY The most important CIA in cyber security.

import tkinter as tk

# here tkintertkinter is the standard GUI toolkit that comes with Python. It provides a set of tools and widgets for creating graphical user interfaces. 
# To use tkinter, you need to have Python installed on your system, as it is part of the standard library.

from tkinter import Label, Entry, Button, StringVar, OptionMenu

#here for label,entry,Button,Stringver And the OptionMenu For the Same.
# Now let's Create a Function for Multiple Options and to Calculate the Hash Value of the Same.
def calculate_hash():
    message = entry_value.get()
    algorithm = algorithm_var.get()

    if algorithm == "SHA256":
        hash_object = hashlib.sha256(message.encode())
    elif algorithm == "SHA1":
        hash_object = hashlib.sha1(message.encode())
    elif algorithm == "SHA512":
        hash_object = hashlib.sha512(message.encode())
    elif algorithm == "MD5":
        hash_object = hashlib.md5(message.encode())
    elif algorithm == "MD4":
        # MD4 is not directly supported in hashlib, you can use an external library
        # or implement MD4 manually if needed
        result_label.config(text="MD4 not supported")
        return
    else:
        result_label.config(text="Invalid algorithm")
        return

    hash_hex = hash_object.hexdigest()
    result_label.config(text=f"{algorithm} hash value: {hash_hex}")

# GUI setup , Over here  GUI Setup  We will give title Which Mean Hash Calulator, as a title.
root = tk.Tk()
root.title("Hash Calculator")

label_instruction = Label(root, text="Enter a value:") #Input Value
label_instruction.pack(pady=10)

entry_value = Entry(root)
entry_value.pack(pady=10)

algorithm_var = StringVar()
algorithm_var.set("SHA256")  # Default algorithm SHA256 We will be Keeping.

algorithm_label = Label(root, text="Select hash algorithm:")
algorithm_label.pack(pady=5)

algorithm_options = ["SHA256", "SHA1", "SHA512", "MD5", "MD4"] #Four Options We are GIVING Because MD4 is not supported.
algorithm_menu = OptionMenu(root, algorithm_var, *algorithm_options)
algorithm_menu.pack(pady=10)

calculate_button = Button(root, text="Calculate Hash", command=calculate_hash)
calculate_button.pack(pady=10)

result_label = Label(root, text="")
result_label.pack(pady=10)

root.mainloop()

# Hence we will save this and then We will generate the EXE file For the SAME.


