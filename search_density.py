from binance.client import Client
from threading import Thread
import time


from config import api_key, api_secret
from settings import min_density_future, min_density_spot


client = Client(api_key, api_secret)
file = open('symbol.txt', 'r')

symbol_dict = {}


def symbol_book_future():
    while True:
        for line in file:
            symbol = line.strip()
            try:
                order_book = client.futures_order_book(symbol=symbol)
                order_book_bids = order_book['bids'] + order_book['asks']
                for i in order_book_bids:
                    sum_bids = float(i[0])*float(i[1])
                    if sum_bids > min_density_future:
                        symbol_dict[symbol] = (i[0], sum_bids)
            except Exception as ee:
                print(f'{symbol} : {ee}')
        file.seek(0)
        print(symbol_dict)
        time.sleep(60)


def symbol_book_spot():
    while True:
        for line in file:
            symbol = line.strip()
            try:
                order_book = client.get_order_book(symbol=symbol)
                order_book_bids = order_book['bids'] + order_book['asks']
                for i in order_book_bids:
                    sum_bids = float(i[0])*float(i[1])
                    if sum_bids > min_density_spot:
                        symbol_dict[symbol] = (i[0], sum_bids)
            except Exception as ee:
                print(f'{symbol} : {ee}')
        file.seek(0)
        print(symbol_dict)
        time.sleep(60)


def search():
    Thread(target=symbol_book_future).start()
    Thread(target=symbol_book_spot).start()


if __name__ == "__main__":
    search()
