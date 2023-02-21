from tkinter import *
from tkinter import filedialog
from PIL import Image
import os
import tkinter.messagebox as mbox

root = Tk()

# Function to crop all images in a folder
def crop_images():
    # Open the folder dialog and get the folder path
    folder_path = filedialog.askdirectory()
    
    # Iterate over all files in the folder
    for filename in os.listdir(folder_path):
        if filename.lower().endswith((".jpg", ".png", ".jpeg", ".JPG")):
            # Open the image file
            img_path = os.path.join(folder_path, filename)
            try:
                img = Image.open(img_path)
            except:
                print(f"Error opening file: {img_path}")
                continue
            
            # Calculate the dimensions of the cropped image
            width, height = img.size
            left = 12
            top = 12
            right = width - 12
            bottom = height - 12
            print(f"Cropping image: {img_path}")
            
            # Crop the image
            cropped_img = img.crop((left, top, right, bottom))
            
            # Save the cropped image with a new file name
            cropped_file_path = os.path.join(folder_path, "cropped_" + filename)
            try:
                cropped_img.save(cropped_file_path)
            except:
                print(f"Error saving file: {cropped_file_path}")
                continue
            
            print(f"Saved cropped image as: {cropped_file_path}")
    
    # Display a pop-up message when done
    mbox.showinfo("Done", "All images have been cropped!")

# Create the GUI
root.title("Image Folder Cropper")
root.geometry("300x100")
button = Button(root, text="Select Folder", command=crop_images)
button.pack(pady=20)

root.mainloop()
