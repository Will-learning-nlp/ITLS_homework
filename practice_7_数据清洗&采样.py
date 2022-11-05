import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import csv

def preprocessing(text):
    # text = text.decode("utf8") # 此处不需要解码，若执行反而出错
    # 取词
    tokens = [word for sent in nltk.sent_tokenize(text) for word in
              nltk.word_tokenize(sent)]
    # 去除停用词
    stop = stopwords.words('english')
    tokens = [token for token in tokens if token not in stop]
    # 去除少于3个字母的词汇
    tokens = [token for token in tokens if len(token) >= 3]
    # 小写化
    tokens = [word.lower() for word in tokens]

    # lemmatize
    lmtzr = WordNetLemmatizer()
    tokens = [lmtzr.lemmatize(word) for word in tokens]
    preprocessed_text = ' '.join(tokens)
    return preprocessed_text

# 对SMS文件进行语法分析，清洗其内容，获得更清洁的SMS文本
# 创建了两个列表，获得了清洁过的所有SMS的内容和类别标签。
# 使用机器学习的术语来讲就是所有的X和Y


import pandas as pd

csv_reader = pd.read_csv('/Users/glad/python-study/翻译技术_NLP/SMSSpamCollection.txt', delimiter='\t', header=None)
# print(csv_reader)
# !!! 这种方式处理，将得到表格文件，如下面打印注释
y, X_train = csv_reader[0], csv_reader[1]
# print(y)
# print(X_train)
'''
         0                                                  1
0      ham  Go until jurong point, crazy.. Available only ...
1      ham                      Ok lar... Joking wif u oni...
2     spam  Free entry in 2 a wkly comp to win FA Cup fina...
3      ham  U dun say so early hor... U c already then say...
4      ham  Nah I don't think he goes to usf, he lives aro...
...    ...                                                ...
5567  spam  This is the 2nd time we have tried 2 contact u...
5568   ham               Will ü b going to esplanade fr home?
5569   ham  Pity, * was in mood for that. So...any other s...
5570   ham  The guy did some bitching but I acted like i'd...
5571   ham                         Rofl. Its true to its name

[5572 rows x 2 columns]
'''
smsdata = open('SMSSpamCollection.txt')
sms_data = []
sms_labels = []

csv_reader = csv.reader(smsdata, delimiter='\t')
print(csv_reader)
# 这种方式处理txt，得到的是n个列表
# ['ham', 'Ok lar... Joking wif u oni...']
# ['spam', "Free entry in 2 a wkly"]
count = 0
for line in csv_reader:
    # print(line)
    # count += 1
    # if count ==5:
    #     break
    sms_labels.append(line[0])
    #
    sms_data.append(preprocessing(line[1]))

smsdata.close()

print(sms_labels[:5])
print(sms_data[:5]) # 为 sms短信的 具体内容
# 格式是列表，每个元素是一个字符串--英文短信句子

import sklearn
import numpy as np

# 以上为数据清洗，得到了列表形式的基本数据
# 下面把基本数据以 科学 合理 的形式 采样
# 也即是 训练集 测试集 分类

trainset_size = int(round(len(sms_data) * 0.70))

print('本分类器的测试集大小为' + str(trainset_size) + '\n')


x_train = np.array([''.join(elem) for elem in sms_data[0:trainset_size]])
# join的功能：不确定，因为直接array列表也可以有相同的输出
'''
x_trian = np.array(smsdata_data[0:trainset_size])
print('before join'*40)
print(x_trian)
'''
# 取70%，3900个元素作为训练集
# print('after join'*40)
# print(x_train)


y_train = np.array([''.join(elem) for elem in sms_labels[0:trainset_size]])

x_test = np.array([''.join(elem) for elem in sms_data[trainset_size:len(sms_data)]])
y_test = np.array([''.join(elem) for elem in sms_labels[trainset_size:len(sms_labels)]])

print(x_train)
print(y_train)

# 将整个文本转换成向量形式。这种向量形式称为术语-文档矩阵（term-document matrix）
# 词袋（Bag Of Word，BOW）表示。
# 是文本挖掘和其他应用中最常用的表示方法之一。
# 从本质上讲，为了生成这种类型的表示，不考虑单词之间的任何上下文。

from sklearn.feature_extraction.text import CountVectorizer

def vectorize_auto(a_lst):
    sms_exp = []
    for line in a_lst:
        sms_exp.append(preprocessing(line))
    # a_lst为 sms短信的 具体内容
    # 格式是列表，每个元素是一个字符串--英文短信句子
    vectorizer = CountVectorizer(min_df=1) #??? df is what
    X_exp = vectorizer.fit_transform(sms_exp)
    print('||'.join(vectorizer.get_feature_names()))
    print(X_exp.toarray())


vectorize_auto(['otherwise part time job na-tuition', "thank you 've wonderful"])

# 将文档中每个单词出现的次数除以总单词数，就可以解决不同篇幅文章的对比问题。
# 这个新特征称为词频（Term Frequency，TF）

# 词频-逆文件频率（Term Frequency–Inverse Document Frequency，TF-IDF）
# 按比例缩小在语料库众多文档中都出现的单词的权重，
# 这样这些单词的信息量就比起那些在语料库中出现在较少文档中的单词的信息量小




