#-*- coding: utf-8 -*-

from os import path
import os
import numpy as np
import jieba
from PIL import Image
from wordcloud import WordCloud , ImageColorGenerator
import matplotlib.pyplot as plt

#获取文本内容
d = path.dirname(__file__)
text_content = open(path.join( d , 'text.txt')).read().decode('gbk')
alice_mask=np.array(Image.open(path.join(d,"bear.jpg")))

#jieba分词处理
word_list=jieba.cut(text_content,cut_all=False)
word_split=" ".join(word_list)



#生成词云，并展示
wordcloud_image = WordCloud(background_color='white',mask=alice_mask ,max_words=5000,\
                            width=80,height=40,max_font_size=30,min_font_size=5\
                            ).generate(word_split)
image_colors = ImageColorGenerator(alice_mask)

'''
plt.imshow(wordcloud_image)
plt.axis("off")
'''
plt.figure('1')
plt.imshow(wordcloud_image.recolor(color_func=image_colors))
plt.axis("off")

plt.figure('2')
plt.imshow(alice_mask)
plt.axis("off")

plt.show()

wordcloud_image.to_file(path.join(d,"alice.png"))