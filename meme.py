import argparse

parser = argparse.ArgumentParser()

parser.add_argument('--setup', dest='setup', action='store_true')

args = parser.parse_args()

print(args.setup)
if args.setup:
    print('ok im gonna set up')
else:
    print('did nothing wrong')
