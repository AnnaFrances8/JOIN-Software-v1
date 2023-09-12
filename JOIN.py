#!/usr/bin/env python
# coding: utf-8

# In[1]:


#pip install opencv-python


# In[7]:


#pip install rembg


# In[10]:


1.1
#IMPORTS---------------------------------------------------------------------------------------------
from PIL import Image, ImageTk
from tkinter import filedialog, messagebox, Tk, Button, Label, Menu, Text, simpledialog, Scrollbar, Listbox, Frame,ttk
import os
import tkinter as tk
import webbrowser
import shutil
import cv2
import numpy as np
import time
from time import sleep
from rembg import remove

#FUNCTIONS--------------------------------------------------------------------------------------------

# Function to update the console with progress or information
def update_console(message):
    console_text.insert("end", message + "\n")
    console_text.see("end")  
    root.update_idletasks() 

#to sharp bluriness of the stitching
def sharpen():
    ask_file = filedialog.askopenfilename()
    print(ask_file)
    
    # Load the image
    image = cv2.imread(ask_file)
    
    # Define the sharpening kernel
    kernel = np.array([[0, -1, 0], [-1,5.2, -1], [0, -1, 0]])
    
    # Apply the filter
    sharpened = cv2.filter2D(image, -1, kernel)
    
    # Save the sharpened image
    past_name = os.path.basename(ask_file)
    base_name, extension = os.path.splitext(past_name)
    
    cv2.imwrite(f"{base_name}_sharpened.tif", sharpened)
    update_console("Sharpening process completed. The image has been saved in the same folder as the original.")
    messagebox.showinfo(title=None, message="Your image have been successfully changed")

    
    
    
#background removal function
# Input paths
def background():

    input_path = filedialog.askopenfilename()
    output_path = "output.png"

    input_image = Image.open(input_path)
    update_console("Starting process...")

    # Convert the image to JPEG format, for some reason it works better
    image_array = cv2.imread(input_path, cv2.IMREAD_COLOR)
    jpeg_image_path = "temp.jpg"
    cv2.imwrite(jpeg_image_path, image_array, [int(cv2.IMWRITE_JPEG_QUALITY), 100])

    # Open the converted JPEG image
    jpeg_image = Image.open(jpeg_image_path)

    # Remove the background using rembg
    output_image_rgba = remove(jpeg_image)

    # Convert RGBA image to RGB mode
    output_image_rgb = output_image_rgba.convert("RGB")

    # Save the background-removed image as PNG, it works better if I change to tiff from png
    output_image_rgb.save(output_path, format="PNG")
    update_console("First output achieved")


    # Delete the temporary JPEG image
    os.remove(jpeg_image_path)
    
    
    #from png to tif
    file_name = os.path.basename(input_path)
    print(file_name)
    base_name, extension = os.path.splitext(file_name)
    if extension.lower() == ".jpg" or ".tif" or ".png" or ".jpeg":
        print(base_name)
    
    input_path2 =  "output.png"
    output_path2 = f"{base_name}_no_background.tif"

    # Processing the image
    input = Image.open(input_path2)

    # Removing the background from the given Image
    output = remove(input)

    #Saving the image in the given path
    output.save(output_path2)
    update_console("Second output achieved")
    #earease anything else
    os.remove(input_path2)
    
    update_console("Background removal complete. The image has been saved as a (.tif) file in the same folder as the original.")
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


        update_console("Stitching complete. Image saved as (.tif) in your folder")
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
            

        update_console("Resizing process completed, your resized images are saved in your folder (.jpg or .tif)")
        messagebox.showinfo(title=None, message="Your images have been successfully resized")
    

# Instructions function
def instructions():
    webbrowser.open("instructions.pdf")


# Icon attribution function
def icon_atr():
     webbrowser.open("attributions.pdf")


#--------------------------------------------------------------------------------------------------    
#INTERFICIE----------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------

# Create the root window
root = Tk()
root.title('JOIN Software 1.1')
root.geometry("1000x650")
root.configure(bg="White")

#Logo
icono_p = tk.PhotoImage(file="sharpen.png")
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


# Create the title of the console
#console_title = Label(root, width=10, height=1, bg="white", text="Console")
#console_title.pack()
#console_title.place(x=510, y=85)

# Create a menu bar
menu_bar = Menu(root)
root.config(menu=menu_bar)


# Create a menu bar
menu_bar = Menu(root)
root.config(menu=menu_bar)

# Create the 'Options' dropdown menu
options_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label='Options', menu=options_menu)

# Create a File menu with a dropdown option
options_menu.add_command(label='Stitch', command=stitch)
options_menu.add_command(label='Resize', command=resize)
options_menu.add_command(label='Background removal', command=background)
options_menu.add_command(label='Sharp', command=sharpen)


info_menu = Menu(menu_bar, tearoff=0)
author_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_command(label='How to use', command=instructions)
menu_bar.add_command(label='Author and attributions', command=icon_atr)


# Create buttons for 
#stitching
picture_image = Image.open("stitch.png")
picture_image = picture_image.resize((100, 100), Image.ANTIALIAS)
picture_photo = ImageTk.PhotoImage(picture_image)
button_stitch = Button(root, image=picture_photo, bg="white", command=stitch)
button_stitch.pack()
button_stitch.place(x=115, y=65)


#resize
info_image = Image.open("resize.png")
info_image = info_image.resize((100, 100), Image.ANTIALIAS)
info_photo = ImageTk.PhotoImage(info_image)
button_instructions = Button(root, image=info_photo, bg="white", command=resize)
button_instructions.pack()
button_instructions.place(x=115, y=185)

#background
atr_image = Image.open("removebackground.png")
atr_image = atr_image.resize((100, 100), Image.ANTIALIAS)
atr_photo = ImageTk.PhotoImage(atr_image)
button_atr = Button(root, image=atr_photo, bg="white", command=background)
button_atr.pack()
button_atr.place(x=115, y=305)

#sharpen
resize_image = Image.open("sharpen.png")
resize_image = resize_image.resize((100, 100), Image.ANTIALIAS)
resize_photo = ImageTk.PhotoImage(resize_image)
button_resize = Button(root, image=resize_photo, bg="white", command=sharpen)
button_resize.pack()
button_resize.place(x=115, y=425)

#Create explanation for stitch button

text_stitch = Label(root, text="Combine multiple images to produce a panoramic image or a \nhigh-resolution image",bg="white", fg="black", font=("Arial", 10), wraplength=220)
text_stitch.pack()
text_stitch.place(x=230, y=85)

#Create explanation for resize button
text_stitch = Label(root, text="Change the size of your images choosing a suitable\n scaling factor", bg="white", fg="black", font=("Arial", 10),wraplength=200)
text_stitch.pack()
text_stitch.place(x=230, y=205)

#Create explanation for instructions button
text_stitch = Label(root, text=" Remove the background of your image", bg="white", fg="black", font=("Arial", 10), wraplength=220, anchor="center")
text_stitch.pack()
text_stitch.place(x=230, y=325)

#Create explanation for atribution button
text_stitch = Label(root, text="Sharpen the details of your image", bg="white", fg="black", font=("Arial", 10), wraplength=220)
text_stitch.pack()
text_stitch.place(x=230, y=445)


# Start the GUI event loop
root.mainloop()

