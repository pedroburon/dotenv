import argparse
from dotenv import get_variable, set_variable, get_variables, __version__


parser = argparse.ArgumentParser()

parser.add_argument("key", nargs='?')
parser.add_argument("value", nargs='?')

parser.add_argument('--file', default='.env')

parser.add_argument('--version', action='version', version=__version__)

parser.add_argument('--shell', action='store_true', default=False)

args = parser.parse_args()


if args.shell:
    PRINT_FORMAT = '%s=%s'
else:
    PRINT_FORMAT = '%s: %s'

if args.key is None:
    for key, value in get_variables(args.file).items():
        print(PRINT_FORMAT % (key, value))
elif args.value is None:
    print(PRINT_FORMAT % (args.key, get_variable(args.file, args.key)))
else:
    set_variable(args.file, args.key, args.value)
    print(PRINT_FORMAT % (args.key, args.value))
