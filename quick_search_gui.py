import tkinter as tk
from tkinter import ttk
import urllib.parse
import subprocess
import time
import tkinter.font as tkfont

# 1. Define your fields in a list of dicts
FIELDS = [
    {"key": "name", "label": "Customer Name"},
    {"key": "address", "label": "Home Address"},
    {"key": "location", "label": "City and State"},
    {"key": "business_name", "label": "Business Name"},
    {"key": "business_address", "label": "Business Address"},
    {"key": "tp_category", "label": "Category"},
    {"key": "tp_model", "label": "Model"},
    {"key": "tp_make", "label": "Make"},
    {"key": "tp_model_year", "label": "Model Year"},
    {"key": "tp_engine", "label": "Engine"},
    {"key": "tp_sleeper_type", "label": "Sleeper Type"},
    {"key": "tp_rear_axles", "label": "# of Rear Axles"},
    {"key": "tp_mileage", "label": "Mileage"},
    {"key": "tp_horsepower", "label": "Horsepower"},
]

SEARCH_SITES = {
    "Pacer": "https://pcl.uscourts.gov/pcl/pages/search/findBankruptcy.jsf",
    "OFAC": "https://sanctionssearch.ofac.treas.gov/",
    "NSOPW": "https://www.nsopw.gov/",
    "SOS": "https://businesssearch.ohiosos.gov/",
    "SOS List": "https://www.llcuniversity.com/50-secretary-of-state-sos-business-entity-search/",
    "Zillow": "https://www.zillow.com/homes/{query}_rb/",
    "Safer": "https://safer.fmcsa.dot.gov/keywordx.asp?searchstring=%2A{query}%2A&SEARCHTYPE=",
    #https://www.truckpaper.com/listings/search?Category=16045&Model=CASCADIA%20126&Manufacturer=FREIGHTLINER&Year=2021%2A2025&Mileage=100000%2A150000&Sleeper=Raised%20Roof%20Sleeper&Engine=CUMMINS&keywords=2025%20Cascadia
    "Truck Paper": "https://www.truckpaper.com/listings?keywords={query}",
    "Google Customer": "https://www.google.com/search?q={query}",
    "Google Business": "https://www.google.com/search?q={query}",
}

def run_search():
    # 2. Get all field values from the dictionary
    values = {key: var.get().strip() for key, var in field_vars.items()}

    queries = {
        "Pacer": values["name"],
        "OFAC": values["name"],
        "NSOPW": values["name"],
        "SOS": values["business_name"],
        "SOS List": values["business_name"],
        "Zillow": values["address"] + " " + values["location"],
        "Safer": values["business_name"],
        #"Truck Paper": values["asset"],
        "Google Customer": values["name"] + " " + values["location"],
        "Google Business": values["business_name"] + " " + values["business_address"],
    }

    first = True
    for name, url_pattern in SEARCH_SITES.items():
        query = queries[name]
        if not query:
            continue
        encoded_query = urllib.parse.quote_plus(query)
        url = url_pattern.format(query=encoded_query)
        if first:
            subprocess.Popen(f'start chrome --new-window "{url}"', shell=True)
            first = False
            time.sleep(0.01)
        else:
            subprocess.Popen(f'start chrome --new-tab "{url}"', shell=True)
            time.sleep(0.01)

def clear_fields():
    for var in field_vars.values():
        var.set("")

root = tk.Tk()
root.title("Highway Commercial Services, Inc.")
root.minsize(500, 320)

try:
    root.iconbitmap("HCS Logo.ico")
except Exception:
    pass

default_font = tkfont.nametofont("TkDefaultFont")
default_font.configure(size=11, family="Segoe UI")

mainframe = ttk.Frame(root, padding="20 15 20 15")
mainframe.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

title_label = ttk.Label(mainframe, text="Quick Search Tool", font=("Segoe UI", 16, "bold"))
title_label.grid(row=0, column=0, columnspan=2, pady=(0, 15))

# 3. Create field variables and widgets dynamically
field_vars = {}
row = 1
for field in FIELDS:
    var = tk.StringVar()
    field_vars[field["key"]] = var

    # Skip fields that start with "tp_" for Truck Paper
    if not field["key"].startswith("tp_"):
        ttk.Label(mainframe, text=field["label"] + ":").grid(row=row, column=0, sticky=tk.W, pady=3)
        ttk.Entry(mainframe, textvariable=var, width=45).grid(row=row, column=1, pady=3)
        row += 1

# Separator before Truck Paper specific fields
separator = ttk.Separator(mainframe, orient='horizontal')
separator.grid(row=row, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=10)
row += 1

# Truck Paper specific fields
truck_paper_fields = [
    {"key": "tp_category", "label": "Vehicle Type", "options": ['Truck', 'Trailer', 'Van']},
    {"key": "tp_model", "label": "Model", "options": ['Model A', 'Model B']},
    {"key": "tp_make", "label": "Make", "options": ['Manufacturer X', 'Manufacturer Y']},
    {"key": "tp_model_year", "label": "Model Year", "options": [2025, 2024, 2023]},
    {"key": "tp_engine", "label": "Engine", "options": ['Engine 1', 'Engine 2']},
    {"key": "tp_sleeper_type", "label": "Sleeper Type", "options": ['Flat Top', 'Raised Roof']},
    {"key": "tp_rear_axles", "label": "# of Rear Axles", "options": [1, 2, 3, 4]},
]

# Create variables and widgets for Truck Paper specific fields
for field in truck_paper_fields:
    var = tk.StringVar()
    field_vars[field["key"]] = var

    ttk.Label(mainframe, text=field["label"] + ":").grid(row=row, column=0, sticky=tk.W, pady=3)
    cb = ttk.Combobox(mainframe, textvariable=var, values=field["options"], width=45)
    cb.grid(row=row, column=1, pady=3)
    row += 1

# Mileage Range
ttk.Label(mainframe, text="Mileage Range:").grid(row=row, column=0, sticky=tk.W, pady=3)
mileage_min_var = tk.StringVar()
mileage_max_var = tk.StringVar()
ttk.Entry(mainframe, textvariable=mileage_min_var, width=20).grid(row=row, column=1, sticky=tk.W, pady=3)
ttk.Label(mainframe, text="to").grid(row=row, column=1, sticky=tk.W, padx=(150, 0))
ttk.Entry(mainframe, textvariable=mileage_max_var, width=20).grid(row=row, column=1, sticky=tk.E, pady=3)
row += 1    

# Horsepower Range
ttk.Label(mainframe, text="Horsepower Range:").grid(row=row, column=0, sticky=tk.W, pady=3)
hp_min_var = tk.StringVar()
hp_max_var = tk.StringVar()
ttk.Entry(mainframe, textvariable=hp_min_var, width=20).grid(row=row, column=1, sticky=tk.W, pady=3)
ttk.Label(mainframe, text="to").grid(row=row, column=1, sticky=tk.W, padx=(150, 0))
ttk.Entry(mainframe, textvariable=hp_max_var, width=20).grid(row=row, column=1, sticky=tk.E, pady=3)
row += 1

# Separator before buttons
separator = ttk.Separator(mainframe, orient='horizontal')
separator.grid(row=row, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=10)
row += 1

ttk.Button(mainframe, text="Search", command=run_search).grid(row=row, column=0, pady=10, sticky=tk.E)
ttk.Button(mainframe, text="Clear", command=clear_fields).grid(row=row, column=1, pady=10, sticky=tk.W)

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
mainframe.columnconfigure(0, weight=1)
mainframe.columnconfigure(1, weight=1)

root.mainloop()