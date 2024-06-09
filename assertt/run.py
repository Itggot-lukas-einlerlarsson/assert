import argparse
from assertt  import get_logger
from assertt.machine_manager import MachineManager

def parse_args():
    parser = argparse.ArgumentParser(description="Application description")
    parser.add_argument("--subnet", "-s", dest="subnet", type=str, action="store", required=True, help="Subnet of scan")
    parser.add_argument("--graph", "-g", dest="graph", action="store_true", default=False, help="Create graphviz")
    #parser.add_argument("--intparam", "-i", dest="intparam", type=int, action="store", default=0, help="Int parameter")
    #parser.add_argument("--append", "-a", dest="append_list", action='append', default=[], help="Add values to a list")
    return parser.parse_args()


def main():
    args = parse_args()
    test = MachineManager()
    test.scratch_scan_subnet("192.168.0.0/30")

if __name__ == "__main__":
    main()
