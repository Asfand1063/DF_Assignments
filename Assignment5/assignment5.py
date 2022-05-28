import yara
import argparse

parser=argparse.ArgumentParser(description='match any YARA signatures against a file')
parser.add_argument('file',help='the file to run signatures against')
parser.add_argument('-r',help='a single yara rule to match for')
arg=parser.parse_args()
rules=yara.compile(filepath=arg.r)
print(rules.match(arg.file))
