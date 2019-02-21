#!/usr/bin/env python

# WS client example

import asyncio
import websockets
import json
import struct
 
async def hello():
    async with websockets.connect(
            'wss://ws.zerodha.com/?api_key=kitefront&user_id=DP4281&public_token=KIPHbdXwLwdI1XokAAUGODuE7gIdrJ9m&uid=1538825074164&user-agent=kite3-web&version=1.9.28') as websocket:

        message = '{"a": "subscribe", "mode": "ltp' \
                  '", "v": [884737, 408065]}'
        await websocket.send(message)

        while True:
            greeting = await websocket.recv()
            print(len(greeting))
            if len(greeting) > 93:
                print(struct.unpack('>hhiiiiiiiiiiihiiiiiiiiiii', greeting)) # format string
            else:
                print(greeting)

asyncio.get_event_loop().run_until_complete(hello())
