#!/usr/bin/python

import os 

def run(**args):
	print "[*] In dirlister module."
	files = os.listdir(".")
	return sstr(files)


