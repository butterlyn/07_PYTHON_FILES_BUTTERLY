#
# Example file for formatting time and date output
#

from datetime import datetime

def main():
  t1 = datetime.now()
  print(t1.strftime("%x === %X === %c === %I === %M === %S ==== %P"))

if __name__ == "__main__":
  main()

  # Using .strftime as a method on datetime instances to create a custom string displaying date
  # %Y 2020
  # %y 20
  # %a Wed
  # %d 02
  # %B October
  # %x, %X, %c