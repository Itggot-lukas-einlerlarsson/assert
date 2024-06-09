import nmap3
import logging
import graphviz
import ipaddress
import netifaces
from assertt import get_logger
from assertt.machine import Machine

class MachineManager():
    """
        Class that scan whole network to find assets connected to the network.
        Then adding the information to a database
        Which can then be visualized via e.g. wizgraph
    """

    def __init__(self):
        self.logger = get_logger(__name__)
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

    def create_report(self):
        node_list = []
        for key, value in self.scanned_addresses.items():
            self.logger.info(f"key: {key}, value: {value}")
            node_list.append([key, value])
        # tree_to_graphviz(node_list, "test.dot")s
