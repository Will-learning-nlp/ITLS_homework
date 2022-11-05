# 1.1 分句与分词
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize

txt_file_te = open('TheEconomist1015.txt')

txt_file_te_str1 = ""

for i in range(20):
    aline = txt_file_te.readline().strip()
    if aline != '':
        txt_file_te_str1 += (aline + '. ')

print(txt_file_te_str1)

txt_file_te.close()

# 注意标点符号被视为一个单独的标记。
# 单词shouldn't分隔为should和n't。
# pinkish-blue确实被当作“一个词”来对待
print(sent_tokenize(txt_file_te_str1))
print(word_tokenize(txt_file_te_str1))

# 1.2 停用词
# 预处理的主要形式之一就是过滤掉无用的数据。
# 在自然语言处理中，无用词（数据）被称为停止词。
# 我们将把停止词当作不含任何含义的词，我们要把它们删除。


# 停用词表

from nltk.corpus import stopwords

stopwords_lst = stopwords.words('english')
print(stopwords_lst)


# 定义一个函数来计算文本中没有在停用词列表中的词的比例

def content_fraction(text):
    stopwords = nltk.corpus.stopwords.words('english')
    content = [w for w in text if w.lower() not in stopwords]
    return len(content)/len(text)


con_frac_text = content_fraction(nltk.corpus.reuters.words())
print(con_frac_text)
'''
['i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', "you're", "you've", "you'll", "you'd", 'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', "she's", 'her', 'hers', 'herself', 'it', "it's", 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', "that'll", 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', "don't", 'should', "should've", 'now', 'd', 'll', 'm', 'o', 're', 've', 'y', 'ain', 'aren', "aren't", 'couldn', "couldn't", 'didn', "didn't", 'doesn', "doesn't", 'hadn', "hadn't", 'hasn', "hasn't", 'haven', "haven't", 'isn', "isn't", 'ma', 'mightn', "mightn't", 'mustn', "mustn't", 'needn', "needn't", 'shan', "shan't", 'shouldn', "shouldn't", 'wasn', "wasn't", 'weren', "weren't", 'won', "won't", 'wouldn', "wouldn't"]
0.735240435097661
'''

stop_words = set(stopwords.words('english'))

aGreTxt = open('OG_PAGE66_PASSAGE.txt')
aGreTxt_str = aGreTxt.readline()
print(aGreTxt_str)

word_tokens = word_tokenize(aGreTxt_str)

filter_sent = [w for w in word_tokens if w not in stop_words]
print(filter_sent)
print('='*100)
filter_sent = []

for w in word_tokens:
    if w not in stop_words:
        filter_sent.append(w)

print(word_tokens)
print(filter_sent)

# 1.3  词干提取

from nltk.stem import PorterStemmer
# from nltk.tokenize import sent_tokenize, word_tokenize
filter_sent_wlst = filter_sent
ps = PorterStemmer()
ps_wlst = []
for w in filter_sent_wlst:
    ps_wlst.append(ps.stem(w))
print(ps_wlst)

# 1.4 词性标注
'''
POS tag list
CC    coordinating conjunction
CD    cardinal digit
DT    determiner
EX    existential there (like: "there is" ... think of it like "there exists")
FW    foreign word
IN    preposition/subordinating conjunction
JJ    adjective    'big'
JJR    adjective, comparative    'bigger'
JJS    adjective, superlative    'biggest'
LS    list marker    1)
MD    modal    could, will
NN    noun, singular 'desk'
NNS    noun plural    'desks'
NNP    proper noun, singular    'Harrison'
NNPS    proper noun, plural    'Americans'
PDT    predeterminer    'all the kids'
POS    possessive ending    parent's
PRP    personal pronoun    I, he, she
PRP$    possessive pronoun    my, his, hers
RB    adverb    very, silently,
RBR    adverb, comparative    better
RBS    adverb, superlative    best
RP    particle    give up
TO    to    go 'to' the store.
UH    interjection    errrrrrrrm
VB    verb, base form    take
VBD    verb, past tense    took
VBG    verb, gerund/present participle    taking
VBN    verb, past participle    taken
VBP    verb, sing. present, non-3d    take
VBZ    verb, 3rd person sing. present    takes
WDT    wh-determiner    which
WP    wh-pronoun    who, what
WP$    possessive wh-pronoun    whose
WRB    wh-abverb    where, when
'''

# 句子标记器，PunktSentenceTokenizer。
# 这个标记器能够无监督地进行机器学习，
# 可以在任何文本上进行实际的训练。

print('='*100)
from nltk.tokenize import PunktSentenceTokenizer
from nltk.corpus import gutenberg
import nltk

train_txt = gutenberg.raw('shakespeare-macbeth.txt')
sample_txt = gutenberg.raw('shakespeare-caesar.txt')

custom_sent_tokenizer = PunktSentenceTokenizer(train_txt)
tokenized = custom_sent_tokenizer.tokenize(sample_txt)


def process_content():
    try:
        for i in tokenized[:5]:
            words = nltk.word_tokenize(i)
            tagged = nltk.pos_tag(words)
            print(tagged)
    except Exception as e:
        print(str(e))


process_content()

# 也可以直接使用自带标记器

pos_tag_1 = nltk.pos_tag(word_tokenize('I was watching TV'))
print(pos_tag_1)

# 1.5 nltk分块
# 把词汇分成有意义的块。分块的主要目标之一是将所谓的“名词短语”分组。

# 分块--将词性标签与正则表达式结合起来。
# 正则表达式中利用 +（1或多），？（0或1），*（0或多），.（任意字符），匹配字符

# 重复代码，作为练习
from nltk.corpus import gutenberg
from nltk.tokenize import PunktSentenceTokenizer

train_txt_2 = gutenberg.raw('chesterton-ball.txt')
sample_txt_2 = gutenberg.raw('chesterton-thursday.txt')

custom_sent_tokenizer_2 = PunktSentenceTokenizer(train_txt_2)
tokenized_2 = custom_sent_tokenizer_2.tokenize(sample_txt_2)

print(type(tokenized_2))
# <class 'list'>
print(tokenized_2[:10])

print(type(custom_sent_tokenizer_2))
print(custom_sent_tokenizer_2)


def process_content_2():
    try:
        for i in tokenized_2[:2]:
            words = nltk.word_tokenize(i)
            # print(words) # 列表，元素为 单词字符串
            tagged = nltk.pos_tag(words)
            # print(tagged) # 列表， 元素为 元组，元组为字符串对，单词 对 标签
            chunkGram = r"""Chunk:{<RB.?>*<VB.?>*<NNP>+<NN>?}"""
            chunkParser = nltk.RegexpParser(chunkGram)
            chunked = chunkParser.parse(tagged)
            for subtree in chunked.subtrees():
                print(subtree)
            # print(chunked)
            # for subtree in chunked.subtrees(filter=lambda t: t.label()=='chunk'):
            #     print(subtree) # 无输出
            chunked.draw()
    except Exception as e:
        print(str(e))

# process_content_2()
# 这不是 NLTK 块属性中的“块”...
# 这是字面上的“块”，
# 因为这是我们给它的标签：
# chunkGram = r"""Chunk: {<RB.?>*<VB.?>*<NNP>+<NN>?}"""。

# 1.6 添加缝隙
# 分块之后，块中还有一些不想要的单词
# 添加缝隙与分块很像，它基本上是一种从块中删除块的方法。
# 从块中删除的块就是你的缝隙

from nltk.corpus import state_union
from nltk.tokenize import PunktSentenceTokenizer

train_txt_3 = state_union.raw("2005-GWBush.txt")
sample_txt_3 = state_union.raw("2006-GWBush.txt")

custom_sent_tokenizer_3 = PunktSentenceTokenizer(train_txt_3)

tokenized_3 = custom_sent_tokenizer_3.tokenize(sample_txt_3)

def process_content():
    try:
        for i in tokenized_3[5:]:
            words = nltk.word_tokenize(i)
            tagged = nltk.pos_tag(words)
            chunkGram = r"""Chunk: {<.*>+}
                                        }<VB.?|IN|DT|TO>+{"""
            chunkParser = nltk.RegexpParser(chunkGram)
            chunked = chunkParser.parse(tagged)

            chunked.draw()
    except Exception as e:
        print(str(e))

# process_content()

# 1.7  NLTK 的命名实体识别有两个主要选项：
# 识别所有命名实体，
# 将命名实体识别为它们各自的类型，如人物，地点，位置等

def entityRec():
    try:
        for i in tokenized_3[:5]:
            words = nltk.word_tokenize(i)
            tagged = nltk.pos_tag(words)
            nameEnt = nltk.ne_chunk(tagged, binary=True)
            # nameEnt.draw()
            print(nameEnt)
    except Exception as e:
        print(str(e))


entityRec()

print(nltk.__file__)

# 1.8 wordnet

# WordNet 是面向语义的英语词典，类似与传统辞典，但具有更丰富的结构。
# NLTK 中包 括英语 WordNet，共有 155,287 个词和 117,659 个同义词集合

# 同义词

from nltk.corpus import wordnet as wn

print(wn.synsets('motorcar'))

# [Synset('car.n.01')]
# motorcar 只有一个可能的含义，它被定义为 car.n.01，car 的第一个名词意义。
# car.n.01 被称为 synset 或“同义词集”，意义相同的词(或“词条”)的集合
print(wn.synset('car.n.01').lemma_names)
# <bound method Synset.lemma_names of Synset('car.n.01')>

# print(wn.synsets('car.n.01').lemma_names)
# 报错

from nltk.corpus import wordnet

# 同义词

syns = wordnet.synsets("program")

# 一个同义词
print(syns[0].name())

# 存粹同义词

print(syns[0].lemmas()[0].name())
# lemma 词根，词元（词的基本形式，如名词单数或动词的不定式形式）

# 定义
print(syns[0].definition())

# 单词使用例子
print(syns[0].examples())

# 反义词

synonyms = []
antonyms = []

for syn in wordnet.synsets("good"):
    for l in syn.lemmas():
        synonyms.append(l.name())
        if l.antonyms():
            antonyms.append(l.antonyms()[0].name())

print(set(synonyms))
print(set(antonyms))

# 比较词汇的相似性
w1 = wordnet.synset('football.n.01')
w2 = wordnet.synset('soccer.n.01')
print(w1.wup_similarity(w2))
# 0.96















