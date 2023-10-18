"""
Nyaruko is a command line tool for nyaruko.
"""
import click
from nyaruko.command.ascii import show_ascii
from nyaruko.command.bot import run_bot
from nyaruko.command.sync import sync
from nyaruko.command.list import list_article


@click.group()
@click.option('--debug/--no-debug', default=False, help="Print debug messages.")
@click.pass_context
def cli(ctx, debug):
    """
    This is the main entry point for nyaruko.
    """
    ctx.ensure_object(dict)
    ctx.obj['DEBUG'] = debug


cli.add_command(sync)
cli.add_command(show_ascii, "ascii")
cli.add_command(list_article, "list")
cli.add_command(run_bot, "bot")
