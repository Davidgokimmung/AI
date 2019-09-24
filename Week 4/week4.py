import sys
import os
import xml.etree.ElementTree as elt

%cd /content/drive/My\ Drive/
folder = "Train-corups/"

out = ""
Dict = {}
for _,_,files in os.walk(folder):
    for file in files:
        tree = elt.parse(folder+file)
        r = tree.getroot()

        for w in r.iter('w'):
          word = w.text.strip().lower()
          tag = w.attrib['pos']
          if tag in Dict:
            if word in Dict[tag]:
              Dict[tag][word]+=1
            else:
              Dict[tag][word]=1
          else:
            innerDict = {}
            Dict[tag] = innerDict
            innerDict[word]=1
          
%cd /content

for i in Dict:
  count = 0
  for k in Dict[i]:
    count+=Dict[i][k]
  out+=("Probabilities for the tag "+ i +" :\n")
  for j in Dict[i]:
    prob = Dict[i][j]/count
    out+=(j + " : " + "{:.6f}".format(prob) + "\n" )
  out+="\n"

out2 = open("Week4_output.txt",'w');
out2.write(out)
