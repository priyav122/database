import meradb
db = meradb.load('ekta.db')
db.set('key1', 'value1')
db.get('key1')
db.set('key2', 'value2')
db.get('key2')
db.load_file()

