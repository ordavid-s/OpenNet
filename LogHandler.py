from GtaClient import GtaClient
from constants import *


class LogHandler:
    def __init__(self, target_ssid: str, logs_path: str):
        self._logs_path = logs_path
        self._target_ssid = target_ssid
        self._delimiter = "-"

    def parse_logs(self) -> list[GtaClient]:
        client_list = {}
        with open(self._logs_path, "r") as log_file:
            for line in log_file.readlines():
                line = line.rstrip("\n")
                if line:
                    try:
                        items = line.split(" ")
                        client = GtaClient.empty_client()
                        to_add_client = True
                        for item in items:
                            key_value = item.split(self._delimiter)
                            if key_value[0] == ClientFeatures.ssid:
                                # if log from another network skip log
                                # if from this network skip to client values
                                if key_value[1] != self._target_ssid:
                                    to_add_client = False
                                    break
                                else:
                                    continue
                            client.set_value(key_value[0], key_value[1])
                        if to_add_client:
                            client_list[client.identifier] = client
                    except:
                        pass # bad line in logs
        return list(client_list.values())



    def write_logs(self, client: GtaClient, status: int) -> None:
        with open(self._logs_path, "a+") as log_file:
            log_file.write(f"{ClientFeatures.ssid}{self._delimiter}{self._target_ssid}"
                           f" {ClientFeatures.client_type}{self._delimiter}{client.type}"
                           f" {ClientFeatures.mac}{self._delimiter}{client.identifier}"
                           f" {ClientFeatures.ip}{self._delimiter}{client.ip}"
                           f" {ClientFeatures.status}{self._delimiter}{status}"
                           f" {ClientFeatures.priority}{self._delimiter}{client.priority}\n")