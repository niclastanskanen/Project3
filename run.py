import gspread
from google.oauth2.service_account import Credentials
import random #import random module
from words import words
import pyfiglet

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('hangman_highscore')


highscore = SHEET.worksheet('highscore')

data = highscore.get_all_values()



welcome_message = pyfiglet.figlet_format("Welcome")
print(welcome_message)

input("Do you want to play? [Y/N]\n")
input("Whats your name?\n")