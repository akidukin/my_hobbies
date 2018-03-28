#!bin/usr/env
# -*- coding : utf-8 -*-

## convert img to array strings for public

import cv2
import numpy as np
import os
import json
import sys

def renames(path):
	refile = os.listdir(path)
	Refile = [path + x for x in refile]
	length = len(refile)
	re = [path + '{0:05}'.format(x)+".jpg" for x in range(length)]
	for i in range(length):
		os.rename(Refile[i], re[i])
	return(os.listdir(path),refile)

def convert_img_to_array(cur_filenm, or_filenm, path, dic):
	files = [path + x for x in cur_filenm]
	key_name = [x.replace(".jpg","") for x in or_filenm]
	print("length = " + str(len(files)))
	for f in range(len(files)):
		dic[key_name[f]] = cv2.imread(files[f])
		sys.stdout.write("\r{}".format(f))
    	sys.stdout.flush()
	return(dic)


filepath = './../dmm/'
print("reaname files")
CurFilename, OriFilename = renames(filepath)
actor_array = {}
print("converte png to array strings")
converted = convert_img_to_array(CurFilename,OriFilename,filepath,actor_array)
print("file output")
f = open("actors_array.json","w")
json.dump(converted,f)
