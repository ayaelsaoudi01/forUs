import PySimpleGUI as sg
import os
from PIL import Image
import SimpleITK as sitk

def convert():
    # Get the list of files to convert
    files = sg.PopupGetFile('Select files to convert', no_window=True, multiple_files=True)
    # If no files were selected, exit
    if not files:
        return
    # Get the output directory
    output_dir = sg.PopupGetFolder('Select output directory', no_window=True)
    # If no output directory was selected, exit
    if not output_dir:
        return
    # Loop through the files
    for file in files:
        # Get the filename
        filename = os.path.basename(file)
        # Get the file extension
        ext = os.path.splitext(filename)[1]
        # If the file is not a jpg, skip it
        if ext != '.jpg':
            continue
        # Convert the jpg file to nii format
        img = sitk.ReadImage(file)
        sitk.WriteImage(img, os.path.join(output_dir, os.path.splitext(filename)[0] + '.nii'))
    # Show a message
    sg.Popup('Conversion complete')

# Define the GUI layout
layout = [
    [sg.Text('JPG to NII Converter')],
    [sg.Button('Convert', key='convert', bind_return_key=True)],
    [sg.Exit()]
]

# Create the window
window = sg.Window('JPG to NII Converter', layout)

# Event loop
while True:
    event, values = window.read()
    if event == 'convert':
        convert()
    elif event in (None, 'Exit'):
        break

# Close the window
window.close()