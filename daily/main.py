import configparser
import yaml
from trello import TrelloClient

config = configparser.ConfigParser()
config.read('config.ini')


trello_client = TrelloClient(
    api_key=config["defaut"]["api_key"],
    api_secret=config["defaut"]["api_secret"],
    token=config["defaut"]["token"]
)
all_boards = trello_client.list_boards()
last_board = all_boards[0]
print(last_board.name)
print(all_boards[0].list_lists()[4].name)
print(all_boards[0].list_lists()[4].id)


with open("docs/2023/08-3.yml", 'r', encoding='utf-8') as f:
    yml_str = f.read()
data = yaml.safe_load(yml_str)

card_id = data.get('random', {})['id']
comment = data.get('daily', {})

print(comment[-1]['cn'])

# comment to card id

card = trello_client.get_card(card_id)
print(card.name)
card.comment(comment[-1]['cn'])

print("done")






