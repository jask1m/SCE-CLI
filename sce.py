from tools.setup import SceSetupTool
import argparse

setup = SceSetupTool()
parser = argparse.ArgumentParser()

parser.add_argument('--setup', dest='setup', action='store_true')
args = parser.parse_args()

if args.setup:
    setup.check_os()
    setup.check_docker()
    setup.check_mongo()

    setup.handle_setup()
else:
    print('did nothing wrong')