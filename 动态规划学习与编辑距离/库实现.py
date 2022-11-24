import Levenshtein as levt

# 计算一个字串转化成另一个字串最少的操作次数，在其中的操作包括插入、删除、替换
d1 = levt.distance('Levenshtein', 'Lenvinsten')
print(d1)

# ratio方法专门用来计算文本相似度
# 计算公式为 r = (sum - ldist) /sum, 其中 sum 是指 str1 和 str2 字串的长度总和，ldist 是类编辑距离
print(levt.ratio("good", "bad"))

# 计算2个字符串list的相似度
import jieba

ancient_str1 = '景帝觉而坐阁下，果有赤龙如雾，来蔽户牖。'
modern_str1 = '景帝一下子惊醒了，就到崇芳阁下坐下，果然见空中有一条红色的龙腾云驾雾，把崇芳阁的门窗都笼罩了。'

a1_jieba_gene = jieba.cut(ancient_str1)
m1_jieba_gene = jieba.cut(modern_str1)

l1 = list(a1_jieba_gene)
l2 = list(m1_jieba_gene)

listSimilar=levt.seqratio(l1,l2)

print('l1:', repr(l1))
print('l2:', repr(l2))
print("古文与译文相似度为", str(listSimilar))

# 计算汉明距离，两个字符串的长度必须相同。返回两个字串之间对应位置上不同字符的个数。
hm1 = levt.hamming('Hello world!', 'Holly grail!')
print(hm1)
hm2 = levt.hamming('Brian', 'Jesus')
print(hm2)

# 计算两个字符串的 Jaro 字符串相似度度量
# Jaro 字符串相似度度量适用于短字符串，例如个人姓氏。 对于完全不同的字符串，它是 0,  而 1 表示相同的字符串。
j1 = levt.jaro('Brian', 'Jesus')
print(j1)
j2 = levt.jaro('analogy', 'analysis')
print(j2)

