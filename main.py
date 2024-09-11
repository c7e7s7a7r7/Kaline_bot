import json
import numpy as np
import talib
from binance.client import Client
import websocket
from secrets import api_key, api_secret

TRADE_SYMBOL = 'BTCUSDT'
TIME_INTERVAL = Client.KLINE_INTERVAL_1MINUTE
close = []
"""
def main():
    symbol = TRADE_SYMBOL
    tvm = ThreadedWebsocketManager(api_key,api_secret)
    tvm.start()

    def handle_socket(msg):
        print(f"message type: {msg['e']}")
        print(msg)

    tvm.start_kline_socket(callback=handle_socket(),symbol=symbol)

    tvm.start_depth_socket(callback=handle_socket_message,symbol=symbol)

    streams = ['btcusdt@miniTicker','btcusdt@bookTicker']
    tvm.start_multiplex_socket(callback=handle_socket_message,streams=streams)
    tvm.join()
"""
def on_open(ws):
    print("opened connection")
def on_close(ws):
    print("closed connection")
def on_message(ws,message):
    global close

    json_message = json.loads(message)

    candle = json_message('k')

    is_candle_close = json_message('x')

    close = candle['c']

    if is_candle_closed:
        closes.append(float(close))
        np_closes = np.array(closes)
if __name__ == "__main__":

    client = Client(api_key,api_secret,testnet=True)
    klines = client.get_historical_klines(TRADE_SYMBOL, TIME_INTERVAL, "1 day ago UTC",limit=10)

    print(klines)

    for candle in range(len(klines) - 1):
        close.append(float(klines[candle][4]))

    SOCKET = 'wss://stream.binance.com:9443/ws/'+TRADE_SYMBOL.lower()+'@kline_'+TIME_INTERVAL
    ws = websocket.WebSocketApp(SOCKET, on_open=on_open,on_close=on_close,on_message=on_message)
    ws.run_forever()

