"""
statistic the articles in the folder
"""
import os
import click

skip_folder = [
    'backup',
    'media',
    '.obsidian',
]

BASE_PATH = '/Users/niracler/iCloud云盘（归档）/Obsidian/Note'


def list_markdown_files(folder_path: str, level=0) -> int:
    """
    recursively list all markdown files in the folder
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
            count += list_markdown_files(file_path, level + 1)

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
def list_articles():
    """
    list the articles
    """
    list_markdown_files(BASE_PATH, level=0)
