#!/usr/bin/env python
# coding: utf-8

# In[2]:


1.1
#IMPORTS---------------------------------------------------------------------------------------------
from PIL import Image, ImageTk
from tkinter import filedialog, messagebox, Tk, Button, Label, Menu, Text, simpledialog, Scrollbar, Listbox, Frame,ttk
import os
import tkinter as tk
import shutil
import cv2
import numpy as np
import time
from time import sleep

#FUNCTIONS--------------------------------------------------------------------------------------------

# Function to update the console with progress or information
def update_console(message):
    console_text.insert("end", message + "\n")
    console_text.see("end")  
    root.update_idletasks() 

# Function to clean the console
def clear_console():
    console_text.delete("1.0", tk.END)

#to sharp bluriness of the stitching
def sharpen():
    ask_file = filedialog.askopenfilename()
    print(ask_file)
    save_dir = os.path.dirname(ask_file)
    
    if ask_file == "":
        print("nothing selected")
        update_console("No files selected")
    else:
        #os.chdir(ask_file)
        
        # Load the image
        image = cv2.imread(ask_file)

        # Define the sharpening kernel
        kernel = np.array([[0, -1, 0], [-1,5.2, -1], [0, -1, 0]])

        # Apply the filter
        sharpened = cv2.filter2D(image, -1, kernel)

        # Save the sharpened image
        past_name = os.path.basename(ask_file)
        base_name, extension = os.path.splitext(past_name)
        cv2.imwrite(os.path.join(save_dir, f"{base_name}_sharpened.tif"),sharpened)

        update_console("Sharpening process completed. The image has been  saved in the same folder as the original (.tif).  Refresh the folder.")
        messagebox.showinfo(title=None, message="Your image have been successfully changed")

   
    
# Stitching function
def stitch():
    stitcher = cv2.Stitcher_create(mode=1)
    image_paths = []
    imgs = []
    final = []
    d = 0

    directory = filedialog.askdirectory()
    if directory == "":
        print("nothing selected")
        update_console("No files selected")
    else:
        os.chdir(directory)
    
        for x in sorted(os.listdir(os.getcwd()), key=len):
            if x.endswith(".jpg") or x.endswith(".tif"):
                image_paths.append(x)


        print(image_paths)
        update_console("Starting stitching process...")


        for i in range(len(image_paths)):
            imgs.append(cv2.imread(image_paths[i]))

            if i > 0:
                (A, result) = stitcher.stitch(imgs)

                if A != cv2.Stitcher_OK:
                    print("Error: Image stitching failed")
                    update_console("Image stitching failed, your image have a problem")

                else:
                    final.append(result)
                    update_console(f"Image {i+1} stitched successfully")
                    sleep(1)

        current_directory = os.getcwd()
        folder_name = os.path.basename(current_directory)
        new_filename = f"{folder_name}_stitched.tif"
        cv2.imwrite(new_filename, result)


        update_console("Stitching complete. Image saved as (.tif) in your folder. Refresh the folder.")
        messagebox.showinfo(title=None, message="Your images have been successfully stitched")

# Resizing function
def resize():
    resize_path = []
    resize_imgs = []

    
    directory = filedialog.askdirectory()
    if directory == "":
        print("nothing selected")
        update_console("No files selected")
    else:
        os.chdir(directory)
        sleep(2)
        folder_name = os.path.basename(directory)
        resize_folder = f"{folder_name}_Resized images"
        os.mkdir(resize_folder)
        

        for x in sorted(os.listdir(os.getcwd()), key=len):
            if x.endswith(".jpg") or x.endswith(".tif"):
                resize_path.append(x)
        print(resize_path)

        fx = simpledialog.askfloat("Resize", "Enter the value of fx (scaling factor for width 0-1):", minvalue=0.0)
        fy = simpledialog.askfloat("Resize", "Enter the value of fy (scaling factor for height 0-1):", minvalue=0.0)
        update_console("Starting resizing process...")
        for i in range(len(resize_path)):
            resize_imgs.append(cv2.imread(resize_path[i]))
            resized_img = cv2.resize(resize_imgs[i], None, fx=fx, fy=fy)

            filename, extension = os.path.splitext(resize_path[i])
            new_filename = f"{filename}_resized{extension}"
            cv2.imwrite(new_filename, resized_img)
            source_path = os.path.join(directory, new_filename)
            destination_path = os.path.join(directory, resize_folder)
            shutil.move(source_path, destination_path)
            update_console(f"Image {i+1} resized successfully")
            sleep(1)
            

        update_console("Resizing process completed, resized images saved  in your folder. Refresh the folder.")
        messagebox.showinfo(title=None, message="Your images have been successfully resized")
    

# Instructions function
def instructions():
    os.chdir(program_directory)
    try:
        with open("instructions.txt", "r") as file:
            content = file.read()
            popup = tk.Toplevel(root)  # Create a popup window
            popup.title("How to use")
            popup.iconphoto(False, icono_p, icono_p)
            text_widget = tk.Text(popup, wrap=tk.WORD)
            text_widget.pack()
            text_widget.insert(tk.END, content)
    except FileNotFoundError:
        popup = tk.Toplevel(root)
        popup.title("How to use")
        text_widget = tk.Text(popup, wrap=tk.WORD)
        text_widget.pack()
        text_widget.insert(tk.END, "File not found")
    


# Icon attribution function
def icon_atr():
    os.chdir(program_directory)
    os.system("attributions.pdf")
    
# License function
def license():
    os.chdir(program_directory)
    os.system("license.pdf")


#--------------------------------------------------------------------------------------------------    
#INTERFACE----------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------

# Create the root window
root = Tk()
root.title('JOIN Software v1')
root.geometry("1000x640")
root.configure(bg="White")

#Logo
icono_p = tk.PhotoImage(file="Media/sharpen.png")
root.iconphoto(False, icono_p, icono_p)

# Create a console-like frame for stitching progress
console_frame = Label(root, width=60, height=30, relief="solid", borderwidth=1,
                      highlightthickness=10.5, bg="white")
console_frame.pack()
console_frame.place(x=500, y=70)


# Create a text box for displaying progress or information
console_text = Text(root, width=50, height=23)
console_text.pack()
console_text.place(x=520, y=100)


# Create a menu bar
menu_bar = Menu(root)
root.config(menu=menu_bar)

# Create the 'Options' dropdown menu
options_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label='Options', menu=options_menu)

# Create a File menu with a dropdown option
options_menu.add_command(label='Stitch', font=("Open Sans", 10),command=stitch)
options_menu.add_command(label='Resize', font=("Open Sans", 10),command=resize)
options_menu.add_command(label='Sharp', font=("Open Sans", 10),command=sharpen)

doc_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label='Documentation', menu=doc_menu, font=("Open Sans",10))
doc_menu.add_command(label='How to use', font=("Open Sans", 10),command=instructions)
doc_menu.add_command(label='Author and attributions', font=("Open Sans", 10),command=icon_atr)
doc_menu.add_command(label='License', font=("Open Sans", 10),command=license)



# Create buttons for 
#stitching
picture_image = Image.open("Media/stitch.png")
picture_image = picture_image.resize((100, 100), Image.ANTIALIAS)
picture_photo = ImageTk.PhotoImage(picture_image)
button_stitch = Button(root, image=picture_photo, bg="white", command=stitch)
button_stitch.pack()
button_stitch.place(x=115, y=110)

#resize
info_image = Image.open("Media/resize.png")
info_image = info_image.resize((100, 100), Image.ANTIALIAS)
info_photo = ImageTk.PhotoImage(info_image)
button_instructions = Button(root, image=info_photo, bg="white", command=resize)
button_instructions.pack()
button_instructions.place(x=115, y=240)

#sharpen
resize_image = Image.open("Media/sharpen.png")
resize_image = resize_image.resize((100, 100), Image.ANTIALIAS)
resize_photo = ImageTk.PhotoImage(resize_image)
button_resize = Button(root, image=resize_photo, bg="white", command=sharpen)
button_resize.pack()
button_resize.place(x=115, y=370)

#instructions
atr_image = Image.open("Media/planificacion.png")
atr_image = atr_image.resize((40, 40), Image.ANTIALIAS)
atr_photo = ImageTk.PhotoImage(atr_image)
button_atr = Button(root, image=atr_photo, bg="white",command=instructions)
button_atr.pack()
button_atr.place(x=900, y=10)

#clear
cl_image = Image.open("Media/clean.png")
cl_image = cl_image.resize((40, 40), Image.ANTIALIAS)
cl_photo = ImageTk.PhotoImage(cl_image)
button_cl = Button(root, image=cl_photo, bg="white", command=clear_console)
button_cl.pack()
button_cl.place(x=840, y=10)


#Create explanation for stitch button

text_stitch = Label(root, text="Combine multiple images to produce a panoramic image or a \nhigh-resolution image",bg="white", fg="black", font=("Open Sans", 10), wraplength=220)
text_stitch.pack()
text_stitch.place(x=230, y=125)

#Create explanation for resize button
text_stitch = Label(root, text="Change the size of your images choosing a suitable\n scaling factor", bg="white", fg="black", font=("Open Sans", 10),wraplength=200)
text_stitch.pack()
text_stitch.place(x=230, y=255)

#Create explanation for sharpen button
text_stitch = Label(root, text="Sharpen the details of your image", bg="white", fg="black", font=("Open Sans", 10), wraplength=220)
text_stitch.pack()
text_stitch.place(x=230, y=405)

#Create text for copyright
text_copyright = Label(root, text=" Creative Commons Copyright License Attribution 4.0 International",bg="white", fg="black", font=("Open Sans", 6))
text_copyright.pack()
text_copyright.place(x=695, y=580)

#set program directory
program_directory = os.getcwd()
print(program_directory)

# Start the GUI event loop
root.mainloop()

