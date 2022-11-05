# 1. 概览
from __future__ import division
from nltk.book import *
print(text1)
print(text2)

"""
text1: Moby Dick by Herman Melville 1851
text2: Sense and Sensibility by Jane Austen 1811
text3: The Book of Genesis
text4: Inaugural Address Corpus
text5: Chat Corpus
text6: Monty Python and the Holy Grail
text7: Wall Street Journal
text8: Personals Corpus
text9: The Man Who Was Thursday by G . K . Chesterton 1908
"""

text1.concordance("monstrous")
# concordance 函数
# 词语索引视图显示一个指定单词的每一次出现，连同一些上下文一起显示。

text2.concordance("affection")
text3.concordance("lived")
text4.concordance("nation")
text5.concordance("lol")

# 词语索引使我们看到词的上下文。
# 例如:我们看到monstrous出现的上下文，如 the ___ pictures和the ___ size。
# 还有哪些词出现在相似的上下文中?
# 我们可以通过在被查询的文本名后添加函数名 similar，
# 然后在括号中插入相关的词来查找到。

text1.similar("monstrous")

'''
true contemptible christian abundant few part mean careful puzzled
mystifying passing curious loving wise doleful gamesome singular
delightfully perilous fearless
'''

text2.similar("monstrous")

'''
very so exceedingly heartily a as good great extremely remarkably
sweet vast amazingly
'''
# 观察不同的文本中得到的不同结果。text2使用这些词与text1不同;
# 在text2那里，monstrous 是正面的意思，有时它的功能像词 very 一样作 强调成分。
# 在text1那里，正面意思、负面意思都有；由此可见两人对同一个词汇的不同使用风格；

# 函数common_contexts允许我们研究两个或两个以上的词共同的上下文，
# 如monstrous和very。我们必须用方括号和圆括号把这些词括起来，中间用逗号分割。
text2.common_contexts(["monstrous", "very"])
'''
am_glad a_pretty a_lucky is_pretty be_glad
'''

text4.common_contexts(["men","women"])
text4.common_contexts(["sky","air"])

# 函数 disperse_plot([,,,])绘制一个单词在整个文本中的位置分布
# 下面的绘制图像可以用来研究随时间推移语言使用上的变化, 因为就职演说是按时间排列
# 文章越往后，时间越晚



from matplotlib import *
import numpy

# text3: The Book of Genesis
# text4: Inaugural Address Corpus

text4.dispersion_plot(["citizens", "democracy", "freedom", "duties", "America"])
text3.dispersion_plot(['God', 'he', 'she', 'man', 'woman', 'happy', 'anger'])

# 函数 generate, 生成随机文本
text4.generate(length=200)
# 第一次运行此命令时，由于要搜集词序列的统计信息而执行的比较慢。
# 每次运行它，输出的文本都会不同。
# 虽然文本是随机的，但重用了源文本中常见的词和短语，从而能感觉到它的风格和内容。
'''
Building ngram index...
obligations , and especially the truth that democratic government has
innate capacity to govern its affairs aright through the Province
ceded , by any timid forebodings of evil were not to overtake them
while I possess the property of the pecuniary estimates for the
advancement of civilization . , religion and a reckless disregard of
the Argonne , Omaha Beach , Salerno and halfway around the globe , and
nothing is more important in the House and the special attention of
the Government to interfere with the advice and equipment to free ones
; to the public agents intrusted with the others undone , the issues
and questions in dispute with reference to every circumstance that
could preserve or might endanger the benefits which will be settled on
the support of the government suffers in the support of the Government
. contributed to our country , I ask every American enjoys the
fullness of freedom comes to Americans the profound assurance that
effort and a prepared citizenry . a movement so fundamental to the
conference table in advance , to be satisfied . these have no sanction
by our first priorities , and hope may be compatible with the whole
'''

# 计数词汇
print(len(text3))

# 计数不重复词汇

sorted_set_text3 = sorted(set(text3))
# sorted() & set(text3)，
# 我们得到一个词汇项的排序表，
# 这个表以各种标点符号开始，然后是以 A 开头的词汇。大写单词排在小写单词前面。
# 我们通过求集合中项目的个数间接获得词汇表的大小。
# 再次使用 len 来获得这个数值。
# 小说中有 44,764 个标识符，但只有 2,789 个不同的词汇或“词类型”。
# 一个词类型是指一个词在一个文本中独一无二的出现形式或拼写。也就是说，这个词在词汇表中是唯一的。
# 我们计数的 2,789 个项目中包括标点符号，所以我们把这些叫做唯一项目类型而不是词类型。

print(sorted_set_text3)

len_set_text3 = len(set(text3))

print(len_set_text3)

'''
44764
['!', "'", '(', ')', ...
2789
'''

# text5 中 lol 出现了多少次?它占文本全部词数的百分比是多少?

cont_lol = text5.count("lol")
len_t5 = len(text5)
lol_percen = cont_lol/len_t5*100
print(lol_percen)

# 简单函数实现词频与词汇多样性计算


def lexical_diversity(text):
    return print(len(text) / len(set(text)))


def percentage(count, total):
    return print(100 * count / total)


percentage(text2.count('love'), len(text2))

# 表示《白鲸记》的开篇句  ['Call', 'me', 'Ishmael', '.']
print(sent1)

print(sent2)

print(sent3)

'''
['The', 'family', 'of', 'Dashwood', 'had', 'long', 'been', 'settled', 'in', 'Sussex', '.']
['In', 'the', 'beginning', 'God', 'created', 'the', 'heaven', 'and', 'the', 'earth', '.']
'''
# 列表相加操作
print(sent2+sent3)

# 列表索引与切片
print(text5[16715:16735])
