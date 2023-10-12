"""
Nyaruko is a command line tool for nyaruko.
"""
import os
import click


@click.group()
def cli():
    """
    Nyaruko is a command line tool for nyaruko.
    """
    click.echo("Nyaruko is a command line tool for nyaruko.")


@cli.command("ascii")
@click.option("--big", is_flag=True, help="Print the big ascii art of nyaruko.")
def show_ascii(big):
    """
    Prints the ASCII art of nyaruko.
    """
    art_path = "data/ascii-art-big.txt" if big else "data/ascii-art.txt"
    with open(os.path.join(os.path.dirname(__file__), art_path), "r", encoding="utf-8") as file:
        click.echo(file.read())
