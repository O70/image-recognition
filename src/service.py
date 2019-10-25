# -*- coding: utf-8 -*-

import os
import datetime
from PIL import Image
from io import BytesIO

from process import Process

class Service(object):
	def __init__(self):
		super(Service, self).__init__()

	def save(self, filename, bytes):
		filedir = './repos/'
		if not os.path.exists(filedir):
			os.mkdir(filedir)

		prefix = filedir + datetime.datetime.now().strftime('%Y%m%d%H%M%S%f_')
		image_path = prefix + filename
		target_path = prefix + 'new_' + filename

		image = Image.open(BytesIO(bytes))
		image.save(image_path)

		Process().run(image_path, target_path)

