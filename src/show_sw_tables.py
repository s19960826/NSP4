#!/usr/bin/env python

import argparse
from time import sleep
import os
import subprocess

_THIS_DIR = os.path.dirname(os.path.realpath(__file__))
_THRIFT_BASE_PORT = 22222

parser = argparse.ArgumentParser(description='P4 demo')
parser.add_argument('--swname', help='Switch Name',
                    type=str, action="store", required=True)
args = parser.parse_args()

def main():
    # Get Thrift Port
    sw_name = args.swname
    index = int(sw_name[1:])-1
    thrift_port = _THRIFT_BASE_PORT+index
    
    cmd = "python /home/wpq/NSP4/src/simple_switch_CLI --thrift-port %d < /home/wpq/NSP4/src/cmd/show_tables.txt" % thrift_port
    os.system(cmd)

if __name__ == '__main__':
    main()
