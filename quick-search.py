import webbrowser
import urllib.parse

def main():
    name = input("Enter Name: ").strip()
    address = input("Enter Address: ").strip()
    asset = input("Enter Asset: ").strip()
    business_name = input("Enter Business Name: ").strip()

    queries = {
        "OFAC": name,
        "NSOPW": name,
        "Zillow": address,
        "Safer": business_name,
        "Truck Paper": asset,
    }

    SEARCH_SITES = {
        "OFAC": "https://sanctionssearch.ofac.treas.gov/",
        "NSOPW": "https://www.nsopw.gov/en/search-results?searchType=all&query={query}",
        "Zillow": "https://www.zillow.com/homes/{query}_rb/",
        "Safer": "https://safer.fmcsa.dot.gov/CompanySnapshot.aspx?query_string={query}&searchtype=ANY",
        "Truck Paper": "https://www.truckpaper.com/listings?keywords={query}",
    }

    for name, url_pattern in SEARCH_SITES.items():
        query = queries[name]
        if not query:
            print(f"Skipping {name} (no search term provided).")
            continue
        encoded_query = urllib.parse.quote_plus(query)
        url = url_pattern.format(query=encoded_query)
        print(f"Opening {name}...")
        webbrowser.open_new_tab(url)

if __name__ == "__main__":
    main()