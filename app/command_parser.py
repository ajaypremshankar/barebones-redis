import re

from app.commands.abs_command import BaseCommand, SupportedCommands
from app.commands.echo_command import EchoCommand
from app.commands.get_command import GetCommand
from app.commands.ping_command import PingCommand
from app.commands.set_command import SetCommand


def get_command(command: str, args: [str]):
    match SupportedCommands[command.upper()]:
        case SupportedCommands.PING:
            return PingCommand(args)
        case SupportedCommands.ECHO:
            return EchoCommand(args)
        case SupportedCommands.SET:
            return SetCommand(args)
        case SupportedCommands.GET:
            return GetCommand(args)


def parse(raw_command: str) -> BaseCommand:
    match = re.search(r'^\*(\d+)\r\n', raw_command)

    if not match:
        raise Exception(f"Invalid start of the command: {raw_command}")

    command_len = int(match.group(1))

    if command_len <= 0:
        raise Exception("Empty command passed")

    raw_command_and_params = raw_command.split("\r\n", maxsplit=1)[1]

    command_and_params_arr = raw_command_and_params.split("$")[1:]  # skip empty string

    command = command_and_params_arr[0].split("\r\n")[1].upper()

    raw_params = command_and_params_arr[1:]

    params = []

    for rp in raw_params:
        params.append(rp.split("\r\n")[1])

    return get_command(command, args=params)
