import re
import argparse
import os

parser=argparse.ArgumentParser(description='match any regex signatures against a file')
parser.add_argument('directory',help='the file to run regex against')
parser.add_argument('-r',help='a single regex rule to match for')
arg=parser.parse_args()
regex=re.compile(arg.r)

#path = os.walk(arg.directory)
#f = open("file_in_", "w")

listOfFiles = list()
for (dirpath, dirnames, filenames) in os.walk(arg.directory):
	listOfFiles += [os.path.join(dirpath, file) for file in filenames]
	
# Print the files    
for elem in listOfFiles:
	content = open(elem, 'r').read()
	print(regex.search(content),"		",elem)   

#f.close()
