import sys
import os
import xml.etree.ElementTree as elt

%cd /content/drive/My\ Drive/
!pwd
outerfolder = "Train-corups/"
out = ""
    
shpfiles = []
for dirpath, subdirs, files in os.walk(outerfolder):
    for x in files:
        if x.endswith(".xml"):
            shpfiles.append(os.path.join(dirpath, x))
for file in shpfiles:
  tree = elt.parse(file)
  r = tree.getroot()

  for w in r.iter('w'):
    out+=(w.text.strip().lower() + "_" + w.attrib['c5']+"\n")
  
%cd /content

str_list=out.split()
freq = {}
for item in str_list: 
  if item in freq: 
    freq[item] += 1
  else: 
    freq[item] = 1
out2=""
for i in freq:
        out2+= ("Frequency of " + i + " is : "+ str(freq[i]) + "\n")
out3= open("Week2_output.txt","w")
out3.write(out2)
