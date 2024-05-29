import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import os
from PIL import Image
from datetime import datetime
import shutil

def select_folder():
    folder_path = filedialog.askdirectory()
    if folder_path:
        folder_label.config(text=folder_path)
        organize_images_btn.config(state="normal")

def organize_images():
    folder_path = folder_label.cget("text")
    if not folder_path:
        messagebox.showerror("Error", "Please select a folder")
        return

    for current_file in os.listdir(folder_path):
        file_path = os.path.join(folder_path, current_file)
        if os.path.isfile(file_path):
            creation_date = None
            try:
                with Image.open(file_path) as image:
                    exif_data = image._getexif()
                    if exif_data:
                        creation_date = exif_data.get(36867)
                        if creation_date:
                            date_object = datetime.strptime(creation_date, "%Y:%m:%d %H:%M:%S")
                            year_month = date_object.strftime("%Y/%m")
                        else:
                            raise ValueError("No creation date found")
                    else:
                        raise ValueError("No EXIF data found")
            except Exception as e:
                print(f"Error processing file {current_file}: {e}")

            if not creation_date:
                # Use the last modified date as fallback
                mod_time = os.path.getmtime(file_path)
                date_object = datetime.fromtimestamp(mod_time)
                year_month = date_object.strftime("%Y/%m")

            target_folder = os.path.join(folder_path, year_month)
            if not os.path.exists(target_folder):
                os.makedirs(target_folder)
            try:
                shutil.move(file_path, target_folder)
                print(f"Moved file {current_file} to {target_folder}")
            except Exception as e:
                print(f"Error moving file {current_file}: {e}")

    messagebox.showinfo("Success", "Images have been organized successfully")

root = tk.Tk()
root.title("Image Organizer")
root.geometry("300x250")

select_folder_btn = tk.Button(root, text="Select Folder", command=select_folder)
select_folder_btn.pack(pady=20, padx=20)

folder_label = tk.Label(root, text="", wraplength=400)
folder_label.pack(pady=10, padx=10)

organize_images_btn = tk.Button(root, text="Organize Images", state="disabled", command=organize_images)
organize_images_btn.pack(pady=20,padx=20)

root.mainloop()
