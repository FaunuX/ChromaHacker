import json

with open('colorschemes.json', 'r') as f:
    colorscheme_json = f.read()

colorschemes = json.loads(colorscheme_json)

def process_colorscheme(colorscheme):
    return colorschemes[colorscheme]
