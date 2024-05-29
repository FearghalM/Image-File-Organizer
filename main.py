import tkinter as tk
from tkinter import filedialog

def select_folder():
    folder_path = filedialog.askdirectory()
    if folder_path:
        folder_label.config(text=folder_path)
        organize_images_btn.config(state="normal")

root = tk.Tk()
root.title("Image Organizer")
root.geometry("300x250")

select_folder_btn = tk.Button(root, text="Select Folder", command=select_folder)
select_folder_btn.pack(pady=20, padx=20)

folder_label = tk.Label(root, text="", wraplength=400)
folder_label.pack(pady=10, padx=10)

organize_images_btn = tk.Button(root, text="Organize Images", state="disabled")
organize_images_btn.pack(pady=20,padx=20)

root.mainloop()
