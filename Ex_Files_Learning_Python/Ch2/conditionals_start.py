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

def conditionalStatement(x=0,y=0):
  """
  conditionalStatement(x,y)

  Evaluates two numbers and returns string saying which variable is greater.

  Parameters
  ----------
  x, y : int, optional
    Numbers to be evaluated (the default is 0).
  z : {'first option','4','3','P'}
    Parameter with only a set number of possible values.

  Returns
  -------
  st : str
    Statement saying which variable is larger or smaller.
  
  Raises
  ------
  CustomError1
    A custom error.
  
  See Also
  --------
  conditionalFlow : Same as conditionalStatement except using flow statements.
  func1, func3

  Notes
  -----  
  25/08/20 : Created
  Nicholas Butterly

  Examples
  --------
  >>> print(conditionalFlow(3,4))
  Second number is larger

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
  print(conditionalFlow(3,4))
  print(conditionalStatement(0,4))

if __name__ == "__main__":
  main()

# THERE IS NO 'SWITCH' FLOW CONTROL IN PYTHON, ONLY ELIF STATEMENTS
# For docstring formatting ==> https://numpydoc.readthedocs.io/en/latest/format.html
# For python code formatting ===> https://www.python.org/dev/peps/pep-0008/#documentation-strings