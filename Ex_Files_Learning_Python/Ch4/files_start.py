#
# Read and write files using the built-in Python file methods
#

def main():
  f1 = open("./textfile.txt","w+") # "+" means that it creates the file if it doesn't already exist
  weekdays = ["mon", "tues", "weds", "thurs", "fri", "sat", "sun"]
  for i,d in enumerate(weekdays):
    f1.write("Day number " + str(i+1) + " of the week is: " + str(d) + "\n")
  f1.close()

  f1 = open("./textfile.txt","r")
  if(f1.mode == "r"):
    f1_contents = f1.readlines()
    for i in f1_contents: print(i)
  print("+++++++++\n" + str(f1.readable()))
  f1.close()


  with open("./textfile.txt","r") as f2: # with statement can be used to automatically close an opened file. It calls the .__exit__ method for a given class. For opened file classes, the [file_obj].__exti__() method includes the [file_obj].close() method
    for line in f2:
      print("=================\n" + str(line))

  with myClassWithExit(666) as c1:
    print(c1.attribute1)
    print(c1.classVar1)

class myClassWithExit():
  classVar1 = 3
  def __init__(self,attribute1=0):
    self.attribute1 = attribute1
  
  def __enter__(self):
    print("\n__enter__ method was called\n")
    return self

  def __exit__(self,exc_t,exc_v,trace):
    print("\n__exit__ method was called.\n")



if __name__ == "__main__":
  main()

# r: Opens the file in read-only mode. Starts reading from the beginning of the file and is the default mode for the open() function.
# rb: Opens the file as read-only in binary format and starts reading from the beginning of the file. While binary format can be used for different purposes, it is usually used when dealing with things like images, videos, etc.
# r+: Opens a file for reading and writing, placing the pointer at the beginning of the file.
# w: Opens in write-only mode. The pointer is placed at the beginning of the file and this will overwrite any existing file with the same name. It will create a new file if one with the same name doesn't exist.
# wb: Opens a write-only file in binary mode.
# w+: Opens a file for writing and reading.
# wb+: Opens a file for writing and reading in binary mode.
# a: Opens a file for appending new information to it. The pointer is placed at the end of the file. A new file is created if one with the same name doesn't exist.
# ab: Opens a file for appending in binary mode.
# a+: Opens a file for both appending and reading.
# ab+: Opens a file for both appending and reading in binary mode.