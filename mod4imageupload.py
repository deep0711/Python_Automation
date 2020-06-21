#!/usr/bin/env python3

"""Uploading only Images previos to Description.On uploading Description,
it fetches the images already available on the server"""

import requests
import os,sys
from PIL import Image

url = "http://localhost/upload/"

dire='path/to/images'

for filename in os.listdir(dire):
  try:
    pa=os.path.join(dire,filename)
    im=Image.open(pa)
    if im.format=='JPEG':
      with open(pa, 'rb') as opened:
        r = requests.post(url, files={'file': opened})
  except:
    pass
