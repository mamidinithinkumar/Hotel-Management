import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3

class HotelManagementSystem:
    def __init__(self, root):
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
        
        # Button to book room
        tk.Button(room_frame, text="Book Room", command=self.book_room).grid(row=2, column=0, columnspan=2, pady=10)
        
        # Frame for food menu
        food_frame = ttk.LabelFrame(self.root, text="Food Menu")
        food_frame.grid(row=0, column=1, rowspan=2, padx=10, pady=10, sticky=tk.W+tk.E+tk.N+tk.S)
        
        food_items = {
            'Breakfast': [
                ("Toast", 50),
                ("Eggs", 70),
                ("Pancakes", 80),
                ("Fruit Salad", 60),
                ("Croissant", 40)
            ],
            'Lunch': [
                ("Burger", 100),
                ("Pizza", 120),
                ("Salad", 80),
                ("Sandwich", 70),
                ("Soup", 60)
            ],
            'Dinner': [
                ("Pasta", 150),
                ("Steak", 200),
                ("Fish", 180),
                ("Roast Chicken", 160),
                ("Sushi", 220)
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
    
    def book_room(self):
        # Retrieve all user inputs
        guest_name = self.guest_name.get()
        address = self.address.get()
        check_in_date = self.check_in_date.get()
        check_out_date = self.check_out_date.get()
        room_type = self.room_type.get()
        is_ac = self.is_ac.get()
        
        # Example: Print the details to console
        print(f"Guest Name: {guest_name}")
        print(f"Address: {address}")
        print(f"Check-in Date: {check_in_date}")
        print(f"Check-out Date: {check_out_date}")
        print(f"Room Type: {room_type}")
        print(f"AC Required: {'Yes' if is_ac else 'No'}")
        
        # Here you can add code to store these details in a database or perform other actions
        
        # Show a message box confirming booking
        messagebox.showinfo("Booking Confirmation", "Room booked successfully!")
    
    def run(self):
        self.root.mainloop()

# Initialize Tkinter
if __name__ == "__main__":
    root = tk.Tk()
    app = HotelManagementSystem(root)
    app.run()