#!/usr/bin/env python3

"""Converting the Image Property.
1.Converting the image to RGB mode
2.Resizing it to 600*400 pixel
3.Changing the format to JPEG"""

import os,sys
from PIL import Image

dire='path/for/reading_files'
sav='path/for/saving_file'

for filename in os.listdir(dire):
        try:
                im=Image.open(os.path.join(dire,filename))
                if im.mode!='RGB':
                        im=im.convert('RGB')
                new_im2=im.resize((600,400))
                f,e=os.path.splitext(filename)
                outfile=f+'.jpeg'
                new_im2.save(sav+outfile)
        except:
                pass
