"""
Convert article from obsidian to SQLite
"""
import click

@click.command()
def sync():
    """
    Syncs the obsidian article to the database.
    """
    click.echo("Syncing...")
