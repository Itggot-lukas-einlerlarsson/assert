import nmap3
import logging
# import graphviz
from graphviz_tool import tree_to_graphviz
import ipaddress
import netifaces

#a = ipaddress.ip_network('192.0.2.0/24')
#print(a)

class Machine():
    """
        Information expert regarding a machine in a network
    """

    def __init__(self):
        self.ipv4_address: ipaddress.IPv4Address = None
        self.network_gateway: Machine = None

    def __str__(self):
        return f"ipv4 address: {self.ipv4_address}, networkgateway: {self.network_gateway}"


class MachineManager():
    """
        Class that scan whole network to find assets connected to the network.
        Then adding the information to a database
        Which can then be visualized via e.g. wizgraph
    """

    def __init__(self):
        logging.basicConfig(format = "[%(asctime)s] %(levelname)s:%(lineno)d -- %(message)s", level=logging.DEBUG)
        self.logger = logging.getLogger(__name__)
        self.logger.info("starting the AssetManager")
        self.nmapper = nmap3.Nmap()
        self.scanned_addresses = {}

    def scratch_scan_subnet(self, subnet: str):
        net = ipaddress.ip_network(subnet)
        print(dir(net))
        self.logger.info(f"scratch scanning network {subnet}, length: {len(list(net))}")
        for ip in net:
            self.logger.info(f"scanning ipaddress: {ip}")
            self.scanned_addresses[ip] = self.nmapper.nmap_version_detection(ip)

    def deep_scan_subnet(self, subnet: str):
        net = ipaddress.ip_network(subnet)
        self.logger.info(f"deep scanning network {subnet}, length: {list(len(net))}")
        for ip in net:
            self.logger.info(f"scanning ipaddress: {ip}")
            self.scanned_addresses[ip] = self.nmapper.scan_top_ports(ip)

    def create_report():
        node_list = []
        for key, value in self.scanned_addresses.items():
            node_list.append([key, value])
        tree_to_graphviz(node_list, "test.dot")

def main():
    test = AssetManager()
    test.scratch_scan_all_hosts(subnet="192.168.0.0/24")

if __name__ == "__main__":
    main()
