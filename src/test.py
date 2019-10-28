# from web import database

# db = database(dbn='mysql', user='root', pw='mysql', db='riped-config')
# # db.insert('tbl_image_metadata', id='001', filepath='repos/xx1.jpg')
# # db.insert('tbl_image_metadata', id='002', filepath='repos/xx2.jpg')
# datas = db.select('tbl_image_metadata', order = 'create_date desc, final_name')
# print(type(datas))
# for d in datas:
# 	print((d.create_date))
# 	print(d.filepath + ', ' + d.create_date.strftime( '%Y-%m-%d %H:%M:%S.%f' ))

# print(db.multiple_insert)

# import random
 
# l = [0.1, 0.9, 0.7, 0.4, 0.2, 0.8]
# print(l)
# l.sort()
# print(l)
# for x in range(10):
# 	# print(random.seed(12345))
# 	# print(round(random.random(), 6))
# 	print(random.randint(0, 4))

# import uuid

# print(uuid.uuid1())
# # print(uuid.uuid3())
# print(uuid.uuid4())
# print(uuid.uuid5(uuid.NAMESPACE_DNS,'textname'))

# import shutil

# print(shutil)
# shutil.copy('../static/img/sample.jpeg', '../static/img/sample1.jpeg')


# a = 'static/tmp/x_final.jpeg'
# print(a.replace('x_final.jpeg', 'x.jpeg'))
# print((a.replace('_final', '')))
# print((a.replace('/tmp/', '/repos/')))

# import os

# dirpath = '../static/repo'
# print(os.path.exists(dirpath))
# if not os.path.exists(dirpath):
# 	# os.mkdir(dirpath)
# 	os.makedirs(dirpath)

# dicts = [
# 	{ "name": "Tom", "age": 10 },
# 	{ "name": "Mark", "age": 5 },
# 	{ "name": "Pam", "age": 7 },
# 	{ "name": "Dick", "age": 12 }
# ]

# print(next(item for item in dicts if item["name"] == "Pam"))


# people = [
# 	{'name': "Tom", 'age': 10},
# 	{'name': "Mark", 'age': 5},
# 	{'name': "Pam", 'age': 7}
# ]

# d = {'name': "Tom", 'age': 10}
# print(d.keys())
# for x in d:
# 	print(x + ': ' + str(d[x]))

# python 2
# print(filter(lambda person: person['name'] == 'Pam', people))

# # python 3
# print(list(filter(lambda person: person['name'] == 'Pam', people)))
# print(list(map(lambda p: p['name'], people)))


# from functools import reduce
# foo = [2, 18, 9, 22, 17, 24, 8, 12, 27]
# print (reduce(lambda x, y: x + y, foo))

# f = lambda x: [[y for j, y in enumerate(set(x)) if (i >> j) & 1] for i in range(2**len(set(x)))]
# print(list(f))

# from PIL import Image

# img = Image.open('/Users/Guiwang/Downloads/logo.png')
# print(type)

import base64

with open('/Users/Guiwang/Downloads/logo.png', 'rb') as f:
	print(base64.b64encode(f.read()))
