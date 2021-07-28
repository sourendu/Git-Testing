# -*- coding: utf-8 -*-
"""
Created on Tue May  4 17:33:38 2021

@author: shiuli Subhra Ghosh
"""

from bs4 import BeautifulSoup
import pathlib
import re

space_gained = 0
space_input = 0
address=re.compile(r"address|Address|Contact(s)|Contact\sUs|contact\sus")
pincode=re.compile(r"\b\d\d\d(\s)*\d\d\d\b")

for x in range(10):
    filename = str(x) + ".html"
    file = pathlib.Path('input/' + filename)
    if (file.exists()):
        #Read each file
        f = open('input/' + filename, 'r', errors="ignore")
        contents = f.read()   
        
        #Remove html tags
        soup = BeautifulSoup(contents, 'lxml')        
        output = soup.get_text()
        output=output.replace("\n",'')
        
        txt=''
        for i in re.finditer(address,output):
            txt=txt+(output[(i.start()):(i.start()+250)]).strip()
        for i in re.finditer(pincode,output):
            txt=txt+(output[(i.start()-250):(i.start()+20)]).strip()
       
        
        
            
         
               
        
        #Write the output variable contents to output/ folder.
        fw = open('output/' + filename, "w")
        fw.write(txt)
        fw.close()
        f.close()
        
        #Calculate space savings
        space_input = space_input + len(contents)
        space_gained = space_gained + len(contents) - len(txt)        

print("Total Space Gained = " + str(round(space_gained*100/space_input, 2)) + "%") 
       

