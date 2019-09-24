import sys
import os
import xml.etree.ElementTree as elt

%cd /content/drive/My\ Drive/
folder = "Train-corups/"
folder1 = "Test-corpus/"

Dict = {}
for _,_,files in os.walk(folder):
    for file in files:
        tree = elt.parse(folder+file)
        r = tree.getroot()

        for w in r.iter('w'):
          word = w.text.strip().lower()
          tag = w.attrib['pos']
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
for _,_,files in os.walk(folder1):
    for file in files:
        tree = elt.parse(folder1+file)
        r = tree.getroot()
        
        for w in r.iter('w'):
          word = w.text.strip().lower()
          if word in Dict:
            tag = max(Dict[word], key=Dict[word].get)
            out+=(word + " : " + tag + "\n")
%cd /content

out1 = open("Week5_output.txt",'w');
out1.write(out)
