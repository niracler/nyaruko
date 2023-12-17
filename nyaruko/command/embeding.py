"""
embeding telegram data
"""

import ast
import click
from openai import OpenAI
import pandas as pd
import numpy as np
import sqlite3
import sqlite_vss
from nyaruko.config import nyaruko_config


client = OpenAI(api_key=nyaruko_config["openai"]["api_key"])

def cosine_similarity(a, b):
    if isinstance(a, str):
        print(a)
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

def get_embedding(text, model="text-embedding-ada-002"):
    # skip if no string
    if not isinstance(text, str):
        return None

    text = text.replace("\n", " ")
    return client.embeddings.create(input = [text], model=model).data[0].embedding

@click.group()
def embeding():
    """
    embeding telegram data
    """
    print("")

@click.command()
def embeding_gen():
    """
    generate embeding data
    """
    db = sqlite3.connect(':memory:')
    db.enable_load_extension(True)
    sqlite_vss.load(db)
    db.enable_load_extension(False)
    version, = db.execute('select vss_version()').fetchone()
    print(version)

    df = pd.read_csv('channel_messages.csv')
    df['ada_embedding'] = df.text.apply(lambda x: get_embedding(x, model='text-embedding-ada-002'))
    df.to_csv('output/embedded_1k_reviews.csv', index=False)
    pd.set_option('display.max_rows', 100)
    df = df.dropna(subset=['ada_embedding'])
    print(df)

@click.command()
def embeding_cat():
    """
    read the embeding result
    """
    df = pd.read_csv('output/embedded_1k_reviews.csv')
    df = df.dropna(subset=['ada_embedding'])
    print(df)

@click.command()
@click.argument('desc', nargs=-1)  # 命令行中输入的所有非选项参数都会被接收为一个元组
def embeding_search(desc):
    """
    search the embeding result
    """
    product_description = desc[0]
    df = pd.read_csv('output/embedded_1k_reviews.csv')
    df = df.dropna(subset=['ada_embedding'])
    embedding = get_embedding(product_description, model='text-embedding-ada-002')
    df['similarities'] = df.ada_embedding.apply(lambda x: cosine_similarity(ast.literal_eval(x), embedding))
    df = df.dropna(subset=['similarities'])
    res = df.sort_values('similarities', ascending=False).head(10)
    print(res)

embeding.add_command(embeding_cat, "cat")
embeding.add_command(embeding_gen, "gen")
embeding.add_command(embeding_search, "search")
