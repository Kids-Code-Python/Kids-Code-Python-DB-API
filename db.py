def user_db(db):
	new_db = {}
	for k in db.keys():
		if k[1] == 'user':
			new_db[k[0]] = db[k]
	return new_db
