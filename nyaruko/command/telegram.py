"""
export telegram data
"""

import csv
import click
import socks
from telethon import TelegramClient
from telethon.tl.functions.messages import (GetHistoryRequest)
from nyaruko.config import nyaruko_config

proxy = (socks.SOCKS5, 'me.niracler.com', 8235)
api_id = nyaruko_config["telegram"]["api_id"]
api_hash = nyaruko_config["telegram"]["api_hash"]
client = TelegramClient('demo', api_id, api_hash, proxy=proxy)


@click.command()
def telegram():
    """
    export telegram data
    """
    with client:
        client.loop.run_until_complete(main())


async def main():
    """
    Lists all article from the sqlite.
    """

    await client.start()

    print("Client Created")

    # 替换为目标频道的username或者频道id，如果你有权限的话
    channel_username = 'niracler_channel'
    channel_entity = await client.get_input_entity(channel_username)

    # 获取频道中的所有消息
    offset_id = 0
    all_messages = []
    limit = 100

    while True:
        history = await client(GetHistoryRequest(
            peer=channel_entity,
            offset_id=offset_id,
            offset_date=None,
            add_offset=0,
            limit=limit,
            max_id=0,
            min_id=0,
            hash=0
        ))
        if not history.messages:
            break

        for message in history.messages:
            message_dict = {
                'id': message.id,
                # Convert datetime to string if not None
                'date': message.date.strftime('%Y-%m-%d %H:%M:%S') if message.date else None,  
                # Get the user_id if from_id is not None
                'sender_id': message.from_id.user_id if message.from_id else None, 
                'text': message.message
            }
            all_messages.append(message_dict)
        offset_id = history.messages[-1].id
        print("Messages: ", len(all_messages))

        headers = ['id', 'date', 'sender_id', 'text']
        # 将消息保存到 csv 文件中
        with open('channel_messages.csv', 'w', encoding='utf-8', newline='') as f:
            writer = csv.DictWriter(f, headers)
            writer.writeheader()
            for message in all_messages:
                writer.writerow(message)

        
