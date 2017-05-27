import os
from os import listdir
from os.path import isfile, join

onlyfiles = [f for f in listdir("/Users/Pedro_Torres/Downloads/Lab/") if isfile(join("/Users/Pedro_Torres/Downloads/Lab/", f))]
"""the above converts my folder files into a list of files"""

def Answer(folder):
    '''will open the answer key which is currently in .py format and then save the test code or key
    so i can add it to the bottom of the homeworks in the next function'''
    for answer in onlyfiles[-1:]: #here i added a 'z' to the begining of the answer key so that i can easilty splice that out need to find a better alternative
        key=open(folder+answer)# opening the answer key in which ever folder it is kept in
        key=key.read()
        return key
    

for files in onlyfiles[1:-1]:
    """takes your list of files and calls each file up then opens it so you can add the test code/answer key from above to the bottom"""
    HWanswer= Answer("/Users/Pedro_Torres/Downloads/Lab/")#calling function above I can always change the directory where the answer key is being kept
    x=open("/Users/Pedro_Torres/Downloads/Lab/"+files,"rw")# here i am opening each file so i have the directory and add the file name then open it
    x=x.read()
    o=open("answers"+files,"w")# i will write a new file which contains the students labs plus the key added to the bottom
    combined=x+HWanswer
    o.write(combined)
    o.close()

for myfile in [i for i in os.listdir("/Users/Pedro_Torres/Downloads/Answers") if "DictionariesV2.py" in i]:#this will change depending on hw
    '''myfile calls up each of the students combined lab and test script specifically if the lab ends with Function.py THIS WILL HAVE TO CHANGE WITH EACH LAB. This part ignores anyother python files that are in the same folder.
    because within this folder I have this python script i am using'''
    os.system("python /Users/Pedro_Torres/Downloads/Answers/"+myfile+" > finalanswers/"+myfile+".txt")
    myfile= myfile.split('.')
    print myfile[0]
