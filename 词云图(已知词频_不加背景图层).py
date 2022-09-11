import pandas as pd
from wordcloud import WordCloud
from matplotlib import pyplot as plt

data=pd.read_excel('./GDP.xlsx',sheet_name='2021',usecols=['国家/地区','GDP总量(人民币核算)'])
list_country=data['国家/地区'].tolist()
list_gdp=data['GDP总量(人民币核算)'].tolist()
dic=dict(zip(list_country,list_gdp))

font=r'C:\Windows\Fonts\simhei.ttf'
wordcloud=WordCloud(background_color='black',width=800,height=800,margin=1,font_path=font).generate_from_frequencies(dic)
plt.imshow(wordcloud)
plt.axis('off')
plt.show()
