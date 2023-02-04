import tkinter as tk
import csv
import uuid



def add_system():
    system_info = [manufacturer_entry.get(), cpu_entry.get(), psu_entry.get(), ram_entry.get()]
    sysID = uuid.uuid4()
    fpath = "temp/{}.csv".format(sysID)
    with open(fpath, 'a', newline='') as file:
        writer = csv.writer(file)
        if file.tell() == 0:  # if file is empty, write column headings
            writer.writerow(["Manufacturer", "CPU", "PSU", "RAM"])
        writer.writerow(system_info)
    manufacturer_entry.delete(0, 'end')
    cpu_entry.delete(0, 'end')
    psu_entry.delete(0, 'end')
    ram_entry.delete(0, 'end')

usedWIN = tk.Tk()
usedWIN.title("System Information")
usedWIN.configure(bg="#F18E0F")


manufacturer_label = tk.Label(usedWIN, text="Manufacturer:",bg="#F18E0F")
manufacturer_label.grid(row=0, column=0)

manufacturer_entry = tk.Entry(usedWIN)
manufacturer_entry.grid(row=0, column=1)

cpu_label = tk.Label(usedWIN, text="CPU:",bg="#F18E0F")
cpu_label.grid(row=1, column=0)

cpu_entry = tk.Entry(usedWIN)
cpu_entry.grid(row=1, column=1)

psu_label = tk.Label(usedWIN, text="PSU (W):",bg="#F18E0F")
psu_label.grid(row=2, column=0)

psu_entry = tk.Entry(usedWIN)
psu_entry.grid(row=2, column=1)

ram_label = tk.Label(usedWIN, text="RAM (GB):",bg="#F18E0F")
ram_label.grid(row=3, column=0)

ram_entry = tk.Entry(usedWIN)
ram_entry.grid(row=3, column=1)

add_button = tk.Button(usedWIN, text="Add System", command=add_system)
add_button.grid(row=4, column=0, columnspan=2, pady=10)

usedWIN.mainloop()