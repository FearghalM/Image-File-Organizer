import tkinter as tk



root = tk.Tk()
root.title("Image Organizer")

tk.Button(root, text="Select Folder").pack(pady=20)
folder_label = tk.Label(root, text="", wraplength=400)
folder_label.pack(pady=20, padx=20)

organize_images_btn = tk.Button(root, text="Organize Images", state="disabled")
organize_images_btn.pack(pady=20)

root.mainloop()
