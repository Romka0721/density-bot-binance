import asyncio
from binance import AsyncClient, BinanceSocketManager
from search_density import search, symbol_dict


# async def main():
    # client = await AsyncClient.create()
    # bm = BinanceSocketManager(client)
    # if symbol_dict:
    #     for i in symbol_dict:
    #         print(i)






        # ts = bm.trade_socket('BNBUSDT')
        # async with ts as tscm:
        #     while True:
        #         res = await tscm.recv()
        #         print(res)
        #
        # await client.close_connection()

if __name__ == "__main__":
    search()
    # loop = asyncio.get_event_loop()
    # loop.run_until_complete(main())
