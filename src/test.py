from datetime import datetime
import asyncio
import time

while True:
    if datetime.now().weekday() == 0:
        print('曜日OK')
        if datetime.now().hour == 19:
            print('時OK')
            if datetime.now().minute == 10:
                print('Alert successfull!')
            time.sleep(10)