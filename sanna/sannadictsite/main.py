from flask import Flask
from flask_bootstrap import Bootstrap
from flask import render_template, request
from flask_pymongo import PyMongo


app = Flask(__name__)
Bootstrap(app)

app.config['MONGO_DBNAME'] = 'sanna'
app.config['MONGO_URI'] = 'mongodb://sanna:sanna@ds131109.mlab.com:31109/sanna'

mongo = PyMongo(app)

@app.route('/')
def home():

    return render_template("/index.html")

@app.route('/word/<query>', methods=['GET', 'POST'])
def word():
	if request.method == 'GET':
		#db = mongo.db.nouns
  		#entry = {"_id": query}
  		#result = db.find_one(entry)

  		#print(findEntry)
		return render_template('word.html')
	else:
		return render_template('word.html')


"""MUST be at end of program"""
if __name__ == '__main__':
    app.run(debug=True)