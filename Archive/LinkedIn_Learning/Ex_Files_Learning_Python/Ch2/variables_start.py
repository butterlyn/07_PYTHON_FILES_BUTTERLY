# 
# Example file for variables
#

str_1 = "Global variable" # Global variable does not need to be placed above function where it is called
print(str_1)
del str_1 # del ==> deletes a defined variable

def main():
    str_1 = "Local Variable"
    num_1 = 3
    print(str_1)
    print(num_1)

    # str() ==> redefine variabletype to string so it can be concatenated with other strings
    print(str_1 + " " + str(num_1))
    print(str_1, num_1) # Use commas if variables are of a different type

def firstFunction(): # Function
    global str_1 # global ==> declaring that a global variable can be edited within the scope of a function
    str_1 = "Change global variable in a function by declaring it as 'global' at the top of the function"
    print(str_1)

if __name__ == "__main__":
    main()
    firstFunction()