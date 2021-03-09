import websockets
import time
import asyncio
import json
import serial
import time
arduino = serial.Serial(port='/dev/cu.usbmodem14101', baudrate=115200, timeout=.1)

class WebsocketController:
    def __init__(self):
        self.uri = "ws://34.82.37.10:6789"
        self.request = json.dumps({'action': 'request'})

    async def loop(self):
        num_fails = 0
        while True:
            try:
                async with websockets.connect(self.uri) as self.ws:
                    num_fails = 0
                    state = await self.ws.recv()
                    print(f'Startup State: {state}')
                    while True:
                        value = arduino.readline()
                        value = int.from_bytes(value, "big") 
                        print(value) # printing the value

                        #if controlling y axis
                        if value == 1:
                            await self.moveY(-10)
                        elif value == 2:
                            await self.moveY(10)

                        #if controlling x axis
                        # if value == 1:
                        #     await self.moveX(-10)
                        # elif value == 2:
                        #     await self.moveX(10)

                        time.sleep(.30)
            except Exception as e:
                print(f'Error: {e}')
                num_fails += 1
                if num_fails < 10:
                    print('Connection Error! Reestablishing connection...')
                else:
                    print(f'Connection failed {num_fails} times. Exiting.')
                    break


    async def moveY(self, amount):
        data = json.dumps({
            'action': 'movey',
            'value': amount
        })
        await self.ws.send(data)

    async def moveX(self, amount):
        data = json.dumps({
            'action': 'movex',
            'value': amount
        })
        await self.ws.send(data)

if __name__ == "__main__":
    dc = WebsocketController()
    asyncio.get_event_loop().run_until_complete(dc.loop())
    dc.s.close()