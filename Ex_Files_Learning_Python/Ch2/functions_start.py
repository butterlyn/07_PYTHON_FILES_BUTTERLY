#
# Example file for working with functions
#

# define a basic function
def func1():
    print("This is the output of func1")

# function that takes arguments with default value and returns a value
def multiplynum(x, y=1):
    """
    Prints equation and result of multiplying two input arguments.
    """
    result = 0 # set default value of function output
    print(x,"*",y,"=",x*y)
    result = x*y
    return result

# function with variable number of arguments
def multiply_many(*args):
    """
    Multiply several input arguments together
    """
    result = 1
    for x in args: # in ==> checks to see if a value is in a list/tuple/array and returns boolean
        result = result*x
    return result

def main():
    func1()
    print(func1()) # returns value 'None', equivalent to NaN in MATLAB
    print(func1) # Without arguements, function name returns address of pointer to the function (variable type 'function')
    print(multiplynum(3,7))
    print(multiplynum(2))
    print(multiplynum( # function arguments can be passed to function by giving names in any order
        y=55,
        x=8))
    print(multiply_many(2,2,2,2))

if __name__ == "__main__":
    main()