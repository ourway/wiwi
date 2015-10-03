

import argparse
import shutil
import os

boilerplate_dir = os.path.abspath(os.path.join(os.path.dirname(__file), '../', 'boilerplate/')) 



def main():
    parser = argparse.ArgumentParser(
        prog='wiwi', description="WIWI, among the tops!")



    parser.add_argument("-c", '--create',  type=str, action="store",
                        help="create a new app")

    args = parser.parse_args()
    if args.serve:
        server(args.port)
