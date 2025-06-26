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
    {"key": "tp_category", "label": "Vehicle Type", "options": [
        {"label": "Sleeper", "value": 16045},
        {"label": "Day Cab", "value": 16013},
        {"label": "Box Truck", "value": 16004},
        {"label": "Dump Truck", "value": 16014},
        {"label": "Expeditor", "value": 16016},
        {"label": "Hooklift", "value": 16028},
        {"label": "Flatbed", "value": 16019},
        {"label": "Chassis", "value": 16009},
    ]},
    {"key": "tp_model_year", "label": "Model Year", "options": [2027, 2026, 2025, 2024, 2023, 2022, 2021, 2020, 2019, 2018, 2017, 2016, 2015,2014, 2013, 2012, 2011, 2010, 2009, 2008, 2007, 2006, 2005, 2004, 2003, 2002, 2001, 2000]},
    {"key": "tp_make", "label": "Make", "options": ["Freightliner", "Western Star", "Isuzu", "Kenworth", "Peterbilt", "Volvo", "International", "Mack", "Hino", "Sterling"]},
    {"key": "tp_model", "label": "Model", "options": ['Cascadia', 'Columbia', 'M2', 'T680', 'T880', 'W900', 'VNL', 'VNR', 'ProStar', 'LT Series', 'CXU613']},
    {"key": "tp_engine", "label": "Engine", "options": ["CUMMINS", "DETROIT", "PACCAR", "ISUZU", "VOLVO", "MACK", "HINO", "CATERPILLAR"]},
    {"key": "tp_sleeper_type", "label": "Sleeper Type", "options": ['Raised Roof Sleeper', "Mid Roof Sleeper",]},
    {"key": "tp_rear_axles", "label": "# of Rear Axles", "options": ['Single', 'Tandem', 'Tri', 'Quad', 'Five', 'Six', 'Seven']},
]

# 2. Define the search sites and their URL patterns
SEARCH_SITES = {
    "Pacer": "https://pcl.uscourts.gov/pcl/pages/search/findBankruptcy.jsf",
    "OFAC": "https://sanctionssearch.ofac.treas.gov/",
    "NSOPW": "https://www.nsopw.gov/",
    "SOS": "https://businesssearch.ohiosos.gov/",
    "SOS List": "https://www.llcuniversity.com/50-secretary-of-state-sos-business-entity-search/",
    "Zillow": "https://www.zillow.com/homes/{query}_rb/",
    "Safer": "https://safer.fmcsa.dot.gov/keywordx.asp?searchstring=%2A{query}%2A&SEARCHTYPE=",
    #https://www.truckpaper.com/listings/search?Category=16045&Model=CASCADIA%20126&Manufacturer=FREIGHTLINER&Year=2021%2A2025&Mileage=100000%2A150000&Sleeper=Raised%20Roof%20Sleeper&Engine=CUMMINS&keywords=2025%20Cascadia
    "Truck Paper": "https://www.truckpaper.com/listings/search?{query}",
    "Google Customer": "https://www.google.com/search?q={query}",
    "Google Business": "https://www.google.com/search?q={query}",
}

# 3. Function to run the search
# This function will be called when the Search button is clicked
def run_search():
    # 2. Get all field values from the dictionary
    values = {key: var.get().strip() for key, var in field_vars.items()}
    print(values)  # Debugging line to see the values

    queries = {
        "Pacer": values["name"],
        "OFAC": values["name"],
        "NSOPW": values["name"],
        "SOS": values["business_name"],
        "SOS List": values["business_name"],
        "Zillow": values["address"] + " " + values["location"],
        "Safer": values["business_name"],
        "Truck Paper": {
            "Category": values["tp_category"],
            "ModelGroup": values["tp_model"],
            "Manufacturer": values["tp_make"],
            "Year": values["tp_model_year"],
            "Mileage": f"{mileage_min_var.get()}*{mileage_max_var.get()}",
            "Engine": values["tp_engine"],
            "Horsepower": f"{hp_min_var.get()}*{hp_max_var.get()}",
            "Sleeper": values["tp_sleeper_type"],
            "Axle": values["tp_rear_axles"],
        },
        "Google Customer": values["name"] + " " + values["location"],
        "Google Business": values["business_name"] + " " + values["business_address"],
    }
    print(queries)  # Debugging line to see the queries

    # 3. Open URLs in the default web browser
    def open_url(url, first):
        if first:
            subprocess.Popen(f'start chrome --new-window "{url}"', shell=True)
            time.sleep(0.01)
            return False
        else:
            subprocess.Popen(f'start chrome --new-tab "{url}"', shell=True)
            time.sleep(0.01)
            return first

    # Iterate through the SEARCH_SITES and construct URLs
    first = True
    for name, url_pattern in SEARCH_SITES.items():
        query = queries[name]
        if not query:
            continue

        if name == "Truck Paper":
            encoded_query = urllib.parse.urlencode(query, quote_via=urllib.parse.quote)
            url = url_pattern.format(query=encoded_query)
        else:
            encoded_query = urllib.parse.quote_plus(query)
            url = url_pattern.format(query=encoded_query)

        print(url)  # For debugging
        first = open_url(url, first)
    

# 4. Function to clear all fields
# This function will be called when the Clear button is clicked
def clear_fields():
    for var in field_vars.values():
        var.set("")
    #Clear mileage and horsepower ranges
    mileage_min_var.set("")
    mileage_max_var.set("")     
    hp_min_var.set("")
    hp_max_var.set("")

root = tk.Tk()
root.title("Highway Commercial Services, Inc.")
root.minsize(500, 320)

try:
    root.iconbitmap("HCS Logo.ico")
except Exception:
    pass

# Set default font for the application
default_font = tkfont.nametofont("TkDefaultFont")
default_font.configure(size=11, family="Segoe UI")

# 2. Create the main frame and title label
mainframe = ttk.Frame(root, padding="20 15 20 15")
mainframe.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
title_label = ttk.Label(mainframe, text="Quick Search Tool", font=("Segoe UI", 16, "bold"))
title_label.grid(row=0, column=0, columnspan=2, pady=(0, 15))

# 3. Create field variables and widgets dynamically
field_vars = {}
row = 1

# General fields
for field in FIELDS:
    if not field["key"].startswith("tp_"):
        var = tk.StringVar()
        field_vars[field["key"]] = var
        ttk.Label(mainframe, text=field["label"] + ":").grid(row=row, column=0, sticky=tk.W, padx=5, pady=5)
        ttk.Entry(mainframe, textvariable=var, width=40).grid(row=row, column=1, sticky=tk.W, padx=5, pady=5)
        row += 1

# Separator before Truck Paper specific fields
separator = ttk.Separator(mainframe, orient='horizontal')
separator.grid(row=row, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=10)
row += 1

# Truck Paper fields in a LabelFrame
truck_paper_frame = ttk.LabelFrame(mainframe, text="Truck Paper Search", padding="10 10 10 10")
truck_paper_frame.grid(row=row, column=0, columnspan=2, sticky=(tk.W, tk.E), padx=5, pady=5)
tp_row = 0

for field in FIELDS:
    if field["key"].startswith("tp_"):
        var = tk.StringVar()
        field_vars[field["key"]] = var
        ttk.Label(truck_paper_frame, text=field["label"] + ":").grid(row=tp_row, column=0, sticky=tk.W, padx=5, pady=5)
        if "options" in field:
            # Use Combobox for dropdowns
            values = [opt["label"] if isinstance(opt, dict) else opt for opt in field["options"]]
            cb = ttk.Combobox(truck_paper_frame, textvariable=var, values=values, width=37, state="readonly")
            cb.grid(row=tp_row, column=1, sticky=tk.W, padx=5, pady=5)
        else:
            ttk.Entry(truck_paper_frame, textvariable=var, width=40).grid(row=tp_row, column=1, sticky=tk.W, padx=5, pady=5)
        tp_row += 1

# Mileage Range
ttk.Label(truck_paper_frame, text="Mileage Range:").grid(row=tp_row, column=0, sticky=tk.W, padx=5, pady=5)
mileage_min_var = tk.StringVar()
mileage_max_var = tk.StringVar()
mileage_frame = ttk.Frame(truck_paper_frame)
mileage_frame.grid(row=tp_row, column=1, sticky=tk.W, padx=5, pady=5)
ttk.Entry(mileage_frame, textvariable=mileage_min_var, width=17).pack(side=tk.LEFT)
ttk.Label(mileage_frame, text="to").pack(side=tk.LEFT, padx=3)
ttk.Entry(mileage_frame, textvariable=mileage_max_var, width=17).pack(side=tk.LEFT)
tp_row += 1

# Horsepower Range
ttk.Label(truck_paper_frame, text="Horsepower Range:").grid(row=tp_row, column=0, sticky=tk.W, padx=5, pady=5)
hp_min_var = tk.StringVar()
hp_max_var = tk.StringVar()
hp_frame = ttk.Frame(truck_paper_frame)
hp_frame.grid(row=tp_row, column=1, sticky=tk.W, padx=5, pady=5)
ttk.Entry(hp_frame, textvariable=hp_min_var, width=17).pack(side=tk.LEFT)
ttk.Label(hp_frame, text="to").pack(side=tk.LEFT, padx=3)
ttk.Entry(hp_frame, textvariable=hp_max_var, width=17).pack(side=tk.LEFT)
tp_row += 1

row += 1

# Separator before buttons
separator = ttk.Separator(mainframe, orient='horizontal')
separator.grid(row=row, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=10)
row += 1

# Search and Clear buttons
ttk.Button(mainframe, text="Search", command=run_search).grid(row=row, column=0, pady=10, sticky=tk.E, padx=5)
ttk.Button(mainframe, text="Clear", command=clear_fields).grid(row=row, column=1, pady=10, sticky=tk.W, padx=5)

# Configure grid weights for resizing
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
mainframe.columnconfigure(0, weight=1)
mainframe.columnconfigure(1, weight=1)

# Start the GUI event loop
root.mainloop()