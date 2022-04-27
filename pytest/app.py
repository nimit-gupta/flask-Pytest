#!/usr/local/bin/python3
#-*-coding:utf-8-*-

from flask import Flask, redirect, url_for, render_template, session, abort, request, jsonify

app = Flask(__name__, template_folder = "templates")

@app.route('/')
def func_1():
    return render_template("index.html")

@app.route('/next')
def next():
    return render_template('next.html')

@app.route('/data', methods = ["POST"])
def data():
    if request.method == "POST":
        #fname = request.json["fname"]
        #lname = request.json["lname"]
        fname = request.json.get("fname")
        lname = request.json.get("lname")
        return jsonify({"first name": fname, "last name": lname})
    else:
        return jsonify({"error" : "wrong http method"})


if __name__ == '__main__':
    app.run(debug = False)