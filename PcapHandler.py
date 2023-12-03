import GtaClient


class PcapHandler:
    def __init__(self):
        self._clients = {}

    def parse_pcap(self, pcap_path: str)->None:
        # read pcap and add clients to list
        pass

    def get_clients(self)->list[GtaClient]:
        return list(self._clients.values())
