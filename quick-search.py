import webbrowser
import urllib.parse
import subprocess
import time

def main():
    name = input("Enter Name: ").strip()
    address = input("Enter Address: ").strip()
    location = input("Enter City and State: ").strip()
    asset = input("Enter Asset: ").strip()
    business_name = input("Enter Business Name: ").strip()

    queries = {
        "OFAC": name,
        "NSOPW": name,
        "Zillow": address,
        "Safer": business_name,
        "Truck Paper": asset,
        "Google": name + " " + location,
    }

    SEARCH_SITES = {
        # "OFAC": "https://sanctionssearch.ofac.treas.gov/",
        # "NSOPW": "https://www.nsopw.gov/en/search-results?searchType=all&query={query}",
        "Zillow": "https://www.zillow.com/homes/{query}_rb/",
        "Safer": "https://safer.fmcsa.dot.gov/keywordx.asp?searchstring=%2A{query}%2A&SEARCHTYPE=",
        "Truck Paper": "https://www.truckpaper.com/listings?keywords={query}",
        "Google": "https://www.google.com/search?q={query}",
    }

    first = True
    for name, url_pattern in SEARCH_SITES.items():
        query = queries[name]
        if not query:
            print(f"Skipping {name} (no search term provided).")
            continue
        encoded_query = urllib.parse.quote_plus(query)
        url = url_pattern.format(query=encoded_query)
        print(f"Opening {name}...")
        if first:
            subprocess.Popen(f'start chrome --new-window "{url}"', shell=True)
            first = False
            time.sleep(0.5)  # Wait a moment to ensure the first window opens before opening new tabs
        else:
            subprocess.Popen(f'start chrome --new-tab "{url}"', shell=True)

if __name__ == "__main__":
    main()