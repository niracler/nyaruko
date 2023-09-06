"""
statistic the articles in the folder
"""
import os
import re
import click
import yaml

skip_folder = [
    'backup',
    'media',
    '.obsidian',
    'templates',
]

BASE_PATH = '/Users/niracler/iCloud云盘（归档）/Obsidian/Note'

def list_article_as_tree(folder_path: str, level=0) -> int:
    """
    recursively list all the articles in the folder as tree
    """
    if os.path.basename(folder_path) in skip_folder:
        return 0

    count = 0
    file_list = os.listdir(folder_path)
    basedir = os.path.basename(folder_path)
    print(f"{level * '│  '}{basedir}")

    for file_name in file_list:
        file_path = os.path.join(folder_path, file_name)

        if file_path.endswith('.md') and os.path.isfile(file_path):
            count += 1

        elif os.path.isdir(file_path):
            count += list_article_as_tree(file_path, level + 1)

    if count > 0:
        print(f"{level * '│  '}└── ({count})")

    return count


@click.group()
def cli():
    """
    scan the folder
    """
    pass

@cli.command("list")
@click.option("--tree", "-t", is_flag=True, help="list the articles as tree")
@click.option("--tag", default="", help="list the articles with tag")
def list_articles(tree: bool, tag: str):
    """
    list the articles
    """
    if tree:
        list_article_as_tree(BASE_PATH, level=0)
        return

    file_headers = list_articles_with_tag(BASE_PATH, tag)
    # 打印提取的信息
    # for header in file_headers:
    #     print("Date:", header['date'])
    #     print("Tags:", header['tags'])
    #     print("---")


# TODO: list the articles with tag
# example:
# ---
# date: 2022-05-23
# tags:
#   - weekly1
#   - weekly2
#   - weekly3
# ---
# 定义一个函数来扫描文件头部信息
def list_articles_with_tag(base_path, tag:str):
    """
    list the articles with tag
    """
    header_pattern = re.compile(r'^---\n(.*?)\n---', re.DOTALL)
    headers = []

    for root, dirs, files in os.walk(base_path, topdown=True):
        # 检查是否需要跳过当前目录
        dirs[:] = [d for d in dirs if d not in skip_folder]

        for filename in files:
            file_path = os.path.join(root, filename)

            if not file_path.endswith('.md'):
                continue    # 跳过非 Markdown 文件

            with open(file_path, 'r', encoding='utf-8') as file:
                file_contents = file.read()

                match = header_pattern.search(file_contents)
                header_data = {
                    'date': 'N/A',
                    'tags': 'N/A',
                    'path': 'N/A'
                }

                if match:
                    header_content = match.group(1)

                    try:
                        header_object = yaml.load(header_content, Loader=yaml.FullLoader)
                        # print("Parsed Header Object:")
                        # print(header_object)
                    except yaml.YAMLError as error:
                        print("path:", file_path)
                        print("Error parsing YAML:", error)

                headers.append(header_data)

    return headers
