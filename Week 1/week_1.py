import sys
import os
import xml.etree.ElementTree as elt

%cd /content/drive/My\ Drive/
!pwd
folder = "Train-corups/"
file = os.walk(folder)

out = ""
for _,_,files in os.walk(folder):
    print(files)
    for file in files:
        print(file)
        t = elt.parse(folder+file)
        r = tree.getroot()

        for w in r.iter('w'):
          out+=(w.text.strip().lower() + "_" + w.attrib['pos']+"\n")
%cd /content
out1 = open("Week1_output.txt", "w")
out1.write(out)
