from web import database

db = database(dbn='mysql', user='root', pw='mysql', db='riped-config')
# db.insert('tbl_image_metadata', id='001', filepath='repos/xx1.jpg')
# db.insert('tbl_image_metadata', id='002', filepath='repos/xx2.jpg')
datas = db.select('tbl_image_metadata')
for d in datas:
	print(d.id)
	print(d.filepath)
