#! /usr/bin/env python3
"""Processing a Fruit Inventory!!
1.Reading the images and description from File
2.Creating the report PDF
3.Creating the email with PDF as attachment!!"""

import os,sys,datetime,reports,emails

"""Step 1"""
dire = 'path/to/files'

fruits=[]
for filename in os.listdir(dire):
    file=os.path.join(dire,filename)
    k=1
    
    with open(file) as fh:
        for line in fh:
            b=line[:-1]
            if k==1:
                fruits.append("name: "+b)
            elif k==2:
                fruits.append("weight: "+b)
            k=k+1
s1=fruits[0]
s2=fruits[1]
s3=fruits[2]
s4=fruits[3]
s5=fruits[4]
s6=fruits[5]
s7=fruits[6]
s8=fruits[7]
s9=fruits[8]
s10=fruits[9]
s11=fruits[10]
s12=fruits[11]
s13=fruits[12]
s14=fruits[13]
s15=fruits[14]
s16=fruits[15]
s17=fruits[16]
s18=fruits[17]
s19=fruits[18]
s20=fruits[19]

x = datetime.datetime.now()
title="Processed Update on"+str(x.strftime("%B"))+str(x.strftime("%d"))+','+str(x.year)

"""Step 2"""
reports.generate("/path/to/destination/result.pdf", title, s1,s2,s3,s4,s5,s6,s7,s8,s9,s10,s11,s12,s13,s14,s15,s16,s17,s18,s19,s20)

"""Step 3"""
sender = "sender@example.com"
receiver = "receiver@example.com"
subject = "Upload Completed - Online Fruit Store"
body ="All fruits are uploaded to our website successfully. A detailed list is attached to this email."

message = emails.generate(sender, receiver, subject, body, "/tmp/processed.pdf")
emails.send(message)
