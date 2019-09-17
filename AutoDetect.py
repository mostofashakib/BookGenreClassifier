"""

This is a program which takes in a json and csv file and scans the json for keywords associated with
scores then it returns the genre of the books along with their scores in a sorted order.
Language: Python 3.7.2
Written by: Mostofa Adib Shakib

"""

import json
import pandas as pd
import re
from collections import deque

words = []
title = []

with open('sample_book_json.txt') as json_file:
    data = json.load(json_file)
    for i in data:
    	for j in i['description'].split('\t'):
    		words.append(j)
    	for j in i['title'].split('\t'):
    		title.append(j)

filename = "sample_genre_keyword_value.csv"

df = pd.read_csv(filename,  usecols=[0, 1, 2])

listA = []
for i in words:
	placeHolder = dict()
	tracker = dict()
	stack = deque()
	for pattern in df.values:
		j = re.sub(r'[^\w\s]',' ',i)
		temp = re.findall(pattern[1], j)
		if temp:
			count = j.count(pattern[1])
			if pattern[0] not in placeHolder:
				if count == 1:
					placeHolder[pattern[0]] = pattern[2]
					tracker[pattern[0]] = 1
				else:
					placeHolder[pattern[0]] = pattern[2]
					tracker[pattern[0]] = 1
					count = count - 1
					stack.append([pattern[0], pattern[1], count, pattern[2]])
			elif pattern[0] in placeHolder:
				if count > 1:
					placeHolder[pattern[0]] = placeHolder[pattern[0]] + pattern[2]
					tracker[pattern[0]] += 1
					count = count - 1
					stack.append([pattern[0], pattern[1], count, pattern[2]])
				else:
					placeHolder[pattern[0]] = placeHolder[pattern[0]] + pattern[2]
					tracker[pattern[0]] += 1
		elif stack:
			temp2 = stack.popleft()
			average = (placeHolder[temp2[0]]) / tracker[temp2[0]]
			total_count = temp2[2] + tracker[temp2[0]]
			placeHolder[temp2[0]] = pattern[2] * total_count

	listA.append(placeHolder)

zipped = zip(title, listA) 
zipped = list(zipped) 
res = sorted(zipped, key = lambda x: x[0])

for i in res:
	i = list(i)
	for j in i[0].split('\t'):
		print(j)
	for k,v in i[1].items():
		print(k,',', v)