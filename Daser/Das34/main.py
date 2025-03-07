import tkinter as tk 

root = tk.Tk()

def submit():
    text = input.get()
    print(text)

root.title("Test Project")
root.geometry("600x600")
input = tk.Entry(root, width=50)
input.pack(pady=10)

input2 = tk.Entry(root, width=50)
input2.pack(pady=10)

button = tk.Button(root, text="Login", command=submit)
button.pack()


root.mainloop()