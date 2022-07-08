from wordcloud import WordCloud
import matplotlib.pyplot as plt
from collections import Counter
from konlpy.tag import Okt
from PIL import Image
import numpy as np
import os
import pathlib

data_dir = './data'

font_path = "./fonts/huin.otf"# "C:/Windows/Fonts/malgun.ttf"

words = []

for (root, dirs, files) in os.walk(data_dir):
    for f in files:
        ext = pathlib.Path(f).suffix
        if ext != '.txt':
            continue
        file_path = os.path.join(root, f)
        with open(file_path, 'r') as f:
            text = f.read()
            okt = Okt()
            nouns = okt.nouns(text)
            words.extend(nouns)


c = Counter(words)

wc = WordCloud(
    font_path=font_path,
    width=400, 
    height=400, 
    scale=2.0,
    max_font_size=80,
    background_color='white'
)

gen = wc.generate_from_frequencies(c)

plt.figure()
plt.imshow(gen)
plt.axis('off')
plt.show()