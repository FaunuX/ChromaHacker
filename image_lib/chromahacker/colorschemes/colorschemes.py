import requests
import json

def run():
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

    colorschemes_json = json.dumps(colorschemes)

    with open('colorschemes.json', 'w') as f:
        f.write(colorschemes_json)
