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

class Save(object):
	def __init__(self):
		super(Save, self).__init__()

	def POST(self):
		# metadatas = web.webapi.rawinput().get('metadata')
		metadatas = web.data()
		# print(json.loads(metadatas))
		print(json.loads(metadatas)['data'])
		print(type(json.loads(metadatas)['data']))
		print('**************')
		dd = json.loads(json.loads(metadatas)['data'])
		print(type(dd))
		for x in dd:
			print(x)
		# print(json.loads(json.loads(metadatas)['data']))
		# for md in json.loads(metadatas)['data']:
		# 	print((md))
