#!/usr/bin/python3
import requests
import re


recomments = "<\W*--.*?--\W*>"
rejscomments = "//.*"
rejsinhtml = "<script>(.*)</script>"
recssinhtml = "<style>(.*)</style>"
recsscomments = "\/\*.*\*\/"


def huntcomments(f):
		#knowcomments = []
		for url in f:
			finds = []
			#matchcomments(i)
			
			a = re.sub("\n|%0a", "", url)
			#print(a)
			response = requests.get(a, allow_redirects=True)
			# HTML Comments
			for comment in re.findall(recomments, response.text):
				finds.append(comment)
			# Tag script in html
			for scripttag in re.findall(rejsinhtml, response.text):
				# js Comments in tag script
				for commenttag in re.findall(rejscomments, scripttag):
					finds.append(commenttag)
			# Tag style in html
			for csstag in re.findall(recssinhtml, response.text):
				# css comments in tag script
				for commenttag in re.findall(recsscomments, csstag):
					finds.append(commenttag)
			# Comments in js files
			if (a.endswith(".js")):
				for js in re.findall(rejscomments, response.text):
					finds.append(js)
			if (a.endswith(".css")):
				for css in re.findall(recsscomments, response.text, re.DOTALL):
					finds.append(css)			
			if len(finds) > 0:
				print( "\n[+] " + str(response.status_code) + " " + url)
				for find in finds:
					#if find not in knowcomments:
					if len(find) > 240:
						print(find[:240])
						print("[...]\n")
					else:
						print(find)
					#knowcomments.append(find)
			else:
				if arguments.verbose:
					print(str(response.status_code) + " " + url)


def huntfromfile():
	with open(arguments.file) as f:
		huntcomments(f)

if __name__ == '__main__':
	import argparse
	parser = argparse.ArgumentParser(description = 'commentsHunter. An simple script to hunt comments in URL\'s Created by @jcesrstef.')
	parser.add_argument('--file', '-f',action = 'store', dest = 'file', required = True, help = 'File with URL\'s to scan, one per line.')
	parser.add_argument('--verbose', '-v', action='store_true', required=False, help='Show requests')

	arguments = parser.parse_args()

	huntfromfile()
