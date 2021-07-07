
# -*- coding: gbk -*-

# Original work Copyright 2018 The Google AI Language Team Authors.
# Modified work Copyright 2019 Rowan Zellers
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
�����ܣ�  �ı�������д��
          a: �������ⳤ�ȵģ������Զ��壺��
          b: ����ɷ�����ɵľ���
"""
import sys
from urllib.request import urlopen
from random import randint
import collections
import tensorflow as tf
import sys
import requests
import time
import random
from utils import *
from token_reader import *


class sentence_producer(base):
    def __init__(self):
        self.text = ""
        self.dict = []

    def wordListSum(self, wordList):
        """����һ�������б�����"""
        # ����һ������sum����ʼ��
        sum = 0
        # ����word��value �������������������
        # items()�������б��ؿɱ�����(��, ֵ) Ԫ������,����֮���ֵ������е������б����ʽ���أ��б��е�ÿһ����Լ�ֵ�Ե���ʽ���ֵ�
        # ���б�����-ֵ
        for word, value in wordList.items():
            # ���￪ʼ�Լ�
            sum += value
        # ����ֵ������
        return sum

    # 2
    def retrieveRandomWordself, (wordList):
        """�����������"""
        # wordList������ǳ�������һ�������Ĵ����б���Ƶ����ɵ��ֵ䣬Ȼ�����ͳ�Ƶĸ����������һ���ʡ�
        # randint()��������һ��ָ����Χ�ڵ�����
        # ����wordListSun()������������Χ����1-sum��
        randIndex = randint(1,wordListSum(wordList))

        # ����retrieveRandomWord(wordList)
        # ��ʵ���Ǳ����ֵ�
        for word, value in wordList.items():
            # ʹ�ñ���wordListSum()�����Ľ�����еݼ�
            randIndex -= value
            if randIndex <=0:
                return word

    # 3
    def buildWordDict(self, text):
        """buildWordDict(text)���������ı�����"""
        # �޳����з�������
        # ����Ҳ������re.sub(pattern, repl, string, count=0, flags=0)
        # text = text.sub('(\n|\r|\t)+', " ", text)
        # text = text.sub('\"', "", text)
        text = text.replace("\n", " ")
        text = text.replace("\"", "")

        # ��֤ÿ�������Ŷ���ǰ��ĵ�����һ�� ���ã��������ᱻ�޳�������������ɷ�����
        punctuation = [',', '.', ';', ':']

        for symbol in punctuation:
            # ����һ����ʾ���ŵ�symbol�����������б�punctuation
            text = text.replace(symbol, " " + symbol + " ")
        # split()����ָ����ͨ��ָ���ָ������ַ���������Ƭ
        # ����ָ������ͨ��" "�������з�
        words = text.split(" ")
        # ���˿յ����б�
        words = [word for word in words if word!=""]
        print("����words:",words)

        # ����һ�����ֵ�
        wordDict = {}
        for i in range(1, len(words)):
            # ����һ������i,���ã��������˵ĵ���(��1-len(words))
            # ���wordDict�ֵ��в�����words[i-1]
            if words[i-1] not in wordDict:
                # Ϊ�����ڵĵ���(words[i - 1])�½�(���)һ���ֵ�
                wordDict[words[i - 1]] = {}
                print("\n����1 wordDict[words[i - 1]] = {} : ",wordDict)
                # print(wordDict)
            # ���words[i](��i������)������wordDict[words[i - 1]](Ϊ�����ڵ����½����ֵ�-�������ڵĵ�����ӵ��½����ֵ���)
            if words[i] not in wordDict[words[i - 1]]:
                # �� wordDict[words[i - 1]] = {} ��ֵ��ֵ��һ���ֵ䣩�������
                wordDict[words[i - 1]][words[i]] = 0
                print("\n����2 wordDict",wordDict)
            # wordDict[a][b] += 1 --------->�������ά�����a�е�b������+1
            # λ��+1
            # print(words)
            wordDict[words[i - 1]][words[i]] = wordDict[words[i - 1]][words[i]] + 1
            print("����3 wordDict:", wordDict)

        # �����ֵ��ֵ
        return wordDict

if __name__ == "__main__":
    f = open(r"wenben.txt","r")
    # ���ж�ȡ
    text = f.readline()
    # f.close()
    # text = open("wen.txt",encoding='utf-8')
    # text = str(urlopen("http://pythonscraping.com/files/inaugurationSpeech.txt").read(), 'utf-8')
    # ����ʵ��--buildWordDict(text)���������ı�����
    wordDict = buildWordDict(text)
    # ��������Ϊ()������ɷ���
    length = 10
    chain = ""
    currentWord = "B"
    # ��������Ʒ���
    for i in range(0,length):
        chain += currentWord + " "
        # ����currentWord-->����wordDict[currentWord]-->ʹ��retrieveRandomWord()��������currentWord
        currentWord = retrieveRandomWord(wordDict[currentWord])
    print(chain)