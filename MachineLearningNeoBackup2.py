#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#Machine Learning with Python!
from collections import defaultdict
import math

neo_chars = 'abdefgǧhiîklmnoprřsştuvwxyz'
eng_chars = 'abcdefghijklmnopqrstuvwxyz'
all_chars = ''
for char_database in [neo_chars,eng_chars]:
    for char in char_database:
        if char not in all_chars:
            all_chars += char
#all_chars = neo_chars+eng_chars

def process(file_name): 
  f = open(file_name, 'r')
  
  lines = []
  lines = f.readlines()
  
  freq_dict = {}
  scaled_freq_dict = {}
  for char in all_chars:
      freq_dict[char] = 0
      scaled_freq_dict[char] = 0
  
  for line in lines:
    
    line_lower = line.lower()
    line_lower_strip = line_lower.strip('\n')

    for char in line_lower_strip:
        if char in all_chars:
            freq_dict[char] += 1   
  f.close()
  
  total = 0
  
  for char in freq_dict:
      total += freq_dict[char]
  for char in freq_dict:
      scaled_freq_dict[char] = round(freq_dict[char]/total,5)
  #print(total)
  return scaled_freq_dict

def empty(dicto):
    k = 0
    for key in dicto:
        if key in all_chars:
            k += dicto[key]
    if k == 0:
        return True
    elif k != 0:
        return False


def sorted_by_freq(freq_dict_original):
    sorted_freq_list = []
    
    freq_dict = {}
    for key in neo_train:
        freq_dict[key] = freq_dict_original[key]
    
    while empty(freq_dict) == False:
        max_freq = 0
        max_char = ''
        for char in freq_dict:
            if freq_dict[char] > max_freq:
                max_freq = freq_dict[char]
                max_char = char
        
        entry = (max_char,max_freq)
        sorted_freq_list.append(entry)
        freq_dict[max_char] = 0
        
    return sorted_freq_list

def cosine_similarity(a,u,v): #a = sample dict, u = first dict, v = second dict
     
    def dot(u,v):  #Yeah I know I should be using classes for these o welle
        dot = 0
        for comp in all_chars:
            dot += u[comp]*v[comp]
        return dot
    
    def mag(vec):
        return math.sqrt(dot(vec,vec))
    
    cosU = dot(a,u)/(mag(a)*mag(u))
    U = math.acos(cosU)
    
    cosV = dot(a,v)/(mag(a)*mag(v))
    V = math.acos(cosV)
    
    return U,V

def predict(file):
    neo_train = process('neotrainingtext.txt')
    eng_train = process('engtrainingtext.txt')
    test = process(file)
    
    dist_neo,dist_eng = cosine_similarity(test,neo_train,eng_train)
    print("the neo distance is {}".format(dist_neo))
    print("the eng distance is {}".format(dist_eng))
    
    if dist_neo < dist_eng: #conclude neo
        return 'Neo'
    elif dist_eng < dist_neo: #conclude eng
        return 'English'
    else:
        return 'unknown'

#neo_train = process('neotrainingtext.txt')
#sorted_neo_train = sorted_by_freq(neo_train)
#print(sorted_neo_train)

#eng_train = process('engtrainingtext.txt')
#sorted_eng_train = sorted_by_freq(eng_train)
#print(sorted_eng_train)

prediction = predict('test.txt')
print('The sample text is written in {}'.format(prediction))

