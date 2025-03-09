import tkinter as tk
import requests  
from tkinter import ttk
from PIL import Image, ImageTk
from io import BytesIO

root = tk.Tk()
root.title("Country Name")
root.geometry("550x500")
root.configure(bg="#6495ED")

def data():
    try:
        country_name = input.get()
        res = requests.get(f"https://restcountries.com/v3.1/name/{country_name}")
        data = res.json()

        image_url = f"{data[0]["flags"]["png"]}"
        respone = requests.get(image_url)
        img_data = BytesIO(respone.content)
        image = Image.open(img_data)
        photo = ImageTk.PhotoImage(image)
        label2.configure(image=photo)
        label2.image = photo

        label3.config(text=f"Population:  {data[0]["population"]}")
    except:
        print("Error")

label = ttk.Label(root, text="Enter Country Name", style="Design.Label")
label.pack(pady=15)
style = ttk.Style()
style.configure("Design.Label", font=("Arial", 16), background="#6495ED", foreground="white")
input = ttk.Entry(root, width=30)
input.pack()

button = tk.Button(root, text="Submit", font=("Arial", 13), background="#6F00FF", foreground="white", width=15, command=data)
button.pack(pady=25)

label2 = ttk.Label(root, text="Country Flag:  ", style="Flag.TLabel")
label2.pack(pady=15)
style3 = ttk.Style()
style3.configure("Flag.TLabel", font=("Arial", 12), background="#6495ED", foreground="white")

label3 = ttk.Label(root, text="Country Population:  ", style="Population.TLabel")
label3.pack()
style3 = ttk.Style()
style3.configure("Population.TLabel", font=("Arial", 12), background="#6495ED", foreground="white")

root.mainloop()