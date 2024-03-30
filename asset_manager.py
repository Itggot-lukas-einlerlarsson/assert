import nmap3
import logging
import ipaddress

class AssetManager():
    """
        Class that scan whole network to find assets connected to the network.
        Then adding the information to a database
        Which can then be visualized via e.g. wizgraph
    """

    def __init__():
        logging.basicConfig(format = "%(levelname)s:%(message)s", levet=logging.DEBUG)
        self.logger = getLogger(__name__)
        self.logger.info("Starting the AssetManager")

    def scan_all_hosts(subnet: str):
        pass

    def deep_scan_host(ip_address: str, ports: str):
        pass
