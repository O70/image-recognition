# -*- coding: utf-8 -*-

import os
import datetime
from PIL import Image
from io import BytesIO
from web import database

from process import Process

class Service(object):
	def __init__(self):
		super(Service, self).__init__()

	def saveImage(self, filename, bytes):
		dirpath = 'static/repos/'
		if not os.path.exists(dirpath):
			os.mkdir(dirpath)

		prefix = datetime.datetime.now().strftime('%Y%m%d%H%M%S%f_')
		saved_name = prefix + filename
		final_name = prefix + 'final_' + filename

		image_path = dirpath + saved_name
		target_path = dirpath + final_name

		image = Image.open(BytesIO(bytes))
		image.save(image_path)

		# metadata = Process().run(image_path, target_path)
		metadata = {}
		metadata['original_name'] = filename
		metadata['final_name'] = final_name
		metadata['filepath'] = target_path

		metadata['probability'] = round(np.random.rand(), 2)
		metadata['category'] = round(np.random.rand(), 2)

		return metadata

	def saveMetadata(self):
		db = database(dbn='mysql', user='root', pw='mysql', db='riped-config')
		datas = db.select('tbl_image_metadata')
		print(datas)
		return datas
