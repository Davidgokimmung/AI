import sys
import os
import xml.etree.ElementTree as elt
from collections import Counter 

%cd /content/drive/My\ Drive/
folder = "Train-corups/"

out = ""
out1 = ""
for _,_,files in os.walk(folder):
    for file in files:
        tree = elt.parse(folder+file)
        r = tree.getroot()

        for w in r.iter('w'):
          out+=(w.text.strip().lower() +"\n")
          out1+=(w.attrib['pos']+"\n")
%cd /content

#Top 10 frequently used Words
str_list=out.split()
freq = {}
for item in str_list: 
  if item in freq: 
    freq[item] += 1
  else: 
    freq[item] = 1

k = Counter(freq) 
high = k.most_common(10)  

out2 = ""

for i in high:
  out2+=(str(i[0]) + " : " + str(i[1])+"\n")

out3 = open("Week2_output1.txt",'w');
out3.write(out2)

#Top 10 frequently used Tags
str_list1=out1.split()
freq1 = {}
for item in str_list1: 
  if item in freq1: 
    freq1[item] += 1
  else: 
    freq1[item] = 1

k1 = Counter(freq1) 
high1 = k1.most_common(10)  

out4 = ""

for i in high1:
  out4+=(str(i[0]) + " : " + str(i[1])+"\n")

out5 = open("Week2_output2.txt",'w');
out5.write(out4)
