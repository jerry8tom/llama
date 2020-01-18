import alpaca_trade_api as tradeapi
import threading
import time
import datetime

API_KEY = "PK6PRNSO137JXGLH1LZ0"
API_SECRET = "X1cfuvOJN/BuNYCm0BhxawkmGw640JS/NeCQt1Y/"
APCA_API_BASE_URL = "https://paper-api.alpaca.markets"

if __name__ == "__main__":
    api = tradeapi.REST (API_KEY, API_SECRET, APCA_API_BASE_URL, 'v2')
    account = api.get_account()

    if account.trading_blocked:
        print('Account is currently restricted from trading.')

    #check balance
    print ('${} is available as buying power.'.format(account.buying_power))

    stocks = ['AAPL', 'TSLA']
    

