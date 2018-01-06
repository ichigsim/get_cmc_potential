import urllib.request
import json
import pandas as pd

def main():
    url = 'https://api.coinmarketcap.com/v1/ticker/?limit=100'
    response = urllib.request.urlopen(url)
    cmc_ticker = json.loads(response.read().decode('utf8'))
    
    print(response)

    btc_supply = float(cmc_ticker[0]['available_supply'])
    btc_price_usd = float(cmc_ticker[0]['price_usd'])

    all_id = []
    all_supply = []
    all_price = []
    potential_result = []

    #  (ビットコイン発行数/アルト発行数)
    for i in range(len(cmc_ticker) - 1):
        all_id.append(cmc_ticker[i + 1]['id'])
        all_supply.append(float(cmc_ticker[i + 1]['available_supply']))
        all_price.append(float(cmc_ticker[i + 1]['price_usd']))

        potential_result.append(round(((btc_price_usd / (all_supply[i] / btc_supply)) / all_price[i]), 2))

    potential_df = pd.DataFrame({'id': all_id, 'potential_result': potential_result}, index=list(range(2, len(cmc_ticker) + 1)))

    potential_df.to_csv('cmc_coin_potential.csv')

if __name__ == '__main__':
    main()