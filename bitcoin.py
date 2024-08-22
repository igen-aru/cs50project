import sys
import requests

def get_bitcoin_price():
    try:
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        response.raise_for_status()
        data = response.json()
        return data['bpi']['USD']['rate_float']
    except requests.RequestException as e:
        print(f"Error fetching Bitcoin price: {e}")
        sys.exit(1)

def main():
    if len(sys.argv) != 2:
        print("Usage: python script.py <number_of_bitcoins>")
        sys.exit(1)

    try:
        n = float(sys.argv[1])
    except ValueError:
        print("Error: Number of Bitcoins must be a valid number.")
        sys.exit(1)

    bitcoin_price = get_bitcoin_price()
    total_cost = n * bitcoin_price

    print(f"The current cost of {n} Bitcoins is ${total_cost:,.4f}")

if __name__ == "__main__":
    main()
