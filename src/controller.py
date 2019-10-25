# -*- coding: utf-8 -*-

import web
# from process import Process
from service import Service

render = web.template.render('templates/')

class Home(object):
	def __init__(self):
		super(Home, self).__init__()

	def GET(self):
		return render.index()

class Upload(object):
	def __init__(self):
		super(Upload, self).__init__()
		
	def POST(self):
		data = web.input(file = {})
		if 'file' in data:
			file = data.file
			Service().save(file.filename, file.file.read())

# TODO: Remove
# class Show(object):
# 	def __init__(self):
# 		super(Show, self).__init__()
	
# 	def GET(self):
# 		# Process().run()
# 		return render.index()
