import ipaddress

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
    def __init__(self, **kwargs):
        self.src_mac = kwargs['srcMac']
        self.dst_mac = kwargs['dstMac']
        self.src_ip = kwargs['src_ip']
        self.dst_ip = kwargs['dst_ip']
        self.timestampSeconds = kwargs['timestamp']

    @property
    def identifier(self):
        return self.src_mac