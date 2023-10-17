from PIL import Image
import os
import webbrowser
import json
import io
import pickle
import base64

import requests

from flask import Flask, request, send_file, render_template, Response
from werkzeug.wsgi import wrap_file

import tensorflow as tf
import keras
import numpy as np

from chromahacker.palettize import palettize

# @keras.saving.register_keras_serializable('Sorting')
class Sorting(keras.layers.Layer):
    def __init__(self, kernel_size):
        super().__init__()
        self.kernel_size = kernel_size
        self.w = self.add_weight(
                shape=kernel_size,
                initializer="ones",
                trainable=False
                )

    def call(self, inputs):
        sorted = tf.argsort(tf.reduce_sum(inputs * self.w, 2))
        rv = tf.gather(inputs, sorted, batch_dims=1)
        return rv

model = keras.models.load_model('model.h5', custom_objects={'Sorting': Sorting})

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
    return palettize_function(url, *args)

@app.route('/palettize_premade', methods=['GET'])
def palettize_premade_endpoint():
    url = request.args.to_dict()['url']
    palette_string = request.args.to_dict()['palette']
    args = colorschemes[palette_string]
    return palettize_function(url, *args)

@app.route('/palettize_from_image', methods=['GET'])
def palettize_from_image_endpoint():
    url = request.args.to_dict()['url']
    url_colors = request.args.to_dict()['url_colors']
    color_image_array = Image.open(requests.get(url_colors, stream=True).raw).to_array()
    args = model.predict(color_image_array)
    return palettize_function(url, *args)

def palettize_function(url, *args):
    print(args)
    palettized_array = np.rint(palettize(url, *args)).astype(np.uint8)
    buffer = io.BytesIO()
    Image.fromarray(palettized_array).save(buffer, OUTPUT)
    buffer.seek(0)
    data = buffer.read()
    data = base64.b64encode(data).decode()
    return f'<img src="data:image/png;base64,{data}">'

    # with open("ok.png", "wb") as f:
        # print(b.read())
        # f.write(b.read())
    # return send_file(b, mimetype='image/' + OUTPUT)

@app.route('/colorschemes/<query>')
def colorschemes_search(query):
    if query in colorschemes:
        return colorschemes[query]
    else:
        return "Record not found", 400

# @app.route('/')
# def main():
    # return render_template('index.html')

def run():
    app.run()
