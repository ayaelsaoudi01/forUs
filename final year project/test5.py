import os
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image

class BatchImageResizer:
    def __init__(self, master):
        self.master = master
        master.title("Batch Image Resizer")

        self.folder_path = None

        # Create buttons
        self.select_button = Button(master, text="Select Folder", command=self.select_folder)
        self.resize_button = Button(master, text="Resize Images", command=self.resize_images, state=DISABLED)

        # Position widgets
        self.select_button.pack(side=TOP, pady=10)
        self.resize_button.pack(side=BOTTOM, pady=10)

    def select_folder(self):
        # Open a file dialog to select a folder containing image files
        self.folder_path = filedialog.askdirectory()
        if self.folder_path:
            # Enable the resize button
            self.resize_button.config(state=NORMAL)

    def resize_images(self):
        if self.folder_path:
            # Get a list of image files in the selected folder
            image_files = [f for f in os.listdir(self.folder_path) if f.endswith('.jpg') or f.endswith('.png') or f.endswith('.JPG') or f.endswith('.jpeg')]

            # Resize each image and save it in the same folder with "_resized" appended to the filename
            for image_file in image_files:
                # Open the original image and resize it
                original_image_path = os.path.join(self.folder_path, image_file)
                original_image = Image.open(original_image_path)
                resized_image = original_image.resize((256, 256))

                # Convert the image to RGB mode
                resized_image = resized_image.convert('RGB')

                # Save the resized image
                resized_image_path = os.path.join(self.folder_path, image_file.split('.')[0] + '_resized.' + image_file.split('.')[1])
                resized_image.save(resized_image_path)

                # Save the resized image with 300 dpi resolution
                resized_image_path = os.path.join(self.folder_path, image_file.split('.')[0] + '_resized.' + image_file.split('.')[1])
                resized_image.save(resized_image_path, dpi=(300, 300))


                # Delete the original image
                os.remove(original_image_path)

            # Show a message box to indicate success
            message = f"All images in {self.folder_path} have been resized."
            messagebox.showinfo("Resize Images", message)


root = Tk()
resizer = BatchImageResizer(root)
root.mainloop()
