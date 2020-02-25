import os
import shutil as sh


source1 = r'c:/Users/Fahim/Downloads/SYNTHETIK' 
dest1 = r'c:/Users/Fahim/Desktop/desttest'
print("Files will be copied from ")
print(source1 + ' ==> ' + dest1 + " and \n")

#Are you sure? Y/N
#If var = Y it will start the function
#before copying next segment it should do a file size check on both ends and only proceed if both check equal
#do an exit message showing sizes of each segment that was copied


os.listdir(source1)

#Delete the folders recursively on HDD
def wipe(dest):
   shutil.rmtree(dest)

#Copy the folders from source to HDD
def docopy(src, dest):
    for subdir, dirs, files in os.walk(src):
        for file in files:
            print os.path.join(subdir, file)
            shutil.copy2(os.path.join(subdir, file), dest)


#help(sh.copytree)
def transfer(src,dest):
    sh.copytree(src,dest)
