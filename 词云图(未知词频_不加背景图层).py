import re
import jieba
import pandas as pd
from wordcloud import WordCloud
from matplotlib import pyplot as plt

text=pd.read_csv('斗破苍穹.txt',index_col=0,encoding='utf-8',error_bad_lines=False)
text2=str(text)
# 去除特殊字符、数字和字母，只保留汉字
text3=re.sub("[a-zA-Z0-9'!""#$%&\'()*+,-./:;<=>?@，。?★、…【】《》：？“”‘'！[\\]^_`{|}~\s]+","",text2)
text4=jieba.lcut(text3)
text5=' '.join(text4)

# 停用词
stop_words=set()
content=[line.strip() for line in open('stopwords.txt', 'r', encoding='utf-8').readlines()]
stop_words.update(content)

font=r'C:\Windows\Fonts\simhei.ttf'
wordcloud=WordCloud(background_color='white',scale=1,max_words=500,max_font_size=80,min_font_size=1,font_path=font,stopwords=stop_words).generate_from_text(text5)
plt.imshow(wordcloud,interpolation='bilinear')
plt.axis('off')
plt.show()
