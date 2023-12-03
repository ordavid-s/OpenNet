from GtaClient import GtaClient
from constants import *


class LogHandler:
    def __init__(self, logs_path: str):
        self._logs_path = logs_path

    def parse_logs(self) -> list[GtaClient]:
        client_list = {}
        with open(self._logs_path, "r") as log_file:
            for line in log_file.readlines():
                items = line.split(" ")
                client = GtaClient.empty_client()
                for item in items:
                    key_value = item.split(":")
                    client.set_value(key_value[0], key_value[1])
                client_list[client.identifier] = client
        return list(client_list.values())



    def write_logs(self, client: GtaClient, status: int) -> None:
        with open(self._logs_path, "a+") as log_file:
            log_file.write(f"{ClientFeatures.mac}:{client.identifier}"
                           f" {ClientFeatures.ip}:{client.ip} {ClientFeatures.status}:{status}")