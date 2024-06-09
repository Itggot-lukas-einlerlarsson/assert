import ipaddress

class Machine():
    """
        Information expert regarding a machine in a network
    """

    def __init__(self):
        self.ipv4_address: ipaddress.IPv4Address = None
        self.network_gateway: Machine = None

    def __str__(self):
        return f"ipv4 address: {self.ipv4_address}, networkgateway: {self.network_gateway}"

