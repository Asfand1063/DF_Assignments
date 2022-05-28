import hashlib
from pathlib import Path
import argparse
import os
import sys

parser=argparse.ArgumentParser()
parser.add_argument('dir1')
parser.add_argument('dir2')
arg=parser.parse_args()

# Lists of files and directories of both directories
files_in_dir1 = list()
files_in_dir2 = list()
directories_in_dir1 = list()
directories_in_dir2 = list()

# Lists od hashes of files and directories of both directories
file_hashes_in_dir1 = list()
directory_hashes_in_dir1 = list()
file_hashes_in_dir2 = list()
directory_hashes_in_dir2 = list()

def print_files_and_directories():
	print("Directory 1:")
	for elem in files_in_dir1:
		print(elem)
	print("\n\n")
	for elem in directories_in_dir1:
		print(elem)
	print("\n\nDirectory 2:")
	
	for elem in files_in_dir1:
		print(elem)
	print("\n\n")
	for elem in directories_in_dir1:
		print(elem)

def md5_update_from_dir(directory, hash):
	for path in sorted(Path(directory).iterdir(), key=lambda p: str(p).lower()):
		hash.update(path.name.encode())
		#print(path)
		if path.is_file():
			with open(path, "rb") as f:
				for chunk in iter(lambda: f.read(4096), b""):
					hash.update(chunk)
		elif path.is_dir():
			hash = md5_update_from_dir(path, hash)
	return hash

def md5_dir(directory):
	return md5_update_from_dir(directory, hashlib.md5()).hexdigest()

def md5_file1(file1):
	md5 = hashlib.md5()
	with open(file1, 'rb') as f:
		while True:
			data = f.read(65536)
			if not data:
				break
			md5.update(data)
	file_hashes_in_dir1.append(md5.hexdigest())
	# print("MD5: {0}".format(md5.hexdigest()))

def md5_file2(file1):
	md5 = hashlib.md5()
	with open(file1, 'rb') as f:
		while True:
			data = f.read(65536)
			if not data:
				break
			md5.update(data)
	file_hashes_in_dir2.append(md5.hexdigest())
	# print("MD5: {0}".format(md5.hexdigest()))

def compare_hashes():
	for i in file_hashes_in_dir1:
		for j in file_hashes_in_dir2:
			if (i==j):
				file_hashes_in_dir1.remove(i)
				file_hashes_in_dir2.remove(j)
				break
				
	
hash1 = md5_dir(arg.dir1)
hash2 = md5_dir(arg.dir2)
if(hash1 == hash2): # If hash of given directories is same
	print("\n\n\t\tDirectories have no difference")
	print(hash1)
	print(hash2)
else: # If hash is not same then traverse each element in directory, take hashes and compare
	for (dirpath, dirnames, filenames) in os.walk(arg.dir1):
		files_in_dir1 += [os.path.join(dirpath, file) for file in filenames]
		directories_in_dir1 += [os.path.join(dirpath, dir) for dir in dirnames]

	for (dirpath, dirnames, filenames) in os.walk(arg.dir2):
		files_in_dir2 += [os.path.join(dirpath, file) for file in filenames]
		directories_in_dir2 += [os.path.join(dirpath, dir) for dir in dirnames]

	# Sort the lists	
	files_in_dir1.sort()
	directories_in_dir1.sort()
	files_in_dir2.sort()
	directories_in_dir2.sort()
	
	for files in files_in_dir1:
		md5_file1(files)
	for files in files_in_dir2:
		md5_file2(files)
	compare_hashes()
	for files in file_hashes_in_dir1:
		print(files)
	print("\n\n")
	for files in file_hashes_in_dir2:
		print(files)

