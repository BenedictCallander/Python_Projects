import tkinter as tk

root = tk.Tk()
root.geometry("500x500")
root.title("GUI")


textbox = tk.Text(root, height=3, font=('Arial',16))
textbox.pack(padx=10,pady=10)

button = tk.Button(root, text="click", font=("arial",16))
button.pack(padx=10,pady=10)

root.mainloop()