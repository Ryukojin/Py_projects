import os
import re
from glob import glob

all_files = []
for root, folder, files in os.walk(path):
    names =  glob(os.path.join(root,'*.mp3'))
    for f in names:
        all_files.append(f)

fixed = []
for i in all_files:
    fixed.append(re.search('^\-[A-z]\.\w\w\w',i)) 

len(all_files)

phrase = 'C:\\Users\\Fahim\\Desktop\\glo\\1997 - Wu-Tang Clan - Wu-Tang Forever\\CD 2\\18 Wu-Tang Clan - Projects International Remix.mp3'
x = re.findall("\s\-\s[A-z]*\s[A-z]*\s[A-z]*\.\w\w\w$",phrase)