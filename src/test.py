# from web import database

# db = database(dbn='mysql', user='root', pw='mysql', db='riped-config')
# # db.insert('tbl_image_metadata', id='001', filepath='repos/xx1.jpg')
# # db.insert('tbl_image_metadata', id='002', filepath='repos/xx2.jpg')
# # datas = db.select('tbl_image_metadata')
# # for d in datas:
# # 	print(d.id)
# # 	print(d.filepath)

# print(db.multiple_insert)

# import random
 
# for x in range(10):
# 	print(random.randint(0, 4))

import uuid

print(uuid.uuid1())
# print(uuid.uuid3())
print(uuid.uuid4())
print(uuid.uuid5(uuid.NAMESPACE_DNS,'textname'))
