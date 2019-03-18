import meradb
db = meradb.load("table.db")
db.set("key", "value")
db.get('key')
db.get_all()
db.rem()
db.exists()
db.total_keys()
db.del_db()
db.random_insert(5)

