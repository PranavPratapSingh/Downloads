import glob
import shutil
import os
#taking inputs
extension = raw_input("Enter the Extensions you want to process, separated by space: ")
ext = extension.split(" ")
direc = raw_input("Enter Absolute Path of Target Directory, or leave Blank for Downloads: ")
if direc == "":
    uN = raw_input("Enter Username as in Windows: ")
    direc = "C:/Users/" + uN + "/Downloads/"
else:
    direc = direc + "/"
os.chdir(direc)
#making folders and moving files
for E in ext:
    if not os.path.exists(E):
        os.makedirs(E)
    for f in glob.glob("*."+E):
        shutil.move(f, E+"/"+f)
#end of program
print "Operation Successful"
