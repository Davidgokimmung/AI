import sys
import os
import xml.etree.ElementTree as elt
from sklearn.metrics import confusion_matrix 
from sklearn.metrics import accuracy_score 

%cd /content/drive/My\ Drive/
!pwd
outerfolder = "Train-corups/"
outerfolder1 = "Test-corpus/"
Dict = {}
    
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
    if word in Dict:
      tag = max(Dict[word], key=Dict[word].get)
      predicted.append(tag)
    else:
      predicted.append('Undefined')
    actual.append(w.attrib['c5'])

out = "Confusion Matrix :" + "\n"
results = confusion_matrix(actual, predicted)
out+=str(results)+"\n"
out+="Accuracy Score : " + str(accuracy_score(actual, predicted))
print(out)
%cd /content

out1 = open("Week6_output.txt",'w');
out1.write(out)
