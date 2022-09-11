import pandas as pd
import numpy as np
from PIL import Image
from wordcloud import WordCloud
from wordcloud import ImageColorGenerator
from matplotlib import pyplot as plt

data=pd.read_excel('./GDP.xlsx',sheet_name='2021',usecols=['国家/地区','GDP总量(人民币核算)'])
list_country=data['国家/地区'].tolist()
list_gdp=data['GDP总量(人民币核算)'].tolist()
dic=dict(zip(list_country,list_gdp))

font=r'C:\Windows\Fonts\simhei.ttf'
MASK=np.array(Image.open('./背景图层.png'))
img_col=ImageColorGenerator(MASK)
wordcloud=WordCloud(background_color='white',scale=1,max_words=300,max_font_size=300,min_font_size=10,font_path=font,mask=MASK,mode='RGB').generate_from_frequencies(dic)
plt.imshow(wordcloud.recolor(color_func=img_col),alpha=1)
plt.axis('off')
plt.show()
