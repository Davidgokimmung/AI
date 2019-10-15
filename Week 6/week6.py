import sys
import os
import xml.etree.ElementTree as elt
import pandas as pd
import seaborn as sn
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score

%cd /content/drive/My\ Drive/
!pwd
outerfolder = "Train-corups/"
outerfolder1 = "Test-corpus/"
Dict = {}
tagset = set()
taglist = []
shpfiles = []
for dirpath, subdirs, files in os.walk(outerfolder):
    for x in files:
        if x.endswith(".xml"):
            shpfiles.append(os.path.join(dirpath, x))
for file in shpfiles:
  tree = elt.parse(file)
  r = tree.getroot()

  for w in r.iter('w'):
    word = w.text.strip().lower()
    tag = w.attrib['c5']
    if tag not in tagset:
      tagset.add(tag)
      taglist.append(tag)
      
    if word in Dict:
      if tag in Dict[word]:
        Dict[word][tag]+=1
      else:
        Dict[word][tag]=1
    else:
      innerDict = {}
      Dict[word] = innerDict
      innerDict[tag]=1

actual = []
predicted = []
shpfiles1 = []
for dirpath, subdirs, files in os.walk(outerfolder1):
    for x in files:
        if x.endswith(".xml"):
            shpfiles1.append(os.path.join(dirpath, x))
for file in shpfiles1:
  tree = elt.parse(file)
  r = tree.getroot()

  for w in r.iter('w'):
    word = w.text.strip().lower()
    tag1 = w.attrib['c5']
    if tag1 not in tagset:
      tagset.add(tag1)
      taglist.append(tag1)
    if word in Dict:
      tag = max(Dict[word], key=Dict[word].get)
      predicted.append(tag)
    else:
      predicted.append('UNDEFINED')
    actual.append(w.attrib['c5'])

taglist.append("UNDEFINED")
taglist.sort()
out = "Confusion Matrix :" + "\n"
results = confusion_matrix(actual, predicted)
print("Confusion matrix:\n%s" % results)
out+=str(results)+"\n"
print("Accuracy Score: ",accuracy_score(actual, predicted))

%cd /content

out1 = open("Week6_output.txt",'w');
out1.write(out)

df_cm = pd.DataFrame(results, index=taglist, columns=taglist)
plt.figure(figsize = (20,20))
sn.heatmap(df_cm, cmap='gray_r')
plt.show()
