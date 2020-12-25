#
# Example file for working with filesystem shell methods
#
import os
from os import path
import shutil 
from shutil import make_archive
from zipfile import ZipFile

def main():
  # make a duplicate of an existing file
  name = "textfile.txt"
  #os.rename("newfile.txt",name)
  if path.exists(name):
    # get the path to the file in the current directory
    src = path.realpath(name)
    
    # let's make a backup copy by appending "bak" to the name
    dst = src + ".bak"
    
    # copy over the permissions, modification times, and other info
    shutil.copy(src,dst)
    shutil.copystat(src, dst)
    
    # rename the original file
    #os.rename(dst,"newfile.txt")
    
    
    # now put things into a ZIP archive
    root_dir, tail = path.split(src)
    shutil.make_archive("archive","zip", root_dir)

    # more fine-grained control over ZIP files
    with ZipFile("testzip.zip","w") as newzip:
      newzip.write(name)
      newzip.write(dst)
      
if __name__ == "__main__":
  main()
