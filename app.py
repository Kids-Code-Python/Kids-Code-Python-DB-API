from flask import Flask, jsonify
from replit import db
from db import user_db
import os
import package

app = Flask(__name__)
correct_key = os.getenv('KEY')

@app.route('/<key>/users/view')
def view_users(key):
	if correct_key != key:
		return jsonify({'auth-error':'user not authenticized'})
	return user_db(db)
	


@app.route('/<key>/users/add?name=<name>&occupation<occupation>')
def add_user(key, name, occupation):
	if correct_key != key:
		return jsonify({'auth-error': 'user not authenticized'})

app.run('0.0.0.0')
