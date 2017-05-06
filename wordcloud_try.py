#-*- coding: utf-8 -*-

from os import path
import os
import jieba
from wordcloud import WordCloud
import matplotlib.pyplot as plt

#获取文本内容
d = path.dirname(__file__)
text_content = open(path.join( d , 'text.txt')).read().decode('gbk')

#jieba分词处理
word_list=jieba.cut(text_content,cut_all=False)
word_split=" ".join(word_list)

#生成词云1，并展示
wordcloud_image = WordCloud().generate(word_split)
plt.imshow(wordcloud_image)
plt.axis("off")

#生成词云2，并展示
wordcloud_image = WordCloud(width=800,height=400,max_font_size=84,min_font_size=16).generate(word_split)
plt.figure()
plt.imshow(wordcloud_image)
plt.axis("off")
plt.show()