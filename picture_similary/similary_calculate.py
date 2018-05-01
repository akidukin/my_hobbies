#!usr/bin/env
# -*- coding : utf-8 -*-

import cv2
import numpy as np
from matplotlib import pyplot as plt
import os
from PIL import Image

## 顔抽出後のフォルダー作成
if "face_output" not in os.listdir():
	os.mkdir("face_output")

def renames(files):
	length = len(files)
	refile = os.listdir()
	re = ['{0:04}'.format(x)+".jpg" for x in range(length)]
	for i in range(length):
		os.rename(files[i], re[i])
	return(os.listdir(),refile)

## 分類器読み込み
cascade_path = "C:/Users/USER/Anaconda3/Library/etc/haarcascades/haarcascade_frontalface_alt.xml"
faceCascade = cv2.CascadeClassifier(cascade_path)

## テスト画像読み込み
## きっと画像サイズを合わせないとダメになるからのちのちで工夫する
pf,of = renames(os.listdir())
tmp_p = cv2.imread(pf[2])
tmp_p = cv2.resize(tmp_p,(200,200))
## cv2.imshow("color",tmp_p)  ## 読み込まれてるか確認

## グレースケール変換 & 顔抽出
grayscale = cv2.cvtColor(tmp_p,cv2.COLOR_BGR2GRAY)
fc = faceCascade.detectMultiScale(grayscale, scaleFactor=1.2, minNeighbors=2, minSize=(10, 10))
x = fc[0][0];y = fc[0][1];w = fc[0][2];h = fc[0][3]
fp = grayscale[y:y+h, x:x+w]
## cv2.imshow("color",fp)
## cv2.imwrite("./face_output/"+of[3], fp)

## エッジ抽出
## parameter は 
cv2.Canny(fp,i[0],i[1])