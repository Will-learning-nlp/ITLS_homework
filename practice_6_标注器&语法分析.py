import nltk
from nltk import word_tokenize
s = 'I am writing homework'
print(nltk.pos_tag(word_tokenize(s)))

# 在一个典型的预处理中，我们可能想寻找所有的名词

tagged = nltk.pos_tag(word_tokenize(s))
allnoun = [word for word, pos in tagged if pos in['NN','NNP']]
print(allnoun)
allverb = [word for word, pos in tagged if pos in ['VB','VBD','VBG','VBN']]
print(allverb)

from nltk.tag.stanford import StanfordPOSTagger

# stan_tagger = StanfordPOSTagger('models/english-bidirectional-distdim.tagger', 'standford-postagger.jar')

# tokens = nltk.word_tokenize(s)
# s_sp = stan_tagger.tag(tokens)
# print(tokens)
# print(s_sp)
# 从Stanford网站下载斯坦福标注器。将jar和模型提取
# 到一个文件夹中，在P OST agger的参数中，给出一个绝对路径。

# 布朗语料库中POS标签的频率分布

from nltk.corpus import brown

tags = [tag for (word, tag) in brown.tagged_words(categories='news')]
print(nltk.FreqDist(tags))


# 使用有限的词汇和通用规则，写一个语法。

from nltk import CFG

test_grammar = nltk.CFG.fromstring("""
S -> NP VP
VP -> V NP
V -> "eats" | "drinks" 
NP -> Det N 
Det -> "a" | "an" | "the" 
N -> "president" |"Obama" |"apple"| "coke" 
""")

# NP is noun phrase (chunk that has noun in it)
# Det is determiner used in the sentences
# N some example nouns
print(test_grammar.productions())















