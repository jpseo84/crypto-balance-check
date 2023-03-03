import requests
import csv
import time

url = "https://blockchain.info/rawaddr/"

with open('btc_wallet.csv') as csv_file:
    csv_reader = csv.reader(csv_file)
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            # Skipping first row avoiding header
            line_count += 1
        else:
            # Read wallet address from csv file line by line
            wallet_address = row[0]

            # Check balance using API
            response = requests.get(url + wallet_address)
            if response.status_code == 200:
                result = response.json()
                if "final_balance" in result:
                    balance = float(result["final_balance"]) / 10**8  # Convert from satoshis to bitcoins
                    print(f"{wallet_address}: {balance}")
                else:
                    print(f"{wallet_address}: Error retrieving data")
            else:
                print(f"{wallet_address}: Error retrieving data - Error {response.status_code}")

            line_count += 1
            # Wait 11 seconds to avoid Blockchain.com's API limit, 1 per every 10 seconds
            time.sleep(11)
