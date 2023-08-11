from chromahacker.palettize import palettize

def run():
    with open('image.png', 'wb') as f:
        # f.write(palettize('https://wallpaperboat.com/wp-content/uploads/2020/06/12/44975/epic-08.jpg', 'png', 'black', 'midnightblue', 'darkslateblue', 'indianred', 'coral', 'darksalmon', 'white', accurate=True))
        f.write(palettize('https://wallpaperboat.com/wp-content/uploads/2020/06/12/44975/epic-08.jpg', 'png', '#1a1b26', '#db4b4b', '#ff9e64', '#c0caf5', accurate=True))

run()
