#
# Example file for working with conditional statements
#

def conditionalFlow(x, y):
  """
  Evaluates two numbers and returns string saying which variable is greater

  EXAMPLE:
  print(conditionalFlow(3,4))

  PARAMETERS:
    x,y:  Numbers to be evaluated

  RETURNS:
    st:   Statement saying which variable is larger or smaller
  
  25/08/20: Created

  Nicholas Butterly
  """
  result = 0 # set default funciton output
  
  #----------------- Input Error Handling ---------------------
  #----------------------- Function ---------------------------
  if(x < y):
    st = "Second number is larger"
  elif(y < x):
    st = "first number is larger"
  elif(y == x):
    st = "Numbers are equal"
  
  result = st
  #----------------- Output Error Handling --------------------
  #------------------------ Output ----------------------------
  return result

def conditionalStatement(x,y):
  """
  Evaluates two numbers and returns string saying which variable is greater

  EXAMPLE:
  print(conditionalFlow(3,4))

  PARAMETERS:
    x,y:  Numbers to be evaluated

  RETURNS:
    st:   Statement saying which variable is larger or smaller
  
  25/08/20: Created

  Nicholas Butterly
  """
  result = 0 # set default funciton output
  
  #----------------- Input Error Handling ---------------------
  #----------------------- Function ---------------------------
  st = "Second number is larger" if(x<y) else "Numbers are equal?"
  
  result = st
  #----------------- Output Error Handling --------------------
  #------------------------ Output ----------------------------
  return result

def main():
  print(conditionalFlow(44,4))
  print(conditionalStatement(0,4))

if __name__ == "__main__":
  main()

# THERE IS NO 'SWITCH' FLOW CONTROL IN PYTHON, ONLY ELIF STATEMENTS