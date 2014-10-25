#!/usr/bin/python

import os
import sys
import getopt
import git

limit = 0

try:
	author = sys.argv[1]
except:
	print 'please provide at least one parameter'
	print 'codereview.py <username> [-n]' 
	sys.exit(2)

try:
	opts, args = getopt.getopt(sys.argv[2:], "n:")
except getopt.GetoptError:
	print 'invalid parameters'
	print 'codereview.py <username> [-n]'
	sys.exit(2)
for opt, arg in opts:
	if opt == '-n':
		limit = arg

count = 0
repos = {};
limit = int(limit)

print "searching repositories..."

for root, subdirs, files in os.walk(os.getcwd()):
	head = None
	config = None
	description = None
	for file in files:
		if file == 'HEAD':
			head = True
		if file == 'config':
			config = True
		if file == 'description':
			description = True
	
	if head and config:
		g = git.Git(root)
		loginfo = g.log('--author=' + author, '--format=%ar', '-n 1', '--all')
		logkey = g.log('--author=' + author, '--format=%at', '-n 1', '--all')
		if loginfo and logkey:
			repos[logkey] = loginfo + '\t' + root
			count += 1

i = 0
for key in sorted(repos, reverse=True):
	print repos[key]
	i += 1
	if limit and i > limit:
		break

print('Total Repositories: ' + str(count))

