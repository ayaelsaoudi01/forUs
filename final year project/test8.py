#Smoothing: MRI images can have a high level of noise, which can affect the analysis. 
#Therefore, smoothing is performed to reduce the noise and enhance the signal-to-noise ratio.
import os
import subprocess
import tkinter as tk
from tkinter import filedialog

# Define the function to perform image smoothing
def smooth_image(input_file, output_file, fwhm):
    # Define the input and output file paths
    input_path = os.path.join(input_dir, input_file)
    output_path = os.path.join(output_dir, output_file)

    # Use FSL's SUSAN to perform image smoothing
    susan_cmd = f"susan {input_path} {fwhm} -mean {output_path}"
    subprocess.call(susan_cmd, shell=True)

# Create a Tkinter GUI window
window = tk.Tk()

# Define the input and output directories using a file dialog
input_file = filedialog.askopenfilename(title="Select input file")
output_file = filedialog.asksaveasfilename(title="Select output file", defaultextension=".nii.gz")
fwhm = input("Enter the FWHM value for smoothing (in mm): ")

# Define the input and output file paths
input_dir, input_filename = os.path.split(input_file)
output_dir, output_filename = os.path.split(output_file)

# Perform image smoothing on the input file
smooth_image(input_filename, output_filename, fwhm)

# Show a message box when the processing is complete
tk.messagebox.showinfo("Processing complete", "Image smoothing is complete.")

# Close the window
window.destroy()
