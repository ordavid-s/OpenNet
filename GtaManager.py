import LogHandler
import ClientHeap
from GtaClient import GtaClient
import PcapHandler
import ConnectionHandler
from constants import *


class GtaManager:
    def __init__(self, pcap_list: list[str], logs_path="./gta_logs.txt"):
        self._pcap_list = pcap_list
        self._log_handler = LogHandler.LogHandler(logs_path)
        self._client_list = ClientHeap.ClientHeap()
        self._route_list = ClientHeap.ClientHeap()
        self._pcap_analyzer = PcapHandler.PcapHandler()
        self._connection_handler = ConnectionHandler.ConnectionHandler()

    def load_logs(self)->None:
        old_clients = self._log_handler.parse_logs()
        for client in old_clients:
            if client.type == GtaClient.type_client:
                self._client_list.add_client(client)
            if client.type == GtaClient.type_route:
                self._route_list.add_client(client)

    def start_analyzing(self, force_client_retry=True)->None:
        for pcap in self._pcap_list:
            self._pcap_analyzer.parse_pcap(pcap)

        for client in self._pcap_analyzer.get_clients():
            # if to ignore logs and force trying pcap clients
            if force_client_retry:
                self._client_list.add_client(client)
                self._log_handler.write_logs(client, OpCodes.NOT_TRIED)
            # if to not ignore clients found in logs
            else:
                if not self._client_list.is_included(client):
                    self._client_list.add_client(client)
                    self._log_handler.write_logs(client, OpCodes.NOT_TRIED)

        # loops over possible routes identified in pcap
        for route in self._pcap_analyzer.get_routes():
            # if to ignore logs and force trying pcap clients
            if force_client_retry:
                self._route_list.add_client(route)
                self._log_handler.write_logs(route, OpCodes.NOT_TRIED)
            # if to not ignore routes found in logs
            else:
                if not self._client_list.is_included(route):
                    self._client_list.add_client(route)
                    self._log_handler.write_logs(route, OpCodes.NOT_TRIED)

    def start_spoofing(self, interface: str)->None:
        client = self._client_list.pop_client()
        # Runs over clients and tries them by order of client priority
        while client:
            for route in self._route_list:
                result = self._connection_handler.test_connection(interface, client, route)
                if result:
                    self._log_handler.write_logs(client, OpCodes.SUCCESS)
                    self._log_handler.write_logs(route, OpCodes.SUCCESS)
                    return
                else:
                    self._log_handler.write_logs(route, OpCodes.UNKNOWN)

            # if tried all routes and all failed then mark client as failed
            self._log_handler.write_logs(client, OpCodes.FAIL)




