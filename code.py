# -*- coding: utf-8 -*-

import web

urls = (
	'/', 'Home'
)

class Home(object):
	def __init__(self):
		super(Home, self).__init__()

	def GET(self):
		return 'This is the home page!'

if __name__ == '__main__':
	app = web.application(urls, globals())
	app.run()
