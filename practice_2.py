# 2. 简单的统计

from nltk.book import *


# 频率分布

# 使用 FreqDist 寻找《白鲸记》中最常见的 50 个词


from nltk.probability import FreqDist

fdist1 = FreqDist(text1)


print(fdist1)
print(type(fdist1))
vocabulary1 = fdist1.keys()
# top_50_words = vocabulary1[:50]  # 无法输出？？？
# print(vocabulary1)
# print(top_50_words)
# print(vocabulary1[:50])
whale_freq = fdist1["whale"]
print(whale_freq)
'''
第一次调用 FreqDist 时，传递文本的名称作为参数。
《白鲸记》中的总的词数(“结果”)——260,819。
表达式 keys()提供了文本中所有不同类型的链表，
可以通过切片看看这个列表的前 50 项。
'''

fdist1.plot(50, cumulative=True)
# 《白鲸记》中 50 个最常用词的累积频率图，这些词占了所有标识符的将近一半

# text7: Wall Street Journal
fdist7 = FreqDist(text7)
fdist7.plot(80, cumulative=True)


hapaxes_lst = fdist1.hapaxes()
# hapaxes 罕用语
print(len(hapaxes_lst))

# 长词筛选
v = set(text1)
long_words = [w for w in v if len(w) > 15]
sorted_lw_ls = sorted(long_words)
print(sorted_lw_ls)

# 长度与频次筛选
fdist5 = FreqDist(text5)

freq_len_7_7_lst_text5 = sorted([w for w in set(text5) if len(w) > 7 and fdist5[w] >7])
print(freq_len_7_7_lst_text5)

# 词语搭配与bigram
# 要获取搭配，先从提取文本词汇中的词对也就是双连词开始。使用函数 bigrams()

from nltk.util import bigrams

bigrams_test = bigrams(['more', 'is', 'said', 'than', 'done'])
print(list(bigrams_test))

text4.collocations()
text4.collocations(num=10, window_size=3) # 改变参数，定制输出 搭配的 长度 和 数量

'''
United States; fellow citizens; years ago; four years; Federal
Government; General Government; American people; Vice President; God
bless; Chief Justice; one another; fellow Americans; Old World;
Almighty God; Fellow citizens; Chief Magistrate; every citizen; Indian
tribes; public debt; foreign nations
'''

# 计数其他文本数据

text1_wlen = [len(w) for w in text1]  # 迭代记录每个词的长度
# print(text1_wlen)

fdist = FreqDist(text1_wlen)
print(fdist) # 260819个元素，每个元素代表 每个词的长度

#<FreqDist with 19 samples and 260819 outcomes>

print(fdist.keys()) # 字符长度的种类
print(fdist.items()) # 不同长度字符的频率

print(fdist.max())
print(fdist[3])
print(fdist.freq(3))

'''
dict_keys([1, 4, 2, 6, 8, 9, 11, 5, 7, 3, 10, 12, 13, 14, 16, 15, 17, 18, 20])
dict_items([(1, 47933), (4, 42345), (2, 38513), (6, 17111), (8, 9966), (9, 6428), (11, 1873), (5, 26597), (7, 14399), (3, 50223), (10, 3528), (12, 1053), (13, 567), (14, 177), (16, 22), (15, 70), (17, 12), (18, 1), (20, 1)])
3
50223
0.19255882431878046
'''
print(sent7)

# 列表 创建 限定单词长度的单词集合
len_3_w = [w for w in sent7 if len(w) == 3]
print(len_3_w)