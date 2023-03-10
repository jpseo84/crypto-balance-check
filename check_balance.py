import csv
import requests
import time

def check_balance(currency, address):
    #BTC balance request using API from Blockchain.info, free
    if currency == 'BTC':
        api_url = f"https://blockchain.info/rawaddr/{address}"
        response = requests.get(api_url).json()
        return response['final_balance'] / 10**8
    
    #Ethereum balance request using API from etherscan.io, free tier
    elif currency == 'ETH':
        api_url = f"https://api.etherscan.io/api?module=account&action=balance&address={address}&tag=latest&apikey=YourApiKeyToken"
        response = requests.get(api_url).json()
        return int(response['result']) / 10**18

    #Ripple balance request using API from Ripple, free
    elif currency == 'XRP':
        api_url = f"https://data.ripple.com/v2/accounts/{address}/balances"
        response = requests.get(api_url).json()
        for balance in response['balances']:
            if balance['currency'] == 'XRP':
                return float(balance['value'])
        return None

    #Litecoin(LTC) balance request using Blockcypher's API, free tier
    elif currency == 'LTC':
        api_url = f"https://api.blockcypher.com/v1/ltc/main/addrs/{address}/balance"
        response = requests.get(api_url).json()
        return response['balance'] / 10**8
    
    #Dogecoin(DOGE) balance request using Blockcypher's API, free tier
    elif currency == 'DOGE':
        api_url = f"https://api.blockcypher.com/v1/doge/main/addrs/{address}/balance"
        response = requests.get(api_url).json()
        return response['balance'] / 10**8

    else:
        return "Not supported currency"

with open('wallet.csv', 'r') as csvfile:
    csv_reader = csv.reader(csvfile)
    for row in csv_reader:
        currency = row[0]
        address = row[1]
        balance = check_balance(currency, address)
        if balance is not None:
            print(f"{currency},{address},{balance}")
        else:
            print(f"{currency},{address},'Error retrieving data'")
        time.sleep(11)
