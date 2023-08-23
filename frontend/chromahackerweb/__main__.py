import os
import webbrowser
import json
import io

from flask import Flask, request, send_file, render_template, Response
from werkzeug.wsgi import wrap_file

from chromahacker.palettize import palettize

import requests

data = requests.get('https://raw.githubusercontent.com/wez/wezterm/f535c5bdc092c82db1b939c82babf98a2436c456/docs/colorschemes/data.json').json()
colorschemes = {}

for colorscheme in data:
    name       = colorscheme['metadata']['name']
    background = colorscheme['colors']['background']
    foreground = colorscheme['colors']['foreground']
    midground  = colorscheme['colors']['ansi'][4]
    colorschemes[name] = [
        background,
        midground,
        foreground
    ]

app = Flask(__name__)

OUTPUT = "png"

@app.route('/palettize_custom', methods=['GET'])
def palettize_custom_endpoint():
    url = request.args.to_dict()['url']
    args = []
    i = 0
    while True:
        if 'arg' + str(i) in request.args.to_dict():
            args.append(request.args.get('arg' + str(i)))
            i += 1
        else:
            break
    accurate = not "accuracy" in request.args.to_dict()
    return palettize_function(url, *args, accurate=accurate)

@app.route('/palettize_premade', methods=['GET'])
def palettize_premade_endpoint():
    url = request.args.to_dict()['url']
    palette_string = request.args.to_dict()['palette']
    args = colorschemes[palette_string]
    accurate = not "accuracy" in request.args.to_dict()
    return palettize_function(url, *args, accurate=accurate)

def palettize_function(url, *args, accurate=False):
    b = io.BytesIO(palettize(url, OUTPUT, *args, accurate=accurate))
    return send_file(b, mimetype='image/' + OUTPUT)

@app.route('/colorschemes/<query>')
def colorschemes_search(query):
    if query in colorschemes:
        return colorschemes[query]
    else:
        return "Record not found", 400

@app.route('/')
def main():
    return render_template('index.html')

def run():
    webbrowser.open('http://localhost:5000')
    app.run()
