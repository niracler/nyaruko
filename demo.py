import json
from telethon import TelegramClient, sync # type: ignore
import socks  # type: ignore

api_id = ''  # 请替换为您的 API ID
api_hash = ''  # 请替换为您的 API Hash

client = TelegramClient(
    'demo', 
    api_id, 
    api_hash,
    proxy=(socks.SOCKS5, '127.0.0.1', 823)
)

with client:
    client.start()
    channels_and_groups = []

    for dialog in client.get_dialogs():
        if dialog.is_channel or dialog.is_group:
            entity = client.get_entity(dialog.id)
            entity.access_hash = entity.access_hash if hasattr(entity, 'access_hash') else None
            entity.username = entity.username if hasattr(entity, 'username') else None

            item = {
                "name": entity.title,
                "id": entity.id,
                "access_hash": entity.access_hash,
                "type": "channel" if dialog.is_channel else "group",
                "link": f"https://t.me/{entity.username}" if entity.username else "私有或无链接"
            }
            channels_and_groups.append(item)
            print(item)

    with open('channels_and_groups.json', 'w') as f:
        f.write(json.dumps(channels_and_groups, ensure_ascii=False, indent=2))
