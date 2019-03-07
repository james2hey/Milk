from datetime import datetime
from discord.ext.commands import CommandInvokeError
from discord.ext.commands import CommandNotFound


def log(result, context):
    log_message = '{}, command={}, author_id={}\n'

    if isinstance(result, CommandNotFound):
        log_message = '{}, NOT FOUND={}, author_id={}\n'
    elif isinstance(result, CommandInvokeError):
        log_message = '{}, ERROR={}, author_id={}\n'

    with open("LOGS.txt", "a") as log_file:
        log_file.write(log_message.format(datetime.now(), result, context.message.author))
    log_file.close()
