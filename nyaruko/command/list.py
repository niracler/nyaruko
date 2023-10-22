import os
import click

from nyaruko.config import config


@click.command()
def list_article():
    """
    Lists all article from the sqlite.
    """
    article_dir = config["default"]["article_dir"]

    for root, _, files in os.walk(article_dir):
        for file in files:
            if file.endswith(".md"):
                article_path = os.path.join(root, file)[len(article_dir) + 1:]
                click.echo(article_path)
