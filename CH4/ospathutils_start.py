#
# Example file for working with os.path module
#
import os
from os import path
import datetime
from datetime import date, time, timedelta
import time

def main():
  name = "textfile.txt"
  # Print the name of the OS
  print(os.name)
  
  # Check for item existence and type
  print("Item exist: "+str(path.exists(name)))
  print("Item is a file: "+str(path.isfile(name)))
  print ("Item is a directory: "+str(path.isdir(name)))
  # Work with file paths
  print("Item path: "+str(path.realpath(name)))
  print("Item path and name: "+str(path.split(path.realpath(name))))
  
  # Get the modification time
  t1 = time.ctime(path.getmtime(name))
  print(t1)
  t2 = datetime.datetime.fromtimestamp(path.getmtime(name))
  print(t2)
  
  
  
  # Calculate how long ago the item was modified
  td= datetime.datetime.now() - datetime.datetime.fromtimestamp(path.getmtime("textfile.txt"))
  
  print ("It had been "+ str(td)+ " since the file was modified.")
  print("Or, "+str(td.total_seconds())+ " seconds")
if __name__ == "__main__":
  main()
