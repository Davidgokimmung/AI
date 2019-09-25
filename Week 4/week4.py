import sys
import os
import xml.etree.ElementTree as elt

%cd /content/drive/My\ Drive/
!pwd
outerfolder = "Train-corups/"
out = ""
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
%cd /content

for i in Dict:
  count = 0
  for k in Dict[i]:
    count+=Dict[i][k]
  out+=("Probabilities for the word "+ i +" :\n")
  for j in Dict[i]:
    prob = Dict[i][j]/count
    out+=(j + " : " + "{:.6f}".format(prob) + "\n" )
  out+="\n"

out2 = open("Week4_output.txt",'w');
out2.write(out)
