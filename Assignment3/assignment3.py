import yara
import argparse
import os

parser=argparse.ArgumentParser(description='match any YARA signatures against a file')
parser.add_argument('directory',help='the file to run signatures against')
parser.add_argument('-r',help='a single yara rule to match for')
arg=parser.parse_args()
rules=yara.compile(arg.r)

# path = os.walk(arg.directory)
# f = open("file_in_", "w")

listOfFiles = list()
for (dirpath, dirnames, filenames) in os.walk(arg.directory):
	listOfFiles += [os.path.join(dirpath, file) for file in filenames]
	
# Print the files    
for elem in listOfFiles:
	print(rules.match(elem),"		",elem)    

		
# f.close()
