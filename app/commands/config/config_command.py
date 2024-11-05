from socket import socket

from app.commands.abs_command import BaseCommand, SupportedCommands
from app.commands.config.config_get_command import ConfigGetCommand


class ConfigCommand(BaseCommand):

    def __init__(self, args):
        super().__init__(SupportedCommands.GET, args)

    def parse_args(self, args: [str]) -> dict:
        if len(args) < 1:
            raise Exception(f"{self.get_name()} cannot have invalid sub-command passed to it.")

        parsed_args = {"sub_command": args[0], "sub_command_args": args[1:] or []}

        return parsed_args

    def _get_sub_command(self):
        sub_command_args = self.get_arg("sub_command_args")
        match self.get_arg("sub_command"):
            case "GET":
                return ConfigGetCommand(sub_command_args)

    def execute(self, conn: socket):
        self._get_sub_command().execute(conn)
