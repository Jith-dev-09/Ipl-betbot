import os
from dotenv import load_dotenv
import gspread
from google.oauth2.service_account import Credentials

# ✅ Load environment variables from .env file
load_dotenv()

# ✅ Read values from .env
SHEET_NAME = os.getenv("GOOGLE_SHEET_NAME")
CREDS_PATH = os.getenv("GOOGLE_CREDENTIALS_PATH")

def connect_google_sheet():
    try:
        # Set the scope for accessing Google Sheets
        scopes = ["https://www.googleapis.com/auth/spreadsheets"]

        # Load service account credentials
        creds = Credentials.from_service_account_file(CREDS_PATH, scopes=scopes)

        # Authorize and open the sheet
        client = gspread.authorize(creds)
        sheet = client.open(SHEET_NAME)

        print("✅ Connected to Google Sheet successfully!")

        # Example: read the first 5 rows from 'MatchSchedule' tab
        match_schedule = sheet.worksheet("MatchSchedule")
        rows = match_schedule.get_all_values()

        print("\n📅 First 5 rows from 'MatchSchedule':")
        for row in rows[:5]:
            print(row)

    except Exception as e:
        print("❌ Failed to connect to Google Sheet.")
        print("Error:", e)

if __name__ == "__main__":
    connect_google_sheet()
