#
# Read and write files using the built-in Python file methods
#

def main():  
  # Open a file for writing and create it if it doesn't exist
  #f = open("textfile.txt","w+")
  
  # Open the file for appending text to the end
  f = open("textfile.txt","a")
  f2 = open("textfile.txt","r")

  # write some lines of data to the file
  for i in  range (10):
        f.write("This is line "+str(i)+"\r\n")
  
  # close the file when done
  f.close()
  
  # Open the file back up and read the contents
  if f2.mode == 'r':
    fl = f2.readlines()
    for i in fl:
      print(i)
  #contents = f2.read()
  #print(contents)

    
if __name__ == "__main__":
  main()
