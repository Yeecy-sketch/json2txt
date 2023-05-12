import json
import os
import pathlib
import glob


inputfilename = input("Enter the file extension of the pictures (case sensitive) (ex: .png .jpg): ")
working_dir = pathlib.Path(__file__).parent.resolve()

findjsonfile = glob.glob1(working_dir, "*.json")[0]

with open(findjsonfile) as jsonfile:
    fileinners = jsonfile.read()
    
parsedfile = json.loads(fileinners)

picturelist = glob.glob1(working_dir, inputfilename)

for i in parsedfile:
    filename = str(i["captioning"].split("data/upload/8/")[1])
    print(filename)
    caption = i["caption"]
    f = open(str(filename).split(".")[0] + ".txt", 'w')
    f.write(caption)
    f.close()

nondeletionlist = []
for i in picturelist:
    a = i.split(".txt")[0]
    a = a + inputfilename
    if os.path.isfile(a):
        nondeletionlist.append(a)

for i in picturelist:
    if i in nondeletionlist:
        print("not removing: " + i)
    else:
        print("removing")
        os.remove(i)
