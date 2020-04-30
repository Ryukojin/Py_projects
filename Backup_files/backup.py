import os
import shutil as sh


source1 = r'c:/Users/Fahim/Downloads/F1'
dest1 = r'c:/Users/Fahim/Desktop/desttest1/'

source2 = r'c:/Users/Fahim/Downloads/F2'
dest2 = r'c:/Users/Fahim/Desktop/desttest2/'

#Initialise
def prep(src,dst):
    if os.path.isdir(dst) == True:
        print("\nFiles will be copied from ")
        print(src + ' ==> ' + dst)
        ans = input("\nAre you sure to proceed? Type Y/N\n")
    else:
        print("\nWARNING: Destination folder '" + dst + "' does not exist!")
        ans = 'N'
    return ans

#Transfer
def xfer(srce, destn):
    sh.rmtree(destn)
    sh.copytree(srce, destn)

#Print result
def output(dst,src): 
    if os.listdir(dst) == os.listdir(src):
        print("\nAll files successfully copied from " + src + ' ==> ' + dst )
    else:
        print("\nFile transfer unsuccessful!")

# Main body
def main(src,dst):
    ans = prep(src,dst)
    if ans == "Y":
        xfer(src,dst)
        output(src,dst)
        print("====================================================================================================================")
    else:
        print("The segment will not be copied... \nProceeding to next segment...\n")
        print("====================================================================================================================")

if __name__ == "__main__":
    main(source1,dest1)
    main(source2,dest2)








