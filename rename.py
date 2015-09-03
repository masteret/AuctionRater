import os

path = os.getcwd() + "/_IEADL/"
for filename in os.listdir(path):
	if filename.startswith("4\\") or filename.startswith("5\\"):
		os.rename(os.path.join(path, filename), os.path.join(path, filename[2:]))