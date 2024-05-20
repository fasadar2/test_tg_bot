from commands import *


def generate_help_message():
    message = "Приветствую, вот список команд, которые я могу выполнить:\n"
    for key, value in commands.items():
        message += f"{key}: {value}\n"
    return message
