# -*- coding: utf-8 -*-

import random

class Process(object):
	"""Use models to process images"""
	def __init__(self):
		super(Process, self).__init__()

	def run(self, imgpath):
		print('Start processing images: ' + imgpath)

		preds = []
		while len(preds) < 3:
			pred = round(random.random(), 6)
			preds.append({
				'predict': pred,
				'category': random.randint(0, 35)
			})

		return sorted(preds, key = lambda x:x['predict'], reverse = True)
