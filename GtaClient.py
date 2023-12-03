import ipaddress
from constants import *

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


class GtaClient:

    @staticmethod
    def empty_client():
        return GtaClient("", "", -1)

    def __init__(self, mac: str, ip: str, status: int):
        self._mac = mac
        self._ip = ip
        self._status = status

    @property
    def identifier(self):
        return self._mac

    @property
    def ip(self):
        return self._ip

    @property
    def status(self):
        return self._status

    def set_value(self, key: str, value: str):
        if key == ClientFeatures.mac:
            self._mac = value
            return

        if key == ClientFeatures.ip:
            self._ip = value
            return

        if key == ClientFeatures.status:
            self._status = int(value)
            return