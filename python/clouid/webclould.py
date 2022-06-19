from tkinter import Y
from flask import *
import pymongo
import os,sys
from wsgiref.simple_server import make_server
client = pymongo.MongoClient(host= '127.0.0.1', port=27017)
db = client.testdb
coll = db.get_collection("cloulddb")
namelist = [i['name'] for i in coll.find()]
app = Flask(__name__)

@app.route('/')

def upload():

	return render_template("upload.htm")

@app.route('/upload', methods = ['POST','GET'])

def success():
	global namelist
	if request.method == 'POST':
		

		f = request.files['file']
		
		if f.filename !=None:
		
			f.save("D:\\db\\"+f.filename)
			longo={"name":f.filename}
        	
			x=coll.insert_one(longo)
			namelist.append(f.filename)
			return render_template("upload.htm")
		else:
			abort(404)
	return render_template("index.htm")
@app.route('/download', methods = ['POST','GET'])
def succes():

	if request.method == 'POST':
		y= request.values.get("word")
		if y!=None and y in namelist:
			
			if os.path.isdir(y):
				return '<h1>文件夹无法下载</h1>'
			result = coll.delete_many({'name' :y})

			return send_file('D:\db\\'+y)


		else:
			abort(404)

	return render_template("downloald.htm", name = namelist)

		
		
BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, BASE_PATH)
if __name__ == '__main__':
	
	

	app.run(host='0.0.0.0',debug=True,port=5000)