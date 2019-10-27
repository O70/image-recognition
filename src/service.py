# -*- coding: utf-8 -*-

import os, datetime, uuid, shutil

from PIL import Image
from io import BytesIO
from web import database

from process import Process

class Service(object):
	def __init__(self):
		super(Service, self).__init__()

	def saveImage(self, filename, bytes):
		dirpath = 'static/tmp/'
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

	def list(self):
		db = database(dbn = 'mysql', user = 'root', pw = 'mysql', db = 'riped-config')
		rs = db.select('tbl_image_metadata', order = 'create_date desc, final_name')

		result = []
		for x in rs:
			x['create_date'] = x.create_date.strftime('%Y-%m-%d %H:%M:%S')
			result.append(x)

		return result

	def save(self, metadatas):
		dirpath = 'static/repos/'
		if not os.path.exists(dirpath):
			os.mkdir(dirpath)

		curDate = datetime.datetime.now()

		for md in metadatas:
			md['id'] = str(uuid.uuid1())
			md['create_date'] = curDate

			npath = dirpath + md['final_name']
			if os.path.exists(md['filepath']):
				shutil.move(md['filepath'], npath)

			ori_img = md['filepath'].replace('final_', '')
			if os.path.exists(ori_img):
				shutil.move(ori_img, ori_img.replace('/tmp/', '/repos/'))

			md['filepath'] = npath

		db = database(dbn = 'mysql', user = 'root', pw = 'mysql', db = 'riped-config')
		res = db.multiple_insert('tbl_image_metadata', values = metadatas)
