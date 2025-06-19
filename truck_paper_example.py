# ...existing code and dynamic field/widget generation...

# --- Truck Paper Specific Fields ---
truck_paper_fields = {
    "category": {"label": "Category", "options": ['Truck', 'Trailer', 'Van']},
    "model": {"label": "Model", "options": ['Model A', 'Model B']},
    "manufacturer": {"label": "Manufacturer", "options": ['Manufacturer X', 'Manufacturer Y']},
    "model_year": {"label": "Model Year", "options": [2025, 2024, 2023]},
    "engine": {"label": "Engine", "options": ['Engine 1', 'Engine 2']},
    "sleeper_type": {"label": "Sleeper Type", "options": ['Flat Top', 'Raised Roof']},
    "rear_axles": {"label": "Number of Rear Axles", "options": [1, 2, 3, 4]},
}

truck_paper_vars = {}
row = row  # continue from your last row

for field, props in truck_paper_fields.items():
    ttk.Label(root, text=props["label"] + ":").grid(row=row, column=0, sticky="e")
    var = tk.StringVar()
    truck_paper_vars[field] = var
    cb = ttk.Combobox(root, textvariable=var, values=props["options"])
    cb.grid(row=row, column=1)
    row += 1

# Mileage Range
ttk.Label(root, text="Mileage Range:").grid(row=row, column=0, sticky="e")
mileage_min_var = tk.StringVar()
mileage_max_var = tk.StringVar()
ttk.Entry(root, textvariable=mileage_min_var, width=8).grid(row=row, column=1, sticky="w")
ttk.Label(root, text="to").grid(row=row, column=1)
ttk.Entry(root, textvariable=mileage_max_var, width=8).grid(row=row, column=1, sticky="e")
row += 1

# Horsepower Range
ttk.Label(root, text="Horsepower Range:").grid(row=row, column=0, sticky="e")
hp_min_var = tk.StringVar()
hp_max_var = tk.StringVar()
ttk.Entry(root, textvariable=hp_min_var, width=8).grid(row=row, column=1, sticky="w")
ttk.Label(root, text="to").grid(row=row, column=1)
ttk.Entry(root, textvariable=hp_max_var, width=8).grid(row=row, column=1, sticky="e")
row += 1

# --- Update your submit function to include these ---
def submit():
    query = {}
    # ...existing field collection...
    for field, var in truck_paper_vars.items():
        query[field] = var.get()
    query["mileage_min"] = mileage_min_var.get()
    query["mileage_max"] = mileage_max_var.get()
    query["horsepower_min"] = hp_min_var.get()
    query["horsepower_max"] = hp_max_var.get()
    print("Query:", query)  # Replace with your query logic

# ...existing code for Search button and mainloop...