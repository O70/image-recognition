# -*- coding: utf-8 -*-

import web, json
from service import Service

render = web.template.render('templates/')

content_type = 'application/json'

class Home(object):
	def __init__(self):
		super(Home, self).__init__()

	def GET(self):
		return render.index()

class Browse(object):
	def __init__(self):
		super(Browse, self).__init__()
		
	def GET(self):
		return render.browse()

class Upload(object):
	def __init__(self):
		super(Upload, self).__init__()
		
	def POST(self):
		web.header('Content-Type', content_type)
		data = web.input(file = {})
		file = data['file']

		return json.dumps(Service().save(file.filename, file.file.read()))

class List(object):
	def __init__(self):
		super(List, self).__init__()

	def GET(self):
		web.header('Content-Type', content_type)

		return json.dumps(Service().list())

class Update(object):
	def __init__(self):
		super(Update, self).__init__()

	def POST(self):
		Service().update(json.loads(web.data()))

		web.header('Content-Type', content_type)

		return json.dumps({ 'data': True })
