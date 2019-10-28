# -*- coding: utf-8 -*-

import os, datetime, uuid, shutil

from PIL import Image
from io import BytesIO
from web import database

from config import JDBCS, PREDICT_MIN, getSubDir
from process import Process

table_name = 'tbl_image_metadata'
dir_prefix = 'static'

def mkdirs(dirpath):
	if not os.path.exists(dirpath):
		os.makedirs(dirpath)

class Service(object):
	def __init__(self):
		super(Service, self).__init__()

	def list(self):
		db = database(dbn = JDBCS['dbn'], user = JDBCS['user'], pw = JDBCS['pw'], db = JDBCS['db'])
		rs = db.select(table_name, order = 'create_date desc, final_name')

		result = []
		for x in rs:
			x['create_date'] = x.create_date.strftime('%Y-%m-%d %H:%M:%S')
			result.append(x)

		return result

	def save(self, filename, bytes):
		newname = datetime.datetime.now().strftime('%Y%m%d%H%M%S%f_') + filename

		tmpDirpath = dir_prefix + '/tmp/'
		mkdirs(tmpDirpath)
		tmpFilepath = tmpDirpath + newname
		Image.open(BytesIO(bytes)).save(tmpFilepath)

		metadata = { 'id': None, 'filepath': tmpFilepath }

		predicts = Process().run(tmpFilepath)

		if len(predicts) > 0 and predicts[0]['predict'] >= PREDICT_MIN:
			maxPredict = predicts[0]
			dirpath = dir_prefix + '/repos/' + getSubDir(maxPredict['category'])
			mkdirs(dirpath)

			filepath = dirpath + newname
			shutil.move(tmpFilepath, filepath)

			metadata['id'] = str(uuid.uuid1())
			metadata['filename'] = newname
			metadata['filepath'] = filepath
			metadata['create_date'] = datetime.datetime.now()

			db = database(dbn = JDBCS['dbn'], user = JDBCS['user'], pw = JDBCS['pw'], db = JDBCS['db'])
			db.insert(table_name, **metadata)

		return {
			'id': metadata['id'],
			'filepath': metadata['filepath'],
			'predicts': predicts
		}

	def update(self, metadatas):
		pass

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

	def saveMetadata(self, metadatas):
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

		db = database(dbn = JDBCS['dbn'], user = JDBCS['user'], pw = JDBCS['pw'], db = JDBCS['db'])
		res = db.multiple_insert(table_name, values = metadatas)
