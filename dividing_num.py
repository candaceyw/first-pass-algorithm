# we'll say that a positive int divides itself if every digit in the number divides into the number evenly.
# So for examples 128 divides itself since 1, 2, and 8 all divide into 128 evenly.
# And we'll say that 0 does not divide into anything evenly, so no number with a 0 digit divides itself.
# Write a function to determine if a number divides itself.


def divides_self(num):

    # make an original copy of Num
    new_num = num
    # Loop over each digit in num (it's a while loop):
    while new_num >= 10:
    #   get the right most digit of num using num % 10
        new_num % 10
    #   if the digit is 0, return False
        if new_num == 0:
            return False
    #   take that digit, and get remainder of original num / digit

    #   if remainder is NOT 0, return False

    #   remove the last digit from the number using // 10 (integer division)
    # return True
    pass


print(divides_self(128))  # True
print(divides_self(12))  # True
print(divides_self(120))  # False

# UPER
# INPUTS: A number, positive integer, how large?, 0 case? returns false, can we get bad data (not a number)?
# OUTPUT: what is the type of return? return boolean
# PLAN: Pseudocode, to divide evenly - Modulo operator % - gives the remainder of a/b
# get every number - some kind of loop
# how to get a digit?
    # convert to string/List?
    # get right most digit using % 10