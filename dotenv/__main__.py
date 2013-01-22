import argparse
from dotenv import get_variable, set_variable, get_variables


parser = argparse.ArgumentParser()

parser.add_argument("key", nargs='?')
parser.add_argument("value", nargs='?')

parser.add_argument('--file', default='.env')

args = parser.parse_args()

if args.key is None:
	for key, value in get_variables(args.file).items():
		print "%s: %s" % (key, value)
elif args.value is None:
	print "%s: %s" % (args.key, get_variable(args.file, args.key))
else:
	set_variable(args.file, args.key, args.value)