import sys
import os
import xml.etree.ElementTree as elt
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

out = ""
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
      out+=(word + " : " + tag + "\n")
    else:
      out+=(word + " : Undefined\n")

%cd /content

out1 = open("Week5_output.txt",'w');
out1.write(out)
