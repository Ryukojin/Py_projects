import os
import shutil as sh


source1 = r'c:/Users/Fahim/Downloads/Sin'
dest1 = r'c:/Users/Fahim/Desktop/desttest/'

source2 = 'C:\Users\Fahim\Documents\Projects'
dest2 = 

#FUNCTIONS
#Initialise
def prep(src,dst):
    global ans
    print("Files will be copied from ")
    print(src + ' ==> ' + dst)
    print("\nAre you sure? Type Y/N")
    ans = input()

#Transfer
def xfer(srce, destn):
    sh.rmtree(destn)
    sh.copytree(srce, destn)

#Print result
def output(dst,src): 
    if os.listdir(dst) == os.listdir(src):
        print("\nAll files successfully copied from " + src + ' ==> ' + dst )
    else:
        print("\nFile transfer Unsuccessful!")

#Segment 1
prep(source1,dest1)
if ans == "Y":
    xfer(source1,dest1)
    output(source1,dest1)
else:
    print("\nYou have decided not to copy this segment... \nProceeding to next segment...")

