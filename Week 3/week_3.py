import sys
import os
import xml.etree.ElementTree as elt
from collections import Counter 
from matplotlib import pyplot as plt 

%cd /content/drive/My\ Drive/
!pwd
outerfolder = "Train-corups/"
out = ""
out1 = ""
    
shpfiles = []
for dirpath, subdirs, files in os.walk(outerfolder):
    for x in files:
        if x.endswith(".xml"):
            shpfiles.append(os.path.join(dirpath, x))
for file in shpfiles:
  tree = elt.parse(file)
  r = tree.getroot()

  for w in r.iter('w'):
    out+=(w.text.strip().lower() +"\n")
    out1+=(w.attrib['c5']+"\n") 
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
out2+=("Top 10 frequently used Words"+"\n")
for i in high:
  print(str(i[0]) + " : " + str(i[1]))
  out2+=(str(i[0]) + " : " + str(i[1])+"\n")

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

out2+=("\n"+"Top 10 frequently used Tags"+"\n")

for i in high1:
  print(str(i[0]) + " : " + str(i[1]))
  out2+=(str(i[0]) + " : " + str(i[1])+"\n")

out3 = open("Week3_output.txt",'w');
out3.write(out2)

#Analysis
x = []
y = []

for i in range(0,10):
	x.append(high[i][0])
	y.append(high[i][1])

plt.bar(x,y)
plt.show()

x = []
y = []

for i in range(0,10):
	x.append(high1[i][0])
	y.append(high1[i][1])

plt.bar(x,y)
plt.show()
