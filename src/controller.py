# -*- coding: utf-8 -*-

import web
import json
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
		# data = web.input(file = {})
		files = web.webapi.rawinput().get('file')

		if not isinstance(files, list):
			files = [files]

		metadatas = []
		for f in files:
			metadatas.append(Service().saveImage(f.filename, f.file.read()))

		return json.dumps(metadatas)

class Browse(object):
	def __init__(self):
		super(Browse, self).__init__()
		
	def GET(self):
		return render.browse()

class List(object):
	def __init__(self):
		super(List, self).__init__()

	def GET(self):
		return json.dumps(Service().list())

class Save(object):
	def __init__(self):
		super(Save, self).__init__()

	def POST(self):
		metadatas = web.data()
		Service().save(json.loads(json.loads(metadatas)['data']))
