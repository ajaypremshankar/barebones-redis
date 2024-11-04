from socket import socket

from app.commands.abs_command import BaseCommand, SupportedCommands
from app.resp_parser import encode_resp


class PingCommand(BaseCommand):
    def __init__(self, args):
        super().__init__(SupportedCommands.PING, {})

    def parse_args(self, args: [str]) -> dict:
        return {}

    def execute(self, conn: socket):
        conn.send(encode_resp("PONG"))