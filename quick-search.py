import webbrowser

import urllib.parse

# List of websites with search URL patterns
SEARCH_SITES = {
    "OFAC": "https://sanctionssearch.ofac.treas.gov/",
    "Safer": "https://safer.fmcsa.dot.gov/CompanySnapshot.aspx?query_string={query}&searchtype=ANY",
    "Zillow": "https://www.zillow.com/homes/{query}_rb/",
    "NSOPW": "https://www.nsopw.gov/en/search-results?searchType=all&query={query}",
    "Truck Paper": "https://www.truckpaper.com/listings/for-sale/{query}",
}

def main():
    query = input("Enter the credit review search term: ").strip()
    if not query:
        print("No search term entered.")
        return

    encoded_query = urllib.parse.quote_plus(query)
    for name, url_pattern in SEARCH_SITES.items():
        url = url_pattern.format(query=encoded_query)
        print(f"Opening {name}...")
        webbrowser.open_new_tab(url)

if __name__ == "__main__":
    main()