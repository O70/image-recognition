# -*- coding: utf-8 -*-

import web

urls = (
	'/', 'controller.Home',
	'/upload', 'controller.Upload',
	'/list', 'controller.List',
	'/save', 'controller.Save',
	'/browse', 'controller.Browse'
)

if __name__ == '__main__':
	app = web.application(urls, globals())
	app.run()
