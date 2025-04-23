import gspread
from oauth2client.service_account import ServiceAccountCredentials

def connect_gsheet(sheet_name):
    # Scope akses: Google Sheets dan Google Drive
    scope = [
        "https://spreadsheets.google.com/feeds",
        "https://www.googleapis.com/auth/spreadsheets",
        "https://www.googleapis.com/auth/drive"
    ]

    # Autentikasi dengan credentials JSON
    creds = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scope)
    client = gspread.authorize(creds)

    # Buka spreadsheet berdasarkan nama file
    spreadsheet = client.open(sheet_name)
    return spreadsheet

sheet = connect_gsheet("data")
produk_sheet = sheet.worksheet("Product")
data = produk_sheet.get_all_records()
