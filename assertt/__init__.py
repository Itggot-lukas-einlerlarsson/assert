__version__ = "1.0.0"

import logging

logging.basicConfig(format = "[%(asctime)s] %(levelname)s:%(lineno)d -- %(message)s", level=logging.DEBUG)
master_logger = logging.getLogger(__name__)

def get_logger(scriptname: str):
    return master_logger.getChild(scriptname)
