# -*- coding: utf-8 -*-

import os, datetime, uuid, shutil

from PIL import Image
from io import BytesIO
from web import database

from config import JDBCS, PREDICT_MIN, getSubDir, getLabel
from process import Process

table_name = 'tbl_image_metadata'
dir_prefix = 'static'

def mkdirs(dirpath):
	if not os.path.exists(dirpath):
		os.makedirs(dirpath)

def getDB():
	return database(dbn = JDBCS['dbn'], user = JDBCS['user'], pw = JDBCS['pw'], db = JDBCS['db'])

class Service(object):
	def __init__(self):
		super(Service, self).__init__()

	def list(self):
		rs = getDB().select(table_name, order = 'category, create_date desc')

		result = []
		for x in rs:
			label = getLabel(x['category'])
			result.append({
				'id': x['id'],	
				'filepath': x['filepath'],	
				'predict': x['predict'],	
				'category': label['label'],	
				'describe': label['describe']
			})

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
			metadata['predict'] = maxPredict['predict']
			metadata['category'] = maxPredict['category']
			metadata['create_date'] = datetime.datetime.now()

			getDB().insert(table_name, **metadata)

		return {
			'id': metadata['id'],
			'filepath': metadata['filepath'],
			'predicts': predicts
		}

	def update(self, metadata):
		getDB().update(table_name, 
			where = "id = '" + metadata['id'] + "'", 
			category = str(metadata['category']))
