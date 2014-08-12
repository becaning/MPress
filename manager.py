# /usr/bin/env python
# -*- coding:utf8 -*-

__author__ = 'becaning'

import sys
import os
import shutil
import mpress


#Install theme
def installtheme(themename):
	oldtheme  = './blog/static'
	theme   = os.path.join('./themes/',themename,'static')
	if os.path.isdir(olddir):
		# shutil.copytree(olddir,backdir)
		shutil.rmtree(oldtheme)

	if os.path.isdir(theme):
		shutil.copytree(theme,oldtheme)

#Clean all blog file
def clean():
	filelist = os.listdir('./blog/')
	for f in filelist:
		f = './blog/'+f
		if os.path.isfile(f):
			os.remove(f)

if __name__ == '__main__':
	try:
		Subcmd = sys.argv[1]
	except Exception, e:
		print 'Do Nothing...'
		exit()

	if 'genall' == sys.argv[1]:
		index = mpress.IndexPage()
		index.genIndex()
		post = mpress.PostPage()
		post.genAllposts()
	elif 'clean' == sys.argv[1]:
		clean()
	else:
		print 'Subcommand not fount'
