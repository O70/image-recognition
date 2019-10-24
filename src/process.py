# -*- coding: utf-8 -*-

import cv2
import numpy as np
import core.utils as utils
import tensorflow as tf
from PIL import Image

class Process(object):
	def __init__(self):
		super(Process, self).__init__()

	def run(self):
		# print(tf)
		print('process image....')
