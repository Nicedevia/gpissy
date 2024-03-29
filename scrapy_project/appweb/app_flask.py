from flask import Flask, render_template
from pymongo import MongoClient
from bson import json_util

app = Flask(__name__)

client = MongoClient('mongodb://localhost:27017/')
db = client['mon_mongo']
collection = db['scraped_data']



@app.route('/', methods=['GET'])
def get_data():
    random_quote = db.quotes_scrap.aggregate([{ '$sample': { 'size': 1 } }]).next()
    result = {
        'text': random_quote['text'],
        'author': random_quote['author'],
    }
    
    data = json_util.dumps(result)

    
    return render_template('index.html', quote=random_quote)


if __name__ == '__main__':
    app.run(debug=True)


