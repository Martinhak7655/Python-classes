import tkinter as tk

root = tk.Tk()
root.title("Calculate")
root.geometry("450x400")

def calculator():
    try:

        num1 = int(input.get())
        operator = input2.get()
        num2 = int(input3.get())

        if operator == "+":
            label4.config(text=f"result: {num1 + num2}")   
        elif operator == "-":
            label4.config(text=f"result: {num1 - num2}")   
        elif operator == "*":
            label4.config(text=f"result: {num1 * num2}")   
        elif operator == "/":
            label4.config(text=f"result: {num1 / num2}")   
        else:
            result = "Invalid Operator"
    except:
        print("Error")

label = tk.Label(root, text="First Number")
label.pack()
input = tk.Entry(root, width=50)
input.pack(pady=20)

label2 = tk.Label(root, text="Operator")
label2.pack()
input2 = tk.Entry(root, width=50)
input2.pack(pady=20)

label3 = tk.Label(root, text="Last Number")
label3.pack()
input3 = tk.Entry(root, width=50)
input3.pack(pady=20)

button = tk.Button(root, text="Calculate", command=calculator)
button.pack()

label4 = tk.Label(root, text="Calculating....")
label4.pack(pady=10)

root.mainloop()