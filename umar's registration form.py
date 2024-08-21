import tkinter as tk
from tkinter import ttk

def submit_form():
    # Collect form data
    first_name = first_name_entry.get()
    last_name = last_name_entry.get()
    dob_day = day_var.get()
    dob_month = month_var.get()
    dob_year = year_var.get()
    health_status = 'Yes' if health_var.get() else 'No'
    country = country_entry.get()
    state = state_entry.get()
    city = city_entry.get()
    phone = phone_entry.get()
    email = email_entry.get()
    
    # Print data to console (you can replace this with saving to a file or database)
    print(f"First Name: {first_name}")
    print(f"Last Name: {last_name}")
    print(f"Date of Birth: {dob_day}/{dob_month}/{dob_year}")
    print(f"Health Status: {health_status}")
    print(f"Address: {country}, {state}, {city}")
    print(f"Phone Number: {phone}")
    print(f"Email: {email}")

# Create the main window
root = tk.Tk()
root.title("Registration Form")

# First Name
tk.Label(root, text="First Name").grid(row=0, column=0, padx=10, pady=5)
first_name_entry = tk.Entry(root)
first_name_entry.grid(row=0, column=1, padx=10, pady=5)

# Last Name
tk.Label(root, text="Last Name").grid(row=1, column=0, padx=10, pady=5)
last_name_entry = tk.Entry(root)
last_name_entry.grid(row=1, column=1, padx=10, pady=5)

# Date of Birth
tk.Label(root, text="Date of Birth").grid(row=2, column=0, padx=10, pady=5)

day_var = tk.StringVar()
day_menu = ttk.Combobox(root, textvariable=day_var, values=[str(i) for i in range(1, 32)], width=5)
day_menu.grid(row=2, column=1, padx=10, pady=5, sticky="w")
day_menu.set("Day")

month_var = tk.StringVar()
month_menu = ttk.Combobox(root, textvariable=month_var, values=[
    "January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"
], width=10)
month_menu.grid(row=2, column=1, padx=50, pady=5, sticky="w")
month_menu.set("Month")

year_var = tk.StringVar()
year_menu = ttk.Combobox(root, textvariable=year_var, values=[str(i) for i in range(1900, 2025)], width=7)
year_menu.grid(row=2, column=1, padx=150, pady=5, sticky="w")
year_menu.set("Year")

# Health Status
health_var = tk.IntVar()
tk.Checkbutton(root, text="Do you have any health issues?", variable=health_var).grid(row=3, column=0, columnspan=2, padx=10, pady=5)

# Address
tk.Label(root, text="Country").grid(row=4, column=0, padx=10, pady=5)
country_entry = tk.Entry(root)
country_entry.grid(row=4, column=1, padx=10, pady=5)

tk.Label(root, text="State").grid(row=5, column=0, padx=10, pady=5)
state_entry = tk.Entry(root)
state_entry.grid(row=5, column=1, padx=10, pady=5)

tk.Label(root, text="City").grid(row=6, column=0, padx=10, pady=5)
city_entry = tk.Entry(root)
city_entry.grid(row=6, column=1, padx=10, pady=5)

# Phone Number
tk.Label(root, text="Phone Number").grid(row=7, column=0, padx=10, pady=5)
phone_entry = tk.Entry(root)
phone_entry.grid(row=7, column=1, padx=10, pady=5)

# Email
tk.Label(root, text="Email").grid(row=8, column=0, padx=10, pady=5)
email_entry = tk.Entry(root)
email_entry.grid(row=8, column=1, padx=10, pady=5)

# Submit Button
submit_button = tk.Button(root, text="Submit", command=submit_form)
submit_button.grid(row=9, column=0, columnspan=2, pady=10)

# Run the application
root.mainloop()
