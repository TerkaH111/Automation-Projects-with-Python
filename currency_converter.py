import requests

API_KEY = ""  # Your API key. Register @ https://freecurrencyapi.com/
BASE_URL = f"https://api.freecurrencyapi.com/v1/latest?apikey={API_KEY}"
CURRENCIES = ["USD", "CAD", "CZK", "EUR", "AUD", "CNY"]


#  func to utilize the URL
def convert_currency(base):
    if base not in CURRENCIES:
        print("Invalid currency. Please enter again.")
        return None

    currencies = ",".join(CURRENCIES)  # elements from a list converted into a string with comma separator
    url = f"{BASE_URL}&base_currency={base}&currencies={currencies}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        return data.get("data", {})
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None
    except ValueError:
        print("Invalid response format.")
        return None


while True:
    base = input("Enter the base currency (Q for Quit): ").upper()

    if base == "Q":
        break

    data = convert_currency(base)
    if not data:
        continue

    del data[base]
    print("\nCurrency\tValue")
    print("---------------------")
    for currency, value in data.items():
        print(f"{currency}\t\t{value}")
