"""
embedding telegram data
"""

import ast
import click
from openai import OpenAI
import pandas as pd
import numpy as np
from tabulate import tabulate
from nyaruko.config import nyaruko_config


client = OpenAI(api_key=nyaruko_config["openai"]["api_key"])


def get_embedding(text, model="text-embedding-ada-002"):
    """
    获取文本的嵌入向量。
    """
    text = text.replace("\n", " ")
    return client.embeddings.create(input=[text], model=model).data[0].embedding

def cosine_similarity(a, b):
    """
    计算两个向量的余弦相似度。
    """
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))


@click.command()
def embedding_gen():
    """
    生成教程文本嵌入向量数据。
    """
    df = pd.read_csv('channel_messages.csv')  # 读取 CSV 文件到 DataFrame
    df['text_with_date'] = df['date'] + " " + df['text']  # 拼接日期和文本
    df['ada_embedding'] = df.text_with_date.apply(get_embedding)  # 批量应用文本嵌入函数

    del df['text_with_date']  # 删除 'text_with_date' 列
    df.to_csv('embedded_1k_reviews.csv', index=False)  # 保存结果到新的 CSV 文件
    
    # 打印 DataFrame 的前几行进行确认
    print(df.head())


@click.command()
def embedding_cat():
    """
    read the embedding result
    """
    df = pd.read_csv('embedded_1k_reviews.csv')
    df = df.dropna(subset=['ada_embedding'])
    print(df)


@click.command()
@click.argument('desc', nargs=-1)  # 命令行中输入的所有非选项参数都会被接收为一个元组
def embedding_search(desc):
    """
    search the embedding result
    """
    product_description = desc[0]
    df = pd.read_csv('embedded_1k_reviews.csv')
    embedding = get_embedding(product_description)
    df['similarities'] = df.ada_embedding.apply(
        lambda x: cosine_similarity(ast.literal_eval(x), embedding)
    )
    df = df.sort_values(by='similarities', ascending=False)  # 按相似度降序排列
    df = df.drop(columns=['ada_embedding', 'id'])  # 删除嵌入向量列
    print(tabulate(df.head(10), headers='keys', tablefmt='psql', maxcolwidths=60))


@click.group()
def embedding_group():
    """
    embedding telegram data
    """
    pass


embedding_group.add_command(embedding_cat, "cat")
embedding_group.add_command(embedding_gen, "gen")
embedding_group.add_command(embedding_search, "search")
