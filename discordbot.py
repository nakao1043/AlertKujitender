# モジュールの読み込み
import discord
import asyncio
from datetime import datetime
import time

# Tokenの読み込み
token = 'NjE1NDYwMDAyOTkxMTc3NzUx.XWPKEg.PDxE4C840_Y4ODKnURY9OfoaZmk'

# クライアント接続オブジェクト
client = discord.Client()

# Alert Kujitender 
@client.event
async def on_ready():
    CHANNEL_ID=601765601983332376
    channel = client.get_channel(CHANNEL_ID)
    await channel.send('AlermBot Awaken!')
    while True:
        if datetime.now().weekday() == 5:
            if datetime.now().hour == 20:
                if datetime.now().minute == 00:
                    await channel.send('くじテンダー引き換え期間まであと1時間です。交換してない人は急ぎましょう。')
                    time.sleep(3300)
                    await channel.send('くじテンダー結果発表まであと5分！')
                    time.sleep(300)
                    await channel.send('くじテンダーの結果が発表されました！')
                    break
        print('待機中・・・')
        time.sleep(60)

    while True:
        print('週間待機モードに入ります')
        time.sleep(601200)
        await channel.send('くじテンダー引き換え期間まであと1時間です。交換してない人は急ぎましょう。')
        time.sleep(3300)
        await channel.send('くじテンダー結果発表まであと5分！')
        time.sleep(300)
        await channel.send('くじテンダーの結果が発表されました！')
        
client.run(token)