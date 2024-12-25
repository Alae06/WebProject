import tkinter as tk
from tkinter import messagebox


class SnackStand:
    def __init__(self, root):
        self.root = root
        self.root.title("Snack Stand")
        self.root.geometry("800x600")

        self.menu = {
            "Pizza": 40.00,
            "Tacos": 49.00,
            "Sandwich": 30.00,
            "Burger": 32.00,
            "Frites": 15.00,
            "Nuggets": 35.00,
            "Soda": 15.00,
            "Limonade": 18.00
        }
        self.selected_item = tk.StringVar()
        self.quantity = tk.StringVar(value="1")
        self.total = 0.0

        self.create_widgets()

    def create_widgets(self):
        left_frame = tk.Frame(self.root, bg='#FFE4E1', width=400)
        left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        right_frame = tk.Frame(self.root, bg='#FFF0F5', width=400)
        right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)


        (tk.Label(
            left_frame,
            text="MENU",
            font=('Arial', 20, 'bold'),
            bg='#FF6B6B',
            fg='white',
            pady=10,
            width=20
        ).pack(pady=10))

        menu_frame = tk.Frame(left_frame, bg='#FFE4E1')
        menu_frame.pack(pady=10)

        for item, price in self.menu.items():
            item_frame = tk.Frame(
                menu_frame,
                bg='#FFF0F5',
                padx=10,
                pady=5,
                relief=tk.RAISED,
                borderwidth=2
            )
            item_frame.pack(fill=tk.X, padx=20, pady=5)

            tk.Label(
                item_frame,
                text=f"{item}",
                font=('Arial', 12, 'bold'),
                bg='#FFF0F5'
            ).pack(side=tk.LEFT, padx=10)

            tk.Label(
                item_frame,
                text=f"{price:.2f}DH",
                font=('Arial', 12),
                bg='#FFF0F5',
                fg='#FF6B6B'
            ).pack(side=tk.RIGHT, padx=10)

        tk.Label(
            right_frame,
            text="COMMANDER",
            font=('Arial', 20, 'bold'),
            bg='#FF6B6B',
            fg='white',
            pady=10,
            width=20
        ).pack(pady=10)

        order_frame = tk.Frame(right_frame, bg='#FFF0F5')
        order_frame.pack(pady=20)

        tk.Label(
            order_frame,
            text="Choisir un produit:",
            font=('Arial', 12),
            bg='#FFF0F5'
        ).pack(pady=5)

        product_menu = tk.OptionMenu(order_frame, self.selected_item, *self.menu.keys())
        product_menu.config(width=15, font=('Arial', 12))
        product_menu.pack(pady=5)

        tk.Label(
            order_frame,
            text="Quantité:",
            font=('Arial', 12),
            bg='#FFF0F5'
        ).pack(pady=5)

        quantity_spinbox = tk.Spinbox(
            order_frame,
            from_=1,
            to=10,
            textvariable=self.quantity,
            width=5,
            font=('Arial', 12)
        )
        quantity_spinbox.pack(pady=5)

        tk.Button(
            order_frame,
            text="Ajouter à la commande",
            command=self.add_to_order,
            font=('Arial', 12, 'bold'),
            bg='#FF6B6B',
            fg='white',
            pady=5
        ).pack(pady=20)

        self.order_text = tk.Text(
            right_frame,
            height=10,
            width=35,
            font=('Arial', 10)
        )
        self.order_text.pack(pady=10)

        tk.Button(
            right_frame,
            text="Finaliser la commande",
            command=self.finalize_order,
            font=('Arial', 12, 'bold'),
            bg='#4A4A4A',
            fg='white',
            pady=5
        ).pack(pady=10)

    def add_to_order(self):
        if not self.selected_item.get():
            messagebox.showwarning("Erreur", "Veuillez sélectionner un produit!")
            return

        item = self.selected_item.get()
        quantity = int(self.quantity.get())
        price = self.menu[item]
        subtotal = price * quantity

        self.total += subtotal

        self.order_text.insert(tk.END, f"{item} x{quantity} = {subtotal:.2f}DH\n")

    def finalize_order(self):
        if self.total == 0:
            messagebox.showwarning("Erreur", "Votre commande est vide!")
            return

        message = f"Total de votre commande: {self.total:.2f}DH\nMerci de votre achat!"
        messagebox.showinfo("Commande finalisée", message)

        self.total = 0
        self.order_text.delete(1.0, tk.END)
        self.quantity.set("1")
        self.selected_item.set("")


root = tk.Tk()
app = SnackStand(root)
root.mainloop()