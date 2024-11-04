from datetime import datetime
from socket import socket

from app.commands.abs_command import BaseCommand, SupportedCommands
from app.resp_parser import encode_resp
from app.store import Store


class GetCommand(BaseCommand):

    def __init__(self, args):
        super().__init__(SupportedCommands.GET, args)

    def parse_args(self, args: [str]) -> dict:
        if args[0] is None:
            raise Exception(f"{self.get_name()} cannot have invalid key passed to it.")

        parsed_args = {"key": args[0]}

        return parsed_args

    def execute(self, conn: socket):
        val_obj = Store.get_val(self.get_arg(key="key"))
        expiry_dt = val_obj.get("expiry_dt")

        if expiry_dt and expiry_dt < datetime.now():
            Store.delete_val(self.get_arg(key="key"))
            conn.send(encode_resp(resp_type="null"))
        else:
            conn.send(encode_resp(val_obj.get("value"), 'bulk_string'))
