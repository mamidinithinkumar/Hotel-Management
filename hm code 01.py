import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3

class HotelManagementSystem:
    def _init_(self, root):
        self.root = root
        self.root.title("Hotel Management System")
        
        # Variables to store user inputs
        self.guest_name = tk.StringVar()
        self.address = tk.StringVar()
        self.check_in_date = tk.StringVar()
        self.check_out_date = tk.StringVar()
        self.room_type = tk.StringVar()
        self.is_ac = tk.BooleanVar()
        self.food_menu_selection = {
            'Breakfast': [],
            'Lunch': [],
            'Dinner': []
        }
        
        # Initialize total amount
        self.total_amount = tk.DoubleVar()
        self.total_amount.set(0.0)
        
        # UI setup
        self.create_widgets()
    
    def create_widgets(self):
        # Frame for guest details
        guest_frame = ttk.LabelFrame(self.root, text="Guest Details")
        guest_frame.grid(row=0, column=0, padx=10, pady=10, sticky=tk.W+tk.E)
        
        tk.Label(guest_frame, text="Name:").grid(row=0, column=0, sticky=tk.W)
        tk.Entry(guest_frame, textvariable=self.guest_name).grid(row=0, column=1, padx=5, pady=5)
        
        tk.Label(guest_frame, text="Address:").grid(row=1, column=0, sticky=tk.W)
        tk.Entry(guest_frame, textvariable=self.address).grid(row=1, column=1, padx=5, pady=5)
        
        tk.Label(guest_frame, text="Check-in Date:").grid(row=2, column=0, sticky=tk.W)
        tk.Entry(guest_frame, textvariable=self.check_in_date).grid(row=2, column=1, padx=5, pady=5)
        
        tk.Label(guest_frame, text="Check-out Date:").grid(row=3, column=0, sticky=tk.W)
        tk.Entry(guest_frame, textvariable=self.check_out_date).grid(row=3, column=1, padx=5, pady=5)
        
        # Frame for room booking
        room_frame = ttk.LabelFrame(self.root, text="Room Booking")
        room_frame.grid(row=1, column=0, padx=10, pady=10, sticky=tk.W+tk.E)
        
        tk.Label(room_frame, text="Room Type:").grid(row=0, column=0, sticky=tk.W)
        ttk.Combobox(room_frame, textvariable=self.room_type, values=['Single', 'Double']).grid(row=0, column=1, padx=5, pady=5)
        
        tk.Checkbutton(room_frame, text="AC", variable=self.is_ac).grid(row=1, column=0, padx=5, pady=5)
        
        # Frame for food menu
        food_frame = ttk.LabelFrame(self.root, text="Food Menu")
        food_frame.grid(row=0, column=1, rowspan=2, padx=10, pady=10, sticky=tk.W+tk.E+tk.N+tk.S)
        
        food_items = {
            'Breakfast': [
                ("Toast", 5),
                ("Eggs", 7),
                ("Pancakes", 8),
                ("Fruit Salad", 6),
                ("Croissant", 4)
            ],
            'Lunch': [
                ("Burger", 10),
                ("Pizza", 12),
                ("Salad", 8),
                ("Sandwich", 7),
                ("Soup", 6)
            ],
            'Dinner': [
                ("Pasta", 15),
                ("Steak", 20),
                ("Fish", 18),
                ("Roast Chicken", 16),
                ("Sushi", 22)
            ]
        }
        
        for meal_type, items in food_items.items():
            ttk.Label(food_frame, text=meal_type).grid(row=len(self.food_menu_selection), column=0, columnspan=2, pady=5, sticky=tk.W)
            for index, (item_name, price) in enumerate(items, start=1):
                item_var = tk.IntVar()
                tk.Checkbutton(food_frame, text=f"{item_name} (${price})", variable=item_var).grid(row=len(self.food_menu_selection) + index, column=0, padx=5, pady=2, sticky=tk.W)
                self.food_menu_selection[meal_type].append((item_name, price, item_var))
        
        # Frame for total amount
        total_frame = ttk.LabelFrame(self.root, text="Total Amount")
        total_frame.grid(row=2, column=0, columnspan=2, padx=10, pady=10, sticky=tk.W+tk.E)
        
        tk.Label(total_frame, text="Total:").grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
        tk.Label(total_frame, textvariable=self.total_amount).grid(row=0, column=1, padx=5, pady=5, sticky=tk.W)
        
        # Button to calculate total amount
        tk.Button(self.root, text="Calculate Total", command=self.calculate_total).grid(row=3, column=0, columnspan=2, pady=10)
    
    def calculate_total(self):
        total = 0.0
        
        # Calculate total amount based on selected food items
        for meal_type, items in self.food_menu_selection.items():
            for item_name, price, var in items:
                if var.get() == 1:
                    total += price
        
        # Update total amount variable
        self.total_amount.set(total)
    
    def run(self):
        self.root.mainloop()

# Initialize Tkinter
if _name_ == "_main_":
    root = tk.Tk()
    app = HotelManagementSystem(root)
    app.run()
