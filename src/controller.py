# -*- coding: utf-8 -*-

import web
from process import Process

render = web.template.render('templates/')

class Home(object):
	def __init__(self):
		super(Home, self).__init__()

	def GET(self):
		return render.index()

class Upload(object):
	def __init__(self):
		super(Upload, self).__init__()
		
	def GET(self):
		print('mock...')
		raise web.seeother('/')

	def POST(self):
		i = web.input()
		print(i['name'])
		return web.seeother('/')


class Show(object):
	def __init__(self):
		super(Show, self).__init__()
	
	def GET(self):
		Process().run()
		return render.index()
