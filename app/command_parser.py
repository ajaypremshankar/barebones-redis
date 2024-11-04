import re

from app.models import FiredCommand


# def test(command_arr: [str]):


def parse(raw_command: str):
    match = re.search(r'^\*(\d+)\r\n', raw_command)

    if not match:
        raise Exception(f"Invalid start of the command: {raw_command}")

    command_len = int(match.group(1))

    if command_len <= 0:
        raise Exception("Empty command passed")

    raw_command_and_params = raw_command.split("\r\n", maxsplit=1)[1]

    command_and_params_arr = raw_command_and_params.split("$")[1:] # skip empty string

    command = command_and_params_arr[0].split("\r\n")[1]

    raw_params = command_and_params_arr[1:]

    params = []

    for rp in raw_params:
        params.append(rp.split("\r\n")[1])


    return FiredCommand(command, params)










