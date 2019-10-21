from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from sklearn.metrics import adjusted_rand_score
import json
import os
from flask import Flask,jsonify,request,render_template
app = Flask(__name__)


@app.route('/')
def main_page():
    return render_template('index.html')



@app.route('/predict', methods=['POST'])
def kmeans_pred():

    posted_data = request.get_json()
    true_k = posted_data['num_cluster']
    documents = posted_data['data']
    feeds = dict()
    vectorizer = TfidfVectorizer(stop_words='english')
    X = vectorizer.fit_transform(documents.split('.'))

    
    model = KMeans(n_clusters=true_k, init='k-means++', max_iter=100, n_init=1)
    model.fit(X)

    order_centroids = model.cluster_centers_.argsort()[:, ::-1]
    terms = vectorizer.get_feature_names()
    print(terms)
    for i in range(true_k):
        feeds.update({"cluster_"+str(i)+"": [terms[ind] for ind in order_centroids[i, :10]]})

    return jsonify(feeds)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=3000)#port=os.environ.get('PORT'))