#! /usr/bin/env python3

"""Uploading the Inventory to Website in the form of JSON.""" 
import os,sys
import json
import requests

dire = 'path/to/file/'
for filename in os.listdir(dire):
    file=os.path.join(dire,filename)
    k=1
    feedback={}
    with open(file) as fh:
        for line in fh:
            b=line[:-1]
            if k==1:
                feedback["name"]=b
            elif k==2:
                a=b.strip(" lbs")
                feedback["weight"]=int(a)
            elif k==3:
                feedback["description"]=b
            k=k+1
    f,e=os.path.splitext(filename)
    outfile=f+'.jpeg'
    feedback["image_name"]=outfile
    print(feedback)
    print('\n')
    url="Destination url"
    res=requests.post(url,json=feedback)
    print(res.status_code)
