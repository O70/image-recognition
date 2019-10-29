# -*- coding: utf-8 -*-

import web

urls = (
	'/', 'controller.Home',
	'/browse', 'controller.Browse',
	'/list', 'controller.List',
	'/upload', 'controller.Upload',
	'/update', 'controller.Update'
)

if __name__ == '__main__':
	app = web.application(urls, globals())
	app.run()
