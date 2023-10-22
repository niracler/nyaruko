import sqlite3
import click


@click.command()
def list_article():
    """
    Lists all article from the sqlite.
    """
    conn = sqlite3.connect("db.sqlite3")
    c = conn.cursor()
    c.execute("SELECT * FROM article")
    articles = c.fetchall()
    for article in articles:
        click.echo(f"{article[0]} {article[1]}")
