# モジュールの読み込み
import discord
import asyncio
from datetime import datetime
import time

# Tokenの読み込み
token = 'NjE1NDYwMDAyOTkxMTc3NzUx.XWPEsw.zUkOOWAE821Xh1K8Ea_3RzlXUZk'

# クライアント接続オブジェクト
client = discord.Client()

# Alert Kujitender 
@client.event
async def on_ready():
    CHANNEL_ID=615477635715432462
    channel = client.get_channel(CHANNEL_ID)
    await channel.send('AlermBot Awaken!')
    while True:
        if datetime.now().weekday() == 5:
            if datetime.now().hour == 20:
                if datetime.now().minute == 00:
                    await channel.send('くじテンダー結果発表まであと1時間！')
                    time.sleep(3300)
                    await channel.send('くじテンダー結果発表まであと5分！')
                    break
        time.sleep(60)

    while True:
        time.sleep(601500)
        await channel.send('くじテンダー結果発表まであと1時間！')
        time.sleep(3300)
        await channel.send('くじテンダー結果発表まであと5分！')

client.run(token)