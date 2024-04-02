import pandas as pd
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from gspread_dataframe import set_with_dataframe

class basicInfoGS:
    def __init__(self, SpreadsheetKey, kisyumei, SERVICE_ACCOUNT_FILE, SCOPES):
        self.credentials = ServiceAccountCredentials.from_json_keyfile_name(SERVICE_ACCOUNT_FILE, SCOPES)
        self.SpreadsheetKey = SpreadsheetKey
        self.kisyumei = kisyumei
        self.gs = gspread.authorize(self.credentials)
        self.workbook = self.gs.open_by_key(self.SpreadsheetKey)
        self.worksheet = self.workbook.worksheet(self.kisyumei)
        self.df = pd.DataFrame(self.worksheet.get_all_values())

    def pdPrint(self):
        print(self.df)