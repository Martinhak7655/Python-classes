import tkinter as tk
from tkinter import ttk
from controller import star, cross_square, draw_heart, square

root = tk.Tk()
root.title("Ստեղծել նկար")
root.geometry("450x400")
root.configure(bg="#6495ED")
        
button = tk.Button(root, text="Աստղիկ", font=("Arial", 13), background="#6F00FF", foreground="white", width=15, command=star)
button.pack(pady=25)

button = tk.Button(root, text="Խաչաձև քառակուսի", font=("Arial", 13), background="#6F00FF", foreground="white", width=25, command=cross_square)
button.pack(pady=25)

button = tk.Button(root, text="Սրտիկ", font=("Arial", 13), background="#6F00FF", foreground="white", width=15, command=draw_heart)
button.pack(pady=25)

button = tk.Button(root, text="Եռանկյունի", font=("Arial", 13), background="#6F00FF", foreground="white", width=15, command=square)
button.pack(pady=25)

if __name__ == "__main__":
    root.mainloop()