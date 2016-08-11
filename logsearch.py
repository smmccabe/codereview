#!/usr/bin/python

import os
import sys
import getopt
import git

limit = 0

try:
	message = sys.argv[1]
except:
	print 'please provide at least one parameter'
	print 'logsearch.py <message> [-n]' 
	sys.exit(2)

try:
	opts, args = getopt.getopt(sys.argv[2:], "n:")
except getopt.GetoptError:
	print 'invalid parameters'
	print 'logsearch.py <username> [-n]'
	sys.exit(2)
for opt, arg in opts:
	if opt == '-n':
		limit = arg

output = ''
limit = int(limit)

print "searching repositories..."

for root, subdirs, files in os.walk(os.getcwd()):
	head = None
	config = None
	for file in files:
		if file == 'HEAD':
			head = True
		if file == 'config':
			config = True
	
	if head and config:
		try:
			g = git.Git(root)
			loginfo = g.log('--grep=' + message, '--all')
		except:
			print 'Errored reading repository: ' + root
		if loginfo:
			output += loginfo + '\n'

print(output)

