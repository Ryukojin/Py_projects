import shutil
# Notes path
# Projects path
# PY path
# WoWclassic path

def f_xfer(src, dst):
    #Check if dest path tree empty or not
    
    #If empty then skip rmtree

    #If not empty then
    shutil.rmtree(dst)
    #Now copy folders
    shutil.copytree(src, dst, symlinks=False, ignore=None)
    #Check files, folders and give count 
    #Also print success

# Notes
f_xfer()
# Projects
f_xfer()
# PY
f_xfer()
# WoWclassic
f_xfer()


# - Dropbox backup
# - Time between copy folders
# 