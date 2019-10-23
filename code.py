# -*- coding: utf-8 -*-

import web

urls = (
	'/', 'Home'
)

render = web.template.render('templates/')

class Home(object):
	def __init__(self):
		super(Home, self).__init__()

	def GET(self):
		return render.index('THRAEX')

if __name__ == '__main__':
	app = web.application(urls, globals())
	app.run()
