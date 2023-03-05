import csv
import requests
import time

def check_balance(currency, address):
    if currency == 'BTC':
        api_url = f"https://blockchain.info/rawaddr/{address}"
        response = requests.get(api_url).json()
        return response['final_balance'] / 10**8
    elif currency == 'ETH':
        api_url = f"https://api.etherscan.io/api?module=account&action=balance&address={address}&tag=latest&apikey=YourApiKeyToken"
        response = requests.get(api_url).json()
        return int(response['result']) / 10**18
    elif currency == 'XRP':
        api_url = f"https://data.ripple.com/v2/accounts/{address}/balances"
        response = requests.get(api_url).json()
        for balance in response['balances']:
            if balance['currency'] == 'XRP':
                return float(balance['value'])
        return None
    else:
        return "Not supported currency"

with open('wallet.csv', 'r') as csvfile:
    csv_reader = csv.reader(csvfile)
    for row in csv_reader:
        currency = row[0]
        address = row[1]
        balance = check_balance(currency, address)
        if balance is not None:
            print(f"{currency} - {address}: {balance}")
        else:
            print(f"{currency} - {address}: Error retrieving data")
        time.sleep(11)
