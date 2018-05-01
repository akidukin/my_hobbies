#! usr/bin/env
# -*- coding : utf-8 -*-

'''
BigQueryからデータを持ってきて分析できるようにする
'
select title, price, sold, url, col_name, ele_name, pc_url
from `Project_ebay.20180430_tb
'
でデータを取得する 

習得したデータを適当にフォルダーにおいて、コマンドライン上で
ebay_test.py filename
する
'''
import csv
import os
import numpy as np
import sys

file = sys.argv[1]

# 該当のファイルがちゃんと入っているか確認する
try:
	file in os.listdir()
except:
	raise("Can't find files")

## 配列になっているデータを取り出せないからpandasで読み込む
## df = []
##f = open(file,'r',encoding = 'UTF-8')
##reader = csv.reader(f,"")
##header = next(f)
##for r in reader:
##	df = df + [r]
##f.close()

df = pd.read_csv(file,sep = ",", header = 0)
df = np.array(df)