#
# Example file for working with os.path module
#
import os
from os import path
import datetime
from datetime import date, time, timedelta
import time


def main():
  a = os.path.split(os.path.realpath("./textfile.txt")) # Output is a tuple
  print("\n" + a[1] + "\n")
  print(a[0] + "\n")
  print(
    os.path.exists("./textfile.txt"),
    os.path.isdir("./textfile.txt"),
    os.path.isfile("./textfile.txt"))
  
  
if __name__ == "__main__":
  main()