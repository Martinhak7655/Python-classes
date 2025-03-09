import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from io import BytesIO
import requests

root = tk.Tk()
root.title("Test")
root.geometry("500x500")
root.configure(bg="#2c3e50")

button = ttk.Button(root, text="Button", style="TButton")
button.pack()
style = ttk.Style()
style.configure("TButton", font=("Arial", 10), padding=5, background="#000", foreground="#000")

image_url = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQYZqZkpMyiN2uSuT7GAf6JSkJ44YsZqoQHdw&s"
response = requests.get(image_url)
img_data = BytesIO(response.content)
image = Image.open(img_data)
photo = ImageTk.PhotoImage(image)
label = tk.Label(root, image=photo)
label.pack()

root.mainloop()