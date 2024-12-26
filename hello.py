import tkinter as tk
from tkinter import messagebox

window = tk.Tk()
window.title("Snack")
window.configure(bg='#FFE4E1')

menu = {
    "Pizza": 40.00,
    "Tacos": 49.00,
    "Sandwich": 30.00,
    "Burger": 32.00,
    "Frites": 15.00,
    "Nuggets": 35.00,
    "Soda": 15.00,
    "Limonade": 18.00
}

order = {}

title = tk.Label(
    window,
    text="Menu de snack",
    font=('Arial', 24, 'bold'),
    bg='#FF6B6B',
    fg='white',
    pady=10,
    width=30
)
title.pack(pady=10)

menu_frame = tk.Frame(window, bg='#FFE4E1')
menu_frame.pack(padx=20, pady=10)

row = 0
col = 0
for item in menu:
    item_frame = tk.Frame(
        menu_frame,
        bg='#FFF0F5',
        padx=10,
        pady=10,
        relief=tk.RAISED,
        borderwidth=2
    )
    item_frame.grid(row=row, column=col, padx=10, pady=5)

    tk.Label(
        item_frame,
        text=item,
        font=('Arial', 12, 'bold'),
        bg='#FFF0F5',
        fg='#4A4A4A'
    ).pack()

    tk.Label(
        item_frame,
        text=str(menu[item]) + "DH",
        font=('Arial', 11),
        bg='#FFF0F5',
        fg='#FF6B6B'
    ).pack()

    spinbox = tk.Spinbox(
        item_frame,
        from_=0,
        to=10,
        width=5,
        font=('Arial', 10),
        bg='white',
    )
    spinbox.pack(pady=5)
    order[item] = spinbox

    col = col + 1
    if col > 3:
        col = 0
        row = row + 1

def calculate_total():
    total = 0
    order_summary = "AJOUTER:\n\n"
    has_items = False

    for item in order:
        quantity = int(order[item].get())
        if quantity > 0:
            has_items = True
            item_total = quantity * menu[item]
            total = total + item_total
            order_summary = order_summary + f"{item}: {quantity} x {menu[item]}DH = {item_total}DH\n"

    if has_items == False:
        messagebox.showwarning("commande", "SELECTIONNER QUELQUE CHOSE!")
        return

    order_summary = order_summary + f"\nTotal: {total}DH"
    messagebox.showinfo("Total", order_summary)

def reset_order():
    for item in order:
        order[item].delete(0, tk.END)
        order[item].insert(0, "0")

calculate_button = tk.Button(
    window,
    text="Calculer Total",
    command=calculate_total,
    font=('Arial', 12, 'bold'),
    bg='#FF6B6B',
    fg='white',
    padx=20,
    pady=10,
)
calculate_button.pack(pady=20)

reset_button = tk.Button(
    window,
    text="SUPPRIMER",
    command=reset_order,
    font=('Arial', 12),
    bg='#4A4A4A',
    fg='white',
    padx=20,
    pady=5,
)
reset_button.pack(pady=10)

window.mainloop()

