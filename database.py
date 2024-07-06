import sqlite3

class database:
	def __init__(self,path):
		self.connection = sqlite3.connect(path)
	
	def do(self,text):
		self.connection.cursor().execute(text)
		
	def query():
		self.connection.cursor()

def connect():
	return sqlite3.connect(path)