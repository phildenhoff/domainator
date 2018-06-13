#!/usr/bin/python3

from flask import Flask, render_template, request
from jinja2 import Template

app = Flask(__name__)

def searchFileForPartsOfWord(file, word):
    with open(file) as file:
        fileContents = file.readlines()
    
    results = []
    for line in fileContents:
        line = line.strip().lower()
        # if word.endswith(line):
        index = word.find(line)
        if index != -1 and index != 0:
            path = ""
            if not word.endswith(line):
                path = "/{}".format(word.split(line)[1])

            results.append(({
                "line": line,
                "preLine": word.split(line)[0],
                "path": path
            }))

    return results

@app.route("/")
def hello():
    return render_template('./index.html', my_string="Wheeeee!", my_list=[0,1,2,3,4,5])

@app.route("/search")
def searchWord():
    word = request.args.get('domain')
    if not word:
        return "Looks like you didn't add a word to the url. Try again, like this: 127.0.0.1/search/apple"
    else:
        tldsInWord = searchFileForPartsOfWord("./tlds.txt", word)
        return render_template('./result.html', tlds=tldsInWord)