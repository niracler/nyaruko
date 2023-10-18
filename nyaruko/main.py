"""
Nyaruko is a command line tool for nyaruko.
"""
import os
import configparser
import click
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

config = configparser.ConfigParser()
config.read('config.ini')


async def telegram_start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """
    Handles the /start command.
    """
    await update.message.reply_text(
        f"Hi! {update.message.from_user.first_name}. I'm Nyaruko, your personal assistant. " +
        "I'm still under development, but you can talk to me if you want."
    )


@click.group()
@click.option('--debug/--no-debug', default=False, help="Print debug messages.")
@click.pass_context
def cli(ctx, debug):
    """
    This is the main entry point for nyaruko.
    """
    ctx.ensure_object(dict)
    ctx.obj['DEBUG'] = debug


@cli.command("ascii")
@click.option("--big", is_flag=True, help="Print the big ascii art of nyaruko.")
def show_ascii(big):
    """
    Prints the ASCII art of nyaruko.
    """
    art_path = "data/ascii-art-big.txt" if big else "data/ascii-art.txt"
    with open(os.path.join(os.path.dirname(__file__), art_path), "r", encoding="utf-8") as file:
        click.echo(file.read())


@cli.command("bot")
@click.option("--daemon", is_flag=True, help="Run the bot as a daemon.")
def run_bot(daemon):
    """
    Runs the telegram bot.
    """
    if not daemon:
        click.echo(
            "Hi! I'm Nyaruko, your personal assistant. "
            "I'm still under development, but you can talk to me if you want."
        )
        return None

    app = ApplicationBuilder().get_updates_proxy_url(config["telegram"]["proxy"]).token(
        config["telegram"]["token"]).build()

    app.add_handler(CommandHandler("start", telegram_start))
    app.run_polling()
