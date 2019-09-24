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
out1 = open("Week1_output.txt", "w")
out1.write(out)
