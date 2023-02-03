import tkinter as tk
import uuid
import csv

def submit():
    first_name = first_name_entry.get()
    last_name = last_name_entry.get()
    email = email_entry.get()
    a = uuid.uuid4()
    with open('project2/datastorage/data_{}.csv'.format(a), 'a') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([first_name, last_name, email])

    first_name_entry.delete(0, 'end')
    last_name_entry.delete(0, 'end')
    email_entry.delete(0, 'end')

root = tk.Tk()
root.geometry("500x500")
root.title("Form")

first_name_label = tk.Label(root, text="GPU Model")
first_name_label.pack()

first_name_entry = tk.Entry(root)
first_name_entry.pack()

last_name_label = tk.Label(root, text="GPU Vram")
last_name_label.pack()

last_name_entry = tk.Entry(root)
last_name_entry.pack()

email_label = tk.Label(root, text="Cost")
email_label.pack()

email_entry = tk.Entry(root)
email_entry.pack()

submit_button = tk.Button(root, text="Submit", command=submit)
submit_button.pack()

root.mainloop()