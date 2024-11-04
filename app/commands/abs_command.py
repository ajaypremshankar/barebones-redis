import enum
from abc import abstractmethod
from socket import socket
from enum import Enum

class SupportedCommands(Enum):
    SET = "SET",
    GET = "GET",
    ECHO = "ECHO",
    PING = "PING"


class BaseCommand:
    def __init__(self, name, args=None):
        self.parsed_args = self.parse_args(args)
        self.name: SupportedCommands = name
        self.args = args

    def get_name(self) -> SupportedCommands:
        return self.name

    def get_arg(self, key=None, index=None, default_val=None):

        if key:
            return self.parsed_args.get(key, default_val)

        if index and index < len(self.args):
            return self.args[index] or default_val

        raise Exception("Invalid arg requested")

    @abstractmethod
    def parse_args(self, args: [str]) -> dict:
        pass

    @abstractmethod
    def execute(self, conn: socket):
        pass
