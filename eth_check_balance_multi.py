import requests
import csv
import time

url = "https://api.etherscan.io/api?module=account&action=balance&tag=latest"

api_key = "FWSIQ8ZQE5HXFEF5RQPVZ42R1S8SXGW2R9"

with open('eth_wallet.csv') as csvfile:
    csv_reader = csv.reader(csvfile)
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            line_count += 1
        else:
            wallet_address = row[0]

            # Check balance using Etherscan.io API
            response = requests.get(f"{url}&apikey={api_key}&address={wallet_address}")
            if response.status_code == 200:
                result = response.json()
                if result['status'] == '1':
                    balance = int(result['result']) / 10**18  # Convert from wei to ether
                    print(f"{wallet_address}: {balance}")
                else:
                    print(f"{wallet_address}: Error retrieving data")
            else:
                print(f"{wallet_address}: Error retrieving data - Error {response.status_code}")
            line_count += 1
            
            time.sleep(11)

