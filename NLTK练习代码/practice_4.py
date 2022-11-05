# 条件频率分布

#给定某个词汇或其他项目的链表变量 mylist，
# FreqDist(mylist)会计算链表中每个项目出现的次数

# 条件和事件
# 条件频率分布需要给每个事件关联一个条件，
# 所以不是处理一个词序列
# 我们必须处理的是一个配对序列
# 每对的形式是:(条件，事件)。
# 如果我们按文体处理整个布朗语料库，将有 15 个条件
# (每个文体一个条件)和 1,161,192 个事件(每一个词一个事件)。

# 按文体计数词汇
import nltk
from nltk.corpus import brown

cfd = nltk.ConditionalFreqDist(
    (genre, word)
    for genre in brown.categories()
    for word in brown.words(categories=genre)
)


'''
只看两个文体:新闻和言情。对于每个文体，我们遍历文体中的每
个词以产生文体与词的配对
'''
genre_word = [(genre, word)
              for genre in ['news','romance']
              for word in brown.words(categories=genre) #这里的参数决定了上一行列表的文字与word种类严格对应
              ]
print(len(genre_word))
print(len(cfd))
'''
170576
15
'''
print(genre_word[:4])
print(genre_word[-4:]) #倒数4个
'''
[('news', 'The'), ('news', 'Fulton'), ('news', 'County'), ('news', 'Grand')]
[('romance', 'afraid'), ('romance', 'not'), ('romance', "''"), ('romance', '.')]
'''
cfd = nltk.ConditionalFreqDist(genre_word)
print(cfd)
# <ConditionalFreqDist with 2 conditions>
print(cfd.conditions())
# ['news', 'romance']
print(cfd['news'])
# <FreqDist with 14394 samples and 100554 outcomes>
print(list(cfd['romance']))
# [',', '.', 'the', 'and', 'to', 'a', 'of', '``', "''", 'was', 'I', 'in', 'he', 'had', '?',。。。。。。。。。]
print(cfd['romance']['could'])
# 193


# 词汇列表语料库

def unusual_words(text):
    text_vocab = set(w.lower() for w in text if w.isalpha())
    english_vocal = set(w.lower()for w in nltk.corpus.words.words())
    unusual = text_vocab.difference(english_vocal)
    return sorted(unusual)


unusual_words_test = unusual_words(nltk.corpus.gutenberg.words('austen-sense.txt'))
print(len(unusual_words_test))  # 1601




