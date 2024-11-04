from socket import socket

from app.commands.abs_command import BaseCommand, SupportedCommands
from app.resp_parser import encode_resp


class EchoCommand(BaseCommand):

    def __init__(self, args):
        super().__init__(SupportedCommands.ECHO, args)

    def parse_args(self, args: [str]) -> dict:
        if args[0] is None:
            raise Exception(f"{self.get_name()} cannot have invalid key passed to it.")

        return {"key": args[0]}

    def execute(self, conn: socket):
        conn.send(encode_resp(self.get_arg(key="key")))
