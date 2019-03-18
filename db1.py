import pickledb

db = pickledb.load('hello.db', False)

db.set('key', 'value')
db.get('key')
db.dump()

