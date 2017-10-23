from collections import Counter
import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import numpy as np
import sys

file_words = sys.argv[1]
ex_file = sys.argv[2]

#this assumes the data is in a similar format to the example - continuous text
file = open(file_words, "r", encoding="utf-8-sig")
exclude_file = open(ex_file, "r", encoding="utf-8-sig").read().split()

# Example data 
# file = open(r"C:\\fed_words.txt", "r", encoding="utf-8-sig")
# exclude_file = open(r"C:\\exclude.txt", "r", encoding="utf-8-sig").read().split()

exclude_words = [i for i in exclude_file]

#make all the words lower case so casing doesn't seperate the same word
wordcount = Counter(file.read().split())
wordcount = dict((k.lower(), v) for k,v in wordcount.items())

df = pd.DataFrame.from_dict(wordcount, orient='index').reset_index()
df = df.rename(columns={'index':'word', 0:'count'})

#remove the words we don't want to see
df = df[~df.word.isin(exclude_words)]

#find percent of each word
df['percent'] = df['count']/(df['count'].sum())*100
df = df.sort_values(by = 'percent', ascending = False)
print('\n' + df.to_string(index=False))

#make wordcloud
wordcloud = WordCloud(width = 1000, height = 500).generate(' '.join(df['word']))
plt.figure(figsize=(12,6))
plt.imshow(wordcloud)
plt.axis("off")
plt.show()

#make frequency chart of top 25 words
top_words = df['word'][:25]
y_pos = np.arange(len(top_words))
performance = df['count'][:25]
plt.bar(y_pos, performance, align='center', alpha=0.5)
plt.xticks(y_pos, top_words)
plt.xlabel('Word', fontsize = 8)
plt.xticks(fontsize = 8,rotation = 90)
plt.ylabel('Frequency (count)')
plt.title('Top 25 Words and Frequency')
plt.show()
