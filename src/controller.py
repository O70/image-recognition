# -*- coding: utf-8 -*-

import web
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
			metadata = Service().saveImage(file.filename, file.file.read())
			print(metadata)
