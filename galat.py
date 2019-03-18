import meradb
db1 = meradb.load('some_other.db', True)
db2 = meradb.load('table.db', True)
db1.set('key', 'value1')
db2.set('key', 'value2')
db2.get('key')
db1.get('key')
db1.dump()
db2.dump()