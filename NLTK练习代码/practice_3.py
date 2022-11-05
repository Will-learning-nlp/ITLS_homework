# 3. 语料库介绍与简单练习应用

import nltk
gutenber_op = nltk.corpus.gutenberg.fileids()
print(gutenber_op)

emma = nltk.corpus.gutenberg.words("austen-emma.txt")
print(len(emma))
'''
['austen-emma.txt', 'austen-persuasion.txt', 
'austen-sense.txt', 'bible-kjv.txt', 'blake-poems.txt', 
'bryant-stories.txt', 'burgess-busterbrown.txt', 
'carroll-alice.txt', 'chesterton-ball.txt', 
'chesterton-brown.txt', 'chesterton-thursday.txt',
 'edgeworth-parents.txt', 'melville-moby_dick.txt', 
 'milton-paradise.txt', 'shakespeare-caesar.txt', 
 'shakespeare-hamlet.txt', 'shakespeare-macbeth.txt', 'whitman-leaves.txt']
192427
'''

from nltk.corpus import gutenberg

gutenberg_ids= gutenberg.fileids()
print(gutenberg_ids)

emma = gutenberg.words('austen-emma.txt')

for fileid in gutenberg_ids:
    num_chars = len(gutenberg.raw(fileid))
    num_words = len(gutenberg.words(fileid))
    num_sents = len(gutenberg.sents(fileid))
    num_vocab = len(set([w.lower() for w in gutenberg.words(fileid)]))
    print(int(num_chars/num_words), int(num_words/num_sents), int(num_words/num_vocab), fileid)

# 平均词长，平均句子长度，每个词出现的平均次数

# raw() 函数给我们没有进行过任何语言学处理的文件的内容。
# sents()函数把 文本划分成句子，其中每一个句子是一个词列表。
macbeth_sentences = gutenberg.sents('shakespeare-macbeth.txt')
print(macbeth_sentences[0])
print(macbeth_sentences[100])
print(macbeth_sentences[1037])
longest_len = max([len(s) for s in macbeth_sentences])
print(longest_len)
print([i for i in range(3)])

print([s for s in macbeth_sentences if len(s) == longest_len])


#NLTK的网络文本小集合的内容包括 Firefox交流论坛，
# 在纽约无意听到的对话， 《加勒比海盗》的电影剧本，
# 个人广告和葡萄酒的评论

from nltk.corpus import webtext

for fileid in webtext.fileids():
    print(fileid,webtext.raw(fileid)[:100])

# 布朗语料库是第一个百万词级的英语电子语料库的，由布朗大学于 1961 年创建。
# 这个 语料库包含 500 个不同来源的文本，按照文体分类，如:新闻、社论等

from nltk.corpus import brown
print(brown.categories())
#布朗语料库是一个研究文体之间的系统性差异 ——一种叫做文体学的语言学研究——很方便的资源。

news_text = brown.words(categories = 'news')
fdist = nltk.FreqDist([w.lower() for w in news_text])
modals = ['can', 'could', 'may', 'might', 'must', 'will']
for m in modals:
    print(m+":", fdist[m])
relative_adverbs = ['what', 'when', 'where', 'who', 'why']
print('-'*80)
for ra in relative_adverbs:
    print(ra+":", fdist[ra])


# 使用 NLTK 提供的带条件的频率分布函数，统计不同文本的不同的词汇频率


cfd = nltk.ConditionalFreqDist((genre, word)
    for genre in brown.categories()
    for word in brown.words(categories=genre))
genres = ['news', 'religion', 'hobbies', 'science_fiction', 'romance', 'humor']
modals = ['can', 'could', 'may', 'might', 'must', 'will']
print(cfd.tabulate(conditions=genres, samples=modals))

'''
                  can could   may might  must  will 
           news    93    86    66    38    50   389 
       religion    82    59    78    12    54    71 
        hobbies   268    58   131    22    83   264 
science_fiction    16    49     4    12     8    16 
        romance    74   193    11    51    45    43 
          humor    16    30     8     8     9    13 

'''


# 路透社语料库包含 10,788 个新闻文档，共计 130 万字。
# 这些文档分成 90 个主题，按照 “训练”和“测试”分为两组。
# fileid 为“test/14826”的文档属于测试组

from nltk.corpus import reuters
# 可以以文档或类别为单位查找我们想要的词或句子。这些文本中最开始的
# 几个词是标题，按照惯例以大写字母存储。
searched_title = reuters.words('training/9865')[:14]
print(searched_title)

# 许多文本语料库都包含语言学标注，有词性标注、命名实体、句法结构、语义角色等。
# NLTK 中提供了很方便的方式来访问这些语料库中的几个，
# 还有一个包含语料库和语料样本 的数据包

print('='*100)
# 载入自己的语料库

from nltk.corpus import PlaintextCorpusReader

# 适合纯文本的方式

corpus_root = r'/Users/glad/python-study/翻译技术_NLP'
corpus_file = r'TheEconomist1015.txt'
# wordlists = PlaintextCorpusReader(corpus_root,'TheEconomist1015.txt ')
file_te_imp = PlaintextCorpusReader(corpus_root,corpus_file)
# print(wordlists.fileids())
# print(wordlists.words('connectives'))
print(file_te_imp.words())

# 适合已经解析过的文本的方式

from nltk.corpus import BracketParseCorpusReader
corpus_root = r'/Users/glad/Desktop'
corpus_file = r'OG_PAGE66_PASSAGE.txt'
file_og_imp = BracketParseCorpusReader(corpus_root,corpus_file)
print(file_og_imp.words())
# print(file_og_imp.raw())

print(file_te_imp.sents())
# print(file_te_imp.count('China'))
# print(file_te_imp.concordance('China'))




