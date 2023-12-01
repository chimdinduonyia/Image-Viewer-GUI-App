from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog

root = Tk()
root.title("Image Viewer 2.0")

#List to store images
image_list = []

#List to store image file name/paths
name_list = []

#Serves as a pointer to which image to be displayed
index = 0

#Space for Image to be displayed
image_space = LabelFrame(root, text="Image Frame",
                         padx=50, pady=50, bd=2, relief=SUNKEN)
image_space.grid(row=2, column=2, pady=20)

#Label for image within image space
image_label = Label(image_space, text="Images Here", anchor=CENTER)
image_label.grid(row=0, column=0)

#Functions

#Function for select images button
def select_image():

    global image_list
    global name_list

    #the filetypes to be accepted and passed into the filetypes attribute
    filetypes = (
        ("png files", "*.png"),
        ("jpg files", "*.jpg"),
        ("All files", "*.*")
    )
    #Provides dialog and casts selections to a tuple which is stored as the variable filename
    filename = filedialog.askopenfilenames(title="Select Images",
                                           initialdir="./Images", filetypes=filetypes)
    #Iterate through filename, check if there are duplicates by comparing paths to the name_list and add images to image_list
    for file in filename:
        if file not in name_list:
            name_list.append(file)
            image_list.append(ImageTk.PhotoImage(
                Image.open(file).resize((200, 200), Image.ANTIALIAS)))
        else:
            pass
    #Place first image in the image_list in the image space
    image_label = Label(image_space, image=image_list[0], anchor=CENTER)
    image_label.grid(row=0, column=0)

    #Checks if there are any images, before displaying the navigation buttons
    if len(image_list) >= 1:
        forward_button.grid(row=2, column=3, padx=20, sticky=W+E)
        backward_button.grid(row=2, column=1, padx=20, sticky=W+E)
        exit_button.grid(row=3, column=2, padx=20, pady=20, sticky=W+E)
        status = Label(root, text=f"Image {index+1} of {len(image_list)}", anchor=CENTER, relief=SUNKEN)
        status.grid(row=4, column=0, columnspan=5, sticky=W+E)

#Functions for the forward and backwards buttons
def forward():

    global image_list
    global index
    global image_label
    global status

    if index == len(image_list) - 1:
        index = 0
        image_label = Label(
            image_space, image=image_list[index], anchor=CENTER)
        image_label.grid(row=0, column=0)
        status = Label(
            root, text=f"Image {index+1} of {len(image_list)}", anchor=CENTER, relief=SUNKEN)
        status.grid(row=4, column=0, columnspan=5, sticky=W+E)
    else:
        image_label.grid_forget()
        index += 1
        image_label = Label(
            image_space, image=image_list[index], anchor=CENTER)
        image_label.grid(row=0, column=0)
        status = Label(
            root, text=f"Image {index+1} of {len(image_list)}", anchor=CENTER, relief=SUNKEN)
        status.grid(row=4, column=0, columnspan=5, sticky=W+E)


def backward():

    global image_list
    global index
    global image_label
    global status

    if index <= 0:
        index = len(image_list) - 1
        image_label = Label(
            image_space, image=image_list[index], anchor=CENTER)
        image_label.grid(row=0, column=0)
        status = Label(
            root, text=f"Image {index+1} of {len(image_list)}", anchor=CENTER, relief=SUNKEN)
        status.grid(row=4, column=0, columnspan=5, sticky=W+E)
    else:
        image_label.grid_forget()
        index -= 1
        image_label = Label(
            image_space, image=image_list[index], anchor=CENTER)
        image_label.grid(row=0, column=0)
        status = Label(
            root, text=f"Image {index+1} of {len(image_list)}", anchor=CENTER, relief=SUNKEN)
        status.grid(row=4, column=0, columnspan=5, sticky=W+E)


# Buttons
# The Select files button
select = Button(root, text="Select File(s)", padx=50, command=select_image)
select.grid(row=1, column=2, sticky=W+E, pady=20)

# Instantiate navigation buttons
forward_button = Button(root, text=">>", command=forward)
backward_button = Button(root, text="<<", command=backward)
exit_button = Button(root, text="Exit", command=root.quit)

root.mainloop()
