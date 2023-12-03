import LogHandler
import ClientHeap
import PcapHandler
import ConnectionHandler
from constants import *


class GtaManager:
    def __init__(self, pcap_list: list[str], logs_path="./gta_logs.txt"):
        self._pcap_list = pcap_list
        self._log_handler = LogHandler.LogHandler(logs_path)
        self._client_list = ClientHeap.ClientHeap()
        self._pcap_analyzer = PcapHandler.PcapHandler()
        self._connection_handler = ConnectionHandler.ConnectionHandler()

    def load_logs(self)->None:
        old_clients = self._log_handler.parse_logs()
        for client in old_clients:
            self._client_list.add_client(client)

    def find_route(self):


    def start_analyzing(self, force_client_retry=True)->None:
        for pcap in self._pcap_list:
            self._pcap_analyzer.parse_pcap(pcap)

        for client in self._pcap_analyzer.get_clients():
            if force_client_retry:
                self._client_list.add_client(client)
                self._log_handler.write_logs(client, OpCodes.NOT_TRIED)
            else:
                if not self._client_list.is_included(client):
                    self._client_list.add_client(client)
                    self._log_handler.write_logs(client, OpCodes.NOT_TRIED)

    def start_spoofing(self, interface: str)->None:
        client = self._client_list.pop_client()
        while client:
            result = self._connection_handler.test_connection(interface, client)
            if result:
                self._log_handler.write_logs(client, OpCodes.SUCCESS)
                return
            else:
                self._log_handler.write_logs(client, OpCodes.FAIL)


