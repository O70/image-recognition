# -*- coding: utf-8 -*-

import os
import datetime
from PIL import Image
from io import BytesIO

from process import Process

class Service(object):
	def __init__(self):
		super(Service, self).__init__()

	def saveImage(self, filename, bytes):
		dirpath = 'repos/'
		if not os.path.exists(dirpath):
			os.mkdir(dirpath)

		prefix = datetime.datetime.now().strftime('%Y%m%d%H%M%S%f_')
		saved_name = prefix + filename
		final_name = prefix + 'final_' + filename

		image_path = dirpath + saved_name
		target_path = dirpath + final_name

		image = Image.open(BytesIO(bytes))
		image.save(image_path)

		metadata = Process().run(image_path, target_path)
		metadata['original_name'] = filename
		metadata['final_name'] = final_name
		metadata['filepath'] = target_path

		return metadata

	def saveMetadata(self):
		pass
