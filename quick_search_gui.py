import tkinter as tk
from tkinter import ttk
import urllib.parse
import subprocess
import time


def run_search():
    name = name_var.get().strip()
    address = address_var.get().strip()
    asset = asset_var.get().strip()
    business_name = business_name_var.get().strip()
    business_address = business_address_var.get().strip()
    location = location_var.get().strip()

    queries = {
        "Pacer": name,
        "OFAC": name,
        "NSOPW": name,
        "SOS": business_name,
        "SOS List": business_name,
        "Zillow": address + " " + location,
        "Safer": business_name,
        "Truck Paper": asset,
        "Google Customer": name + " " + location,
        "Google Business": business_name + " " + business_address,
    }

    SEARCH_SITES = {
        "Pacer": "https://pcl.uscourts.gov/pcl/pages/search/findBankruptcy.jsf",
        "OFAC": "https://sanctionssearch.ofac.treas.gov/",
        "NSOPW": "https://www.nsopw.gov/",
        "SOS": "https://businesssearch.ohiosos.gov/",
        "SOS List": "https://www.llcuniversity.com/50-secretary-of-state-sos-business-entity-search/",
        "Zillow": "https://www.zillow.com/homes/{query}_rb/",
        "Safer": "https://safer.fmcsa.dot.gov/keywordx.asp?searchstring=%2A{query}%2A&SEARCHTYPE=",
        "Truck Paper": "https://www.truckpaper.com/listings?keywords={query}",
        "Google Customer": "https://www.google.com/search?q={query}",
        "Google Business": "https://www.google.com/search?q={query}",
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
            time.sleep(0.5)
        else:
            subprocess.Popen(f'start chrome --new-tab "{url}"', shell=True)


def clear_fields():
    name_var.set("")
    address_var.set("")
    asset_var.set("")
    business_name_var.set("")
    business_address_var.set("")    
    location_var.set("")


root = tk.Tk()
root.title("Quick Search")
root.iconbitmap("HCS Logo.ico")

mainframe = ttk.Frame(root, padding="10")
mainframe.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

name_var = tk.StringVar()
address_var = tk.StringVar()
asset_var = tk.StringVar()
business_name_var = tk.StringVar()
business_address_var = tk.StringVar()
location_var = tk.StringVar()

ttk.Label(mainframe, text="Customer Name:").grid(row=0, column=0, sticky=tk.W)
ttk.Entry(mainframe, textvariable=name_var, width=40).grid(row=0, column=1)

ttk.Label(mainframe, text="Home Address:").grid(row=1, column=0, sticky=tk.W)
ttk.Entry(mainframe, textvariable=address_var, width=40).grid(row=1, column=1)

ttk.Label(mainframe, text="City and State:").grid(row=2, column=0, sticky=tk.W)
ttk.Entry(mainframe, textvariable=location_var, width=40).grid(row=2, column=1)

ttk.Label(mainframe, text="Business Name:").grid(row=3, column=0, sticky=tk.W)
ttk.Entry(mainframe, textvariable=business_name_var, width=40).grid(row=3, column=1)

ttk.Label(mainframe, text="Business Address:").grid(row=4, column=0, sticky=tk.W)
ttk.Entry(mainframe, textvariable=business_address_var, width=40).grid(row=4, column=1)

ttk.Label(mainframe, text="Asset:").grid(row=5, column=0, sticky=tk.W)
ttk.Entry(mainframe, textvariable=asset_var, width=40).grid(row=5, column=1)

ttk.Button(mainframe, text="Search", command=run_search).grid(row=6, column=0, pady=10)
ttk.Button(mainframe, text="Clear", command=clear_fields).grid(row=6, column=1, pady=10)

root.mainloop()