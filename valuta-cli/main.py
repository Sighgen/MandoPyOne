import argparse
import requests
import os
from dotenv import load_dotenv

# Indlæs .env
load_dotenv()

parser = argparse.ArgumentParser(description="Valuta CLI Tool")

parser.add_argument(
    "--key",
    type=str,
    help="API key"
)

args = parser.parse_args()

# Gem key i .env
if args.key:
    with open(".env", "w") as f:
        f.write(f"API_KEY={args.key}")
        api_key = args.key
else:
    api_key = os.getenv("API_KEY")

if not api_key:
    print("Ingen API key fundet!")
    exit()

# Valg af valuta
currency_choice = {
    "1": "USD",
    "2": "DKK",
    "3": "EUR"
}

print("\nVælg valuta: ")
print("1, USD")
print("2 DKK")
print("3. EUR")

choice = input("Valg: ")

if choice not in currency_choice:
    print("Findes ikke!")
    exit()

from_currency = currency_choice[choice]

print("\nTil valuta: ")
print("1 USD")
print("2 DKK")
print("3 EUR")

to_choice = input("Til valuta: ")

if to_choice not in currency_choice:
    print("Findes ikke!")
    exit()

to_currency = currency_choice[to_choice]

try:
    amount = float(input("beløb: "))
except ValueError:
    print("Beløb skal være et tal")
    exit()

# API kald
url = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/{from_currency}"

response = requests.get(url)
data = response.json()

if data["result"] != "success":
    print("Fejl i API kald.")
    exit()

rate = data["conversion_rates"][to_currency]
result = amount * rate

print(f"{amount} {from_currency} = {result:.2f} {to_currency}")    