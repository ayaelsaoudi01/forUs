import os
from PIL import Image
from collections import defaultdict
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

root = tk.Tk()

def browse_button():
    global path
    path = filedialog.askdirectory()
    path_label.config(text=path)

def show_duplicates():
    if not path:
        messagebox.showwarning("Warning", "Please select a folder first.")
        return
    
    image_dict = defaultdict(list)
    result_text.delete('1.0', tk.END)
    duplicate_files = []
    for file_name in os.listdir(path):
        if file_name.endswith('.jpg') or file_name.endswith('.jpeg') or file_name.endswith('.png'):
            img = Image.open(os.path.join(path, file_name))
            img_hash = hash(img.tobytes())
            image_dict[img_hash].append(file_name)

    for img_hash, file_names in image_dict.items():
        if len(file_names) > 1:
            result_text.insert(tk.END, "Duplicate images with hash value %s:\n" % img_hash)
            for file_name in file_names:
                duplicate_files.append(file_name)
                result_text.insert(tk.END, "- %s\n" % file_name)

    if not duplicate_files:
        result_text.insert(tk.END, "No duplicate images found.")
        
def delete_duplicates():
    if not path:
        messagebox.showwarning("Warning", "Please select a folder first.")
        return
    
    image_dict = defaultdict(list)
    result_text.delete('1.0', tk.END)
    deleted_files = []
    for file_name in os.listdir(path):
        if file_name.endswith('.jpg') or file_name.endswith('.jpeg') or file_name.endswith('.png') or file_name.endswith('.JPG'):
            img = Image.open(os.path.join(path, file_name))
            img_hash = hash(img.tobytes())
            image_dict[img_hash].append(file_name)

    for img_hash, file_names in image_dict.items():
        if len(file_names) > 1:
            result_text.insert(tk.END, "Deleting duplicate images with hash value %s:\n" % img_hash)
            for file_name in file_names[1:]:
                deleted_files.append(file_name)
                os.remove(os.path.join(path, file_name))
                result_text.insert(tk.END, "- %s\n" % file_name)

    if not deleted_files:
        result_text.insert(tk.END, "No duplicate images found.")
    else:
        result_text.insert(tk.END, "Deleted files:\n")
        for file_name in deleted_files:
            result_text.insert(tk.END, "- %s\n" % file_name)

path = ""
path_label = tk.Label(root, text="")
path_label.pack()

browse_button = tk.Button(text="Browse", command=browse_button)
browse_button.pack()

show_duplicates_button = tk.Button(text="Show Duplicates", command=show_duplicates)
show_duplicates_button.pack()

process_duplicates_button = tk.Button(text="Process Duplicates", command=lambda: [show_duplicates(), delete_duplicates()])
process_duplicates_button.pack()

result_text = tk.Text(root)
result_text.pack()

root.mainloop()
