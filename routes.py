from flask import request, render_template, redirect, jsonify
import pronouncing
from extensions import (
    FB_VERIFY_TOKEN,
    LOGGER
)
from app import app

@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template("index.html")
    elif request.method == 'POST':
        response = ["This is the rhymes of the word " + str(request.form['data'])]
        print(request.form['data'])
        words = pronouncing.rhymes(request.form['data'])
        words = words[:7]
        for w in words:
            response.append(str(w))
        return jsonify({"response" : response})
