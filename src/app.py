# -*- coding: utf-8 -*-

import web

urls = (
	'/', 'controller.Home',
	# '/', 'controller.Show',
	'/upload', 'controller.Upload'
)

if __name__ == '__main__':
	app = web.application(urls, globals())
	app.run()
