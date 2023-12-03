import ipaddress
import GtaClient


def is_private_ip(ip):
    try:
        ip_obj = ipaddress.ip_address(ip)
        private_ranges = [
            ipaddress.ip_network('10.0.0.0/8'),
            ipaddress.ip_network('172.16.0.0/12'),
            ipaddress.ip_network('192.168.0.0/16')
        ]

        for private_range in private_ranges:
            if ip_obj in private_range:
                return True

        return False

    except ValueError:
        # Invalid IP address
        return False


class PcapHandler:
    def __init__(self):
        self._clients = {}
        self._routes = {}

    def parse_pcap(self, pcap_path: str)->None:
        # read pcap and add clients to list
        # check toDs and fromDs to find ap and station
        # add ap to router list with priority default_route
        # calculate priority for station:
        # 1. check if communicated with internet
        # 2. check if has both mac and ip saved (can be from prior packets)
        pass

    def get_clients(self)->list[GtaClient]:
        return list(self._clients.values())

    def get_routes(self)->list[GtaClient]:
        return list(self._routes.values())
