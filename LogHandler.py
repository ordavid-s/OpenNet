import GtaClient
from constants import *


class LogHandler:
    def __init__(self, logs_path: str):
        self._logs_path = logs_path

    def parse_logs(self) -> list[GtaClient]:
        pass

    def write_logs(self, client: GtaClient, status: int) -> None:
        pass