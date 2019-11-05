from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from sklearn.metrics import adjusted_rand_score
import json
import spacy
import os
# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from flask import Flask,jsonify,request,render_template
app = Flask(__name__)


@app.route('/')
def main_page():
    return render_template('index.html')



@app.route('/kmeans', methods=['POST'])
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

@app.route("/ads", methods=['POST'])
def purshase():

    posted_data = request.get_json()
    age = int(posted_data['age'])
    salary = int(posted_data['salary'])

    new_data = [[age,salary]]

    # Importing the dataset
    dataset = pd.read_csv('Social_Network_Ads.csv')
    X = dataset.iloc[:, [2, 3]].values
    y = dataset.iloc[:, 4].values

    # Splitting the dataset into the Training set and Test set
    from sklearn.model_selection import train_test_split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25, random_state = 0)

    # Feature Scaling
    from sklearn.preprocessing import StandardScaler
    sc = StandardScaler()
    X_train = sc.fit_transform(X_train)
    X_test = sc.transform(X_test)
    new_data_pred = sc.transform(new_data)

    # Fitting SVM to the Training set
    from sklearn.svm import SVC
    classifier = SVC(kernel = 'linear', random_state = 0)
    classifier.fit(X_train, y_train)

    # Predicting the Test set results
    y_pred = classifier.predict(new_data_pred)

    response = {
        "result" : str(y_pred)
    }

    return jsonify(response)




if __name__ == '__main__':
    app.run(host="0.0.0.0", port=os.environ.get('PORT'))



