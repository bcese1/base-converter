"""
    Name: Benjamin Cesero
    Task: Assignment 2
    Class: CSCI3351
    Description: Takes 1 base and a dynamic amount of parameters to convert it to the proper base type.
"""

from functools import reduce  # import reduce library

Poss_Val = "0123456789ABCDEF"  # Needed for conversion


def convert(b, *args):  # Base converter
    if 2 <= b <= 16 and args != float:  # Checks if base is between 2 and 16, and the args are not decimal values
        output = ['base=', str(b)]  # Creates output list with the base already included
        output[0:2] = [reduce(lambda i, j: i + j, output[0:2])] # joins the 0th and 1st elements
        for arg in args:  # unpacks args into arg
            ar = ""  # creates a var with type string
            while arg > 0 and ar != "NA":  # checks if arg is greater than 0, and res is not equal to NA
                if isinstance(arg, int):  # checks if arg is a type int
                    ar += Poss_Val[arg % b]  # uses BS string to do arg mod base
                    arg //= b  # arg floor division on b then stores back in arg
                else:
                    ar = "NA"  # set res to string value NA
                    output.append(ar[::] or "0")  # put "NA" in the output list
            output.append(ar[::-1] or "0")  # every while loop break it appends the list
        if "NA" in output:  # checks if "NA" is in the list
            output.remove("AN")  # removes "AN" from the list if it appears
        return output  # returns the list
    else:
        output = ['Wrong Base']  # if the base is not between 2 and 16 create a list with 'Wrong Base'
        return output  # return output


print(convert(2, 5, 10, 3))
print(convert(8, 5, 10))
print(convert(17, 5, 10))
print(convert(16, 5, 40, 3.5))
