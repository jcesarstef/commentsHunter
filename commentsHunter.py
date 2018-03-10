#!/usr/bin/python3
import requests
import re
import argparse

parser = argparse.ArgumentParser(description = 'commentsHunter. An simple script to hunt comments in URL\'s Created by @jcesrstef.')
parser.add_argument('--file', '-f',action = 'store', dest = 'file', required = True, help = 'File with URL\'s to scan, one per line.')
arguments = parser.parse_args()

comments = "<\W*--.*?--\W*>"

with open(arguments.file) as f:
	knowcomments = []
	for i in f:
		#knowcomments = []
		a = re.sub("\n|%0a", "", i)
		response = requests.get(a, allow_redirects=True)
		finds = re.findall(comments, response.text)
		if len(finds) > 0:
			print( "\n[+] " + str(response.status_code) + " " + i)
			for find in finds:
				if find not in knowcomments:
					print(find)
				knowcomments.append(find)
