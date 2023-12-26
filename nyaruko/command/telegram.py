"""
export telegram data
"""

import csv
import click
import socks
from telethon import TelegramClient
from telethon.tl.functions.messages import GetHistoryRequest
from nyaruko.config import nyaruko_config

# 设置 TelegramClient，连接到 Telegram API
client = TelegramClient(
    'demo',
    nyaruko_config["telegram"]["api_id"],
    nyaruko_config["telegram"]["api_hash"],
    proxy=(socks.SOCKS5, 'me.niracler.com', 8235)
)

async def export_to_csv(filename, fieldnames, data):
    """
    将数据导出到 CSV 文件中。

    参数:
    filename -- 导出文件的名称
    fieldnames -- CSV 头部字段名称列表
    data -- 要导出的字典列表
    """
    with open(filename, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)

async def fetch_messages(channel_username):
    """
    获取指定频道的所有消息。

    参数:
    channel_username -- 目标频道的用户名
    """
    channel_entity = await client.get_input_entity(channel_username)
    offset_id = 0  # 初始消息 ID 偏移量
    all_messages = []  # 存储所有消息的列表

    while True:
        # 请求消息记录
        history = await client(GetHistoryRequest(
            peer=channel_entity,
            offset_id=offset_id,
            offset_date=None,
            add_offset=0,
            limit=100,  # 每次请求的消息数量
            max_id=0,
            min_id=0,
            hash=0
        ))
        if not history.messages:  # 当没有更多消息时结束循环
            break

        for message in history.messages:
            if message.message:  # 仅处理有文本内容的消息
                # 将消息序列化为字典形式
                message_dict = {
                    'id': message.id,
                    'date': message.date.strftime('%Y-%m-%d %H:%M:%S'),
                    'text': message.message
                }
                all_messages.append(message_dict)
        offset_id = history.messages[-1].id
        print(f"Fetched messages: {len(all_messages)}")
    return all_messages

async def main():
    """
    主程序：从指定频道获取消息并保存到 CSV 文件中。
    """
    await client.start()  # 启动 Telegram 客户端
    print("Client Created")

    channel_username = 'niracler_channel'  # 你要抓取的 Telegram 频道用户名
    all_messages = await fetch_messages(channel_username)  # 获取消息

    # 定义 CSV 文件的头部，并导出
    headers = ['id', 'date', 'text']
    await export_to_csv('channel_messages.csv', headers, all_messages)

# 当该脚本作为主程序运行时
if __name__ == '__main__':
    client.loop.run_until_complete(main())

@click.command()
def telegram():
    """
    export telegram data
    """
    with client:
        client.loop.run_until_complete(main())
