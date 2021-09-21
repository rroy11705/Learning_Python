import argparse


parse = argparse.ArgumentParser(description="test")

parse.add_argument('count', action='store', type=int)
parse.add_argument('units', action='store')

print(parse.parse_args())

