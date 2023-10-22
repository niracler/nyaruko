import click
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from nyaruko.config import nyaruko_config

async def telegram_start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """
    Handles the /start command.
    """
    await update.message.reply_text(
        f"Hi! {update.message.from_user.first_name}. I'm Nyaruko, your personal assistant. " +
        "I'm still under development, but you can talk to me if you want."
    )

@click.command("bot")
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

    app = ApplicationBuilder().get_updates_proxy_url(nyaruko_config["telegram"]["proxy"]).token(
        nyaruko_config["telegram"]["token"]).build()

    app.add_handler(CommandHandler("start", telegram_start))
    app.run_polling()
