# Quick Search Tool

A simple desktop application for quickly searching customer and business information across multiple online resources. Built with Python and Tkinter.

## Features

- Enter customer and business details once, then search multiple sites with one click.
- Opens search results in Google Chrome (new window and tabs).
- Supports searches on:
  - Pacer
  - OFAC
  - NSOPW
  - Secretary of State (Ohio and all states)
  - Zillow
  - Safer
  - Truck Paper
  - Google (Customer & Business)

## Requirements

- **Windows** (tested)
- **Python 3.7+**
- **Google Chrome** installed and in your system PATH

## Installation

1. **Clone or Download** this repository.
2. Ensure `quick_search_gui.py` and (optionally) `HCS Logo.ico` are in the same folder.
3. (Optional) Install required Python packages (Tkinter is included with most Python installations).

## Usage

1. Open a terminal in the project folder.
2. Run the application:

   ```
   python quick_search_gui.py
   ```

3. Enter the relevant information in the fields:
   - Customer Name
   - Home Address
   - City and State
   - Business Name
   - Business Address
   - Asset

4. Click **Search** to open all relevant search sites in Chrome.
5. Click **Clear** to reset all fields.

## Notes

- The app will attempt to use `HCS Logo.ico` as the window icon if present.
- If Chrome is not your default browser, it will still open Chrome directly.
- If you see a security warning when running an `.exe` version, click **More info** > **Run anyway**.

## Packaging as an EXE (Optional)

To distribute as a standalone `.exe`, use [PyInstaller](https://pyinstaller.org/):

```
pip install pyinstaller
pyinstaller --onefile --windowed quick_search_gui.py
```

Place `HCS Logo.ico` in the same directory as the `.exe` for the icon to appear.

---

**For questions or support, contact your IT
