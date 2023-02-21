from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image

def detect_rotation(image_path_1, image_path_2):
    image_1 = Image.open(image_path_1)
    image_2 = Image.open(image_path_2)
    
    # check rotation direction and return result
    # ...

def check_rotation_direction():
    # create a Tkinter window
    root = Tk()
    root.withdraw()

    # ask the user to select the two image files to compare
    file_path_1 = filedialog.askopenfilename(title="Select image file 1", filetypes=[("JPEG files", "*.jpg")])
    file_path_2 = filedialog.askopenfilename(title="Select image file 2", filetypes=[("JPEG files", "*.jpg")])

    if file_path_1 and file_path_2:
        # check if the images have the same rotation direction
        result = detect_rotation(file_path_1, file_path_2)

        # show a message box with the result
        if result:
            messagebox.showinfo("Rotation direction", "The images have the same rotation direction.")
        else:
            messagebox.showinfo("Rotation direction", "The images have different rotation directions.")
    else:
        # show an error message if the user didn't select both files
        messagebox.showerror("Error", "Please select two image files.")

check_rotation_direction()
