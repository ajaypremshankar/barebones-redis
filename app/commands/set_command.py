import datetime
from socket import socket

from app.commands.abs_command import BaseCommand, SupportedCommands
from app.resp_parser import encode_resp
from app.store import Store


class SetCommand(BaseCommand):
    def __init__(self, args: [str]):
        super().__init__(SupportedCommands.SET, args)

    def get_name(self):
        return self.name

    def parse_args(self, args: [str]) -> dict:

        if args[0] is None:
            raise Exception(f"{self.get_name()} cannot have invalid key passed to it.")

        parsed_args = {'key': args[0], 'value': args[1]}

        lowered_args = list((arg.upper() for arg in args))

        if "EX" in lowered_args:
            val_at = lowered_args.index("EX") + 1
            parsed_args["EX"] = int(lowered_args[val_at])

        if "PX" in lowered_args:
            val_at = lowered_args.index("PX") + 1
            parsed_args["PX"] = int(lowered_args[val_at])

        return parsed_args

    def execute(self, conn: socket):

        expiry_dt = None

        if self.get_arg(key="EX"):
            expiry_dt = (datetime.datetime.now() + datetime.timedelta(seconds=int(self.get_arg(key="EX"))))
        elif self.get_arg(key="PX"):
            expiry_dt = (datetime.datetime.now() + datetime.timedelta(milliseconds=int(self.get_arg(key="PX"))))

        Store.set_val(self.get_arg(key="key"), {
            "value": self.get_arg(key="value"),
            "expiry_dt": expiry_dt
        })

        conn.send(encode_resp("OK"))
