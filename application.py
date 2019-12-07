from flask import Flask, render_template, jsonify, request
from elasticsearch import Elasticsearch

es = Elasticsearch()

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('home.html')



@app.route('/elasticsearch', methods=['GET'])
def elasticsearch():
    results = es.get(index='ecommerce', id='1')
    return jsonify(results['_source'])

@app.route('/search/', methods=['GET'])
def search():
    body = {
        "query":{
            "match_all": {}
        }
    }

    result = es.search(index='ecommerce', body=body)
    return jsonify(result['hits']['hits'])

if __name__ == "__main__":
    app.run(debug=True)