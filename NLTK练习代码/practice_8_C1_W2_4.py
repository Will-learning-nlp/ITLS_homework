from utils import process_tweet, lookup
import pdb
from nltk.corpus import stopwords, twitter_samples
import numpy as np
import pandas as pd
import nltk
import string
from nltk.tokenize import TweetTokenizer
from os import getcwd
import w2_unittest

filePath = f"{getcwd()}/../tmp2/"
nltk.data.path.append(filePath)

all_positive_tweets = twitter_samples.strings('positive_tweets.json')
all_negative_tweets = twitter_samples.strings('negative_tweets.json')

test_pos = all_positive_tweets[4000:]
train_pos = all_positive_tweets[:4000]

test_neg = all_negative_tweets[4000:]
train_neg = all_negative_tweets[:4000]

train_x = train_pos + train_neg
test_x = test_pos + test_neg

train_y = np.append(np.ones(len(train_pos)), np.zeros(len(train_neg)))
test_y = np.append(np.ones(len(test_pos)), np.zeros(len(test_neg)))

# 第一部分 处理数据
# 去除无用词，各种符号，标点，词干处理， 使用封装好的函数 process_tweet
# 第一部分第一节

def count_tweets(result, tweets, ys):
    '''
    :param result: 一个字典，用于记录每个元组（词汇，情感色彩）和它在所有对应情感色彩推文中出现的频次
    :param tweets: 一个列表，每个元素为一个字符串
    :param ys: 一个列表，对应推文列表每个元素的情感色彩
    :return: result
    '''
    for y, tweet in zip(ys, tweets):
        for word in process_tweet(tweet):
            pair = (word, y)
            # result[pair] = result.get(pair, 0) + 1
            if pair in result:
                result[pair] += 1
            else:
                result[pair] = 1
    return result


# result = {}
# tweets = ['i am happy', 'i am tricked', 'i am sad', 'i am tired', 'i am tired']
# ys = [1, 0, 0, 0, 0]
# print(count_tweets(result, tweets, ys))

w2_unittest.test_count_tweets(count_tweets)

# 第二部分 训练模型

# 首先用上一部分封装的函数得到freqs字典，


freqs = count_tweets({}, train_x, train_y)
# print(freqs)
# print(freqs.keys())
# print(len(freqs)) 11428
# 使用set函数将字典转化为集合时，只是收录了字典中的key
def train_naive_bayes(freqs, train_x, train_y):
    '''
    :param freqs: 键为元组（词，情感色彩1/0），值：频次
    :param train_x: 一个列表，包含所有推文
    :param train_y: 一个列表，为1或0，与train_x中推文色彩一致
    :return: logprior，一个值; loglikelihood，一个字典，单词对应其log likelihood值，为训练结果
    '''
    loglikelihood = {}
    logprior = 0
    # print(set(freqs))
    vocab = set([wordset[0] for wordset in freqs.keys()]) # 这行代码造成的错误，反复检查了代码2-3个小时,set位置造成错误
    # vocab = [wordset[0] for wordset in set(freqs)]  得到11428个词汇
    # print(vocab)
    V = len(vocab)
    # print(V) #11428--->9162

    N_pos = 0
    N_neg = 0
    for key in freqs.keys():
        if key[1] > 0:
            N_pos += freqs[key]
        else:
            N_neg += freqs[key]

    D = len(train_y)
    D_pos = 0
    D_neg = 0

    for i in train_y:
        if i > 0:
            D_pos += 1
        else:
            D_neg += 1

    # P_D_pos = D_pos/D
    # P_D_neg = D_neg/D

    logprior = np.log(D_pos) - np.log(D_neg)

    for word in vocab:
        # freqs_pos = 0
        # freqs_neg = 0
        # p_w_pos = 0
        # p_w_neg = 0
        if (word, 1) in freqs.keys():
            freqs_pos = freqs[(word, 1)]
        else:
            freqs_pos = 0

        if (word, 0) in freqs.keys():
            freqs_neg = freqs[(word, 0)]
        else:
            freqs_neg = 0

        p_w_pos = (freqs_pos + 1) / (N_pos + V)
        p_w_neg = (freqs_neg + 1) / (N_neg + V)

        # loglikelihood[word] = np.log(p_w_pos) - np.log(p_w_neg)
        loglikelihood[word] = np.log(p_w_pos / p_w_neg)

    return logprior, loglikelihood

# UNQ_C3 (UNIQUE CELL IDENTIFIER, DO NOT EDIT)
logprior, loglikelihood = train_naive_bayes(freqs, train_x, train_y)
print(logprior)
print(len(loglikelihood))

# w2_unittest.test_train_naive_bayes(train_naive_bayes, freqs, train_x, train_y)


# w2_unittest.test_train_naive_bayes(train_naive_bayes, freqs, train_x, train_y)

# 第三部分 测试

def naive_bayes_predict(tweet, logprior, loglikelihood):
    word_l = process_tweet(tweet)
    p = 0
    p += logprior

    for word in word_l:
        if word in loglikelihood:
            p += loglikelihood[word]
        # else:
        #     p += 0
    return p

# UNQ_C5 (UNIQUE CELL IDENTIFIER, DO NOT EDIT)
# Experiment with your own tweet.
my_tweet = 'She smiled.'
p = naive_bayes_predict(my_tweet, logprior, loglikelihood)
print('The expected output is', p)

w2_unittest.test_naive_bayes_predict(naive_bayes_predict)

def test_naive_bayes(test_x, test_y, logprior, loglikelihood, naive_bayes_predict=naive_bayes_predict):
    '''
    :param test_x: 推文列表，元素为字符串
    :param test_y: 列表，元素为1或0
    :param logprior:
    :param loglikelihood:
    :param naive_bayes_predict:
    :return: accuracy
    '''
    accuracy = 0
    y_hats = []
    for tweet in test_x:
        # 如果预测值大于0
        if naive_bayes_predict(tweet, logprior, loglikelihood) > 0:
            y_hat_i = 1
        else:
            y_hat_i = 0

        y_hats.append(y_hat_i)

    error = 0
    num_right = 0
    test_yl = np.squeeze(test_y)
    for k in range(len(y_hats)):
        if y_hats[k] != test_yl[k]:
            error += 1
    # error = np.mean(np.array(y_hats).transpose() != np.array(test_y))
    accuracy = (len(test_yl)-error) / len(test_yl)
    # accuracy = 1- error
    return accuracy

print("Naive Bayes accuracy = %0.4f" %
      (test_naive_bayes(test_x, test_y, logprior, loglikelihood)))
# UNQ_C7 (UNIQUE CELL IDENTIFIER, DO NOT EDIT)
# Run this cell to test your function
for tweet in ['I am happy', 'I am bad', 'this movie should have been great.', 'great', 'great great', 'great great great', 'great great great great']:
    p = naive_bayes_predict(tweet, logprior, loglikelihood)
    print(f'{tweet} -> {p:.2f}')
# Feel free to check the sentiment of your own tweet below
my_tweet = 'you are bad :('
naive_bayes_predict(my_tweet, logprior, loglikelihood)
w2_unittest.unittest_test_naive_bayes(test_naive_bayes, test_x, test_y)























