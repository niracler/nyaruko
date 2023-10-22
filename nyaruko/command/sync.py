"""
Convert article from obsidian to SQLite
"""
import os
import sqlite3
import click
from nyaruko.config import nyaruko_config

@click.command()
def sync():
    """
    Syncs the obsidian article to the sqlite.
    """
    article_dir = nyaruko_config["default"]["article_dir"]
    block_dir_list = nyaruko_config["default"]["block_dir_list"]
    create_article_table()

    # insert article
    for root, _, files in os.walk(article_dir):
        for file in files:
            if file.endswith(".md"):
                article_path = os.path.join(root, file)[len(article_dir) + 1:]
                # FIXME: some wrong here
                if article_path.startswith(tuple(block_dir_list)):
                    continue
                with open(os.path.join(root, file), "r", encoding="utf-8") as f:
                    article_content = f.read()
                article_title = file[:-3]
                click.echo(f"Inserting {article_title}...")
                insert_article(article_title, article_content, article_path)


def create_article_table():
    """
    Creates the database table.
    """
    conn = sqlite3.connect("db.sqlite3")
    c = conn.cursor()
    c.execute("DROP TABLE IF EXISTS article")
    c.execute("""
        CREATE TABLE IF NOT EXISTS article (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title STRING NOT NULL,
            content TEXT NOT NULL,
            path STRING NOT NULL,
            create_time INTEGER NOT NULL,
            update_time INTEGER NOT NULL
        )
    """)
    conn.commit()
    conn.close()

def insert_article(title, content, path):
    """
    Inserts article into database.
    """
    conn = sqlite3.connect("db.sqlite3")
    c = conn.cursor()
    c.execute("""
        INSERT INTO article (title, content, path, create_time, update_time)
        VALUES (?, ?, ?, ?, ?)
    """, (title, content, path, 0, 0))
    conn.commit()
    conn.close()
