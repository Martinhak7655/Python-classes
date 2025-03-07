import requests
import tkinter as tk

root = tk.Tk()

def data():
    try: 
        text = input.get()
        res = requests.get(f"https://restcountries.com/v3.1/name/{text}")
        data = res.json()
        print(f"Population: {data[0]["population"]}")
        print(f"Capital City: {data[0]["capital"][0]}")
        label.config(text=f"Population: {data[0]["population"]}")
        label2.config(text=f"Capital City: {data[0]["capital"][0]}")
    except:
        print("Error")

root.title("Country Name")
root.geometry("400x400")

input = tk.Entry(root, width=30)
input.pack(pady=15)

button = tk.Button(root, text="Submit", command=data)
button.pack()

label = tk.Label(root, text="Population")
label.pack(pady=10)

label2 = tk.Label(root, text="Capital City")
label2.pack(pady=10)

root.mainloop()

#Desktop havelvac sarqel vory calculator a uni ereq tox arajiny` tivy rkrordy nshan errordy eli tiv nayev petqa kochak lini vortex petqa hasvi 