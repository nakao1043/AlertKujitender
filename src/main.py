# モジュールの読み込み
import discord
import asyncio
from datetime import datetime
import time

# コンフィグファイルの読み込み
token = 'NjE1NDYwMDAyOTkxMTc3NzUx.XWOjyg.ma67t9A8yfbyvQrrd2D0epdiDak'

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

# メッセージ受信時に動作する処理
@client.event
async def on_message(message):
    # メッセージ送信者がBotだった場合は無視する
    if message.author.bot:
        return
    # 「/neko」と発言したら「にゃーん」が返る処理
    if message.content == '/neko':
        await message.channel.send('にゃーん')

client.run(token)