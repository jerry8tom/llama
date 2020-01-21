import alpaca_trade_api as tradeapi
import threading
import time
import datetime

APCA_API_BASE_URL = "https://paper-api.alpaca.markets"

def restBalance (public_k, secret_k):
    api = tradeapi.REST (public_k, secret_k, APCA_API_BASE_URL, 'v2')
    account = api.get_account()

    if account.trading_blocked:
        print('Account is currently restricted from trading.')

    return account.buying_power

