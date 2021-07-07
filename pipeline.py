# -*- coding: gbk -*-
####################################################################
# Original work Copyright 2018 The Google AI Language Team Authors.
# Modified work Copyright 2019 Rowan Zellers
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# ����Ŀ�����ڼ���������;���������п�Դ���֣���ֹ�����κ���ҵ��;
#####################################################################



# ʹ�ô��غõ�EssayKilelrBrain����ģ�鹹��pipeline���˵�������ı�
# ���ֺ��Ĵ����Ѽ��ܣ���Ҫ��ȡ�����汾�븽�ϸ���/�о���������֤��

from absl import app
from absl import flags
import collections
import tensorflow as tf
import sys
import requests
import numpy as np
import pandas as pd
import time
import random
import logging

from AutoBrainBase import *
from RecognizaitonNetwork.text_detection_video import *
from RecognizaitonNetwork.crnn import *
from RecognizaitonNetwork.train import *
from LanguageNetwork.GPT2.scripts import *
from LanguageNetwork.BERT.models import *
from LanguageNetwork.BERT.utils import *
from ScoringNetwork.AutoFormatter import *
from ScoringNetwork import *

from utils import *

tf.logging.set_verbosity(tf.logging.ERROR)
tf.get_logger().setLevel('INFO')
tf.autograph.set_verbosity(1)

FLAGS = flags.FLAGS
flags.DEFINE_string('gpu', None, 'comma separated list of GPU(s) to use.')

result = []

class EssayKillerPipeline(AutoBrainBase):
	"""
	@params
	input_feed: text input_feed
	sequence_len: sequence length
	...
	In order to prevent the EssayKiller framework from being maliciously registered, used or 
	copied, the pipeline core code and construction classes are temporarily not open-sourced

	If you have academic needs, please bring an individual or institution's academic needs 
	statement and send an email to deanyuton@gmail.com. According to the stated information, 
	I will send the full version of the code and test data to the given mailbox.
	
	Thanks for understanding.

	Ϊ��ֹ�Զ���д����ܱ��˶�����ע�����û򸴿̣�pipeline���Ĵ����빹�����ݲ���Դ
	����ѧ����Ҫ������ϸ��˻������ѧ����������������ʼ���deanyuton@gmail.com
	���ݳ�����Ϣ���ҽ��ᷢ��������Ĵ�����������ݵ����������䡣
	
	��л���~
	"""
	def __init__():
		self.config = FLAGS.config
		pass 

	def enable_textdetect(self):
		'''
		������Ƶ��⣬��Ӳ������˻�ȡ��Ƶ���ļ�
		Ӳ�����ã�Logitech C930C
		@params:video��Ƶ������˿�
		'''
		pass

	def generage_text_from_videostream(self):
		pass 

	def preprocess_exam(self):
		pass

	def summarize_exam_topic(self):
		pass

	def sentence2network(self):
		pass 

	def essay_writter_core(self):
		pass

	def scoring_to_best_essay(self):
		pass 

	def formatting_essay_output(self):
		pass


		
def main(argv):
    del argv
    if FLAGS.gpu:
        os.environ['CUDA_VISIBLE_DEVICES'] = FLAGS.gpu
    else:
        print('Please assign GPUs.')
        exit()

print("test sample in trained model...")
if __name__ == "__main__":
	try:
		pass
	except:
		print("pipeline has failed...")
	#dicts = result[0].split(":")
	#plexity = result.get['ppl']
	print("the final ppl score is: \n",scores )
	print("the final text output as :", text)
	print(sum(result))
