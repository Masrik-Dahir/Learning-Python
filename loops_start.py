#
# Example file for working with loops
#

def main():
  x = 0

  # define a while loop
  while (x<5):
   print(x)
   x=x+1

  # define a for loop
  for x in range (5,10):
   print(x)

  # use a for loop over a collection
  days = ["suck","my","dick","!"]
  for i in days:
    print(i)
  
  # use the break and continue statements
  for x in range (5,10):
    #if(x==7): break
    if (x%2==0): continue
    print(x)
  

  #using the enumerate() function to get index 
  months = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sept","Oct","Nov","Dec"]
  for i,m in enumerate(months):
      print(i,m)
  
if __name__ == "__main__":
  main()
