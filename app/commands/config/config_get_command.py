from socket import socket

from app.commands.abs_command import BaseCommand, SupportedCommands
from app.resp_parser import encode_resp
from app.globaldatastore import GlobalConfigStore


class ConfigGetCommand(BaseCommand):

    def __init__(self, args):
        super().__init__(SupportedCommands.GET, args)

    def parse_args(self, args: [str]) -> dict:
        if args[0] is None:
            raise Exception(f"{self.get_name()} requires config to get passed to it.")

        parsed_args = {"config": args[0]}

        return parsed_args

    def execute(self, conn: socket):
        val_obj = GlobalConfigStore.get_val(self.get_arg(key="config"))
        conn.send(encode_resp([self.get_arg(key="config"), val_obj], 'array_bulk_string'))
