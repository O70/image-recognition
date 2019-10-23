# -*- coding: utf-8 -*-

import web

urls = (
	'/', 'Hello'
)

app = web.application(urls, globals())

class Hello(object):
	def __init__(self):
		super(Hello, self).__init__()

	def GET(self):
		return 'Hello, THRAEX!'

if __name__ == '__main__':
	app.run()
