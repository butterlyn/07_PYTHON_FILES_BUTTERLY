#
# Example file for working with loops
#

def main():
  x = 0
  while(x<5):
    print(x)
    x = x+1
  print()  
  for i in range(4):
    print(i)
  print()
  for i in [1,4,"hi"]:
    print(i)
  print()
  for i,d in enumerate([1,4,"hi"],11):
    print(i,d)
  print()
  for i in range(1,14,2):
    print(i)

if __name__ == "__main__":
  main()


# x = x++ is NOT VALID