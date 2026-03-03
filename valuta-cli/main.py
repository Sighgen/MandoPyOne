import argparse
import requests
import os
from dotenv import load_dotenv

# Indlæs .env
load_dotenv

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

# Bruger input
from_currency = input("Fra valuta: ").upper()
to_currency = input("Til valuta: ").upper()
amount = float(input("Beløb: "))

# API kald
url = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/from_curency"

response = requests.get(url)
data = response.json()

if data["result"] != "succes":
    print("Fejl i API kald.")
    exit()

rate = data["conversion_rates"][to_currency]
result = amount * rate

print(f"{amount} {from_currency} = {result:.2f} to_currency")    