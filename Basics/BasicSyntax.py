#Math Operators from Highest to Lowest Precedence
"""Operator     Operation   Example     Evaluates to...

    **          Exponent    2 ** 3          8
    %     Modulus/remainder 22 % 8          6
    //      Integer division 22 // 8        2
    /           Division    22 / 8        2.75
    *       Multiplication  3 * 5           15
    -          Subtraction  5 - 2           3
    +           Addition    2 + 2           4

#Common Data Types
    Data type           Examples
    Integers    -2, -1, 0, 1, 2, 3, 4, 5

    Floats  -1.25, -1.0, --0.5, 0.0, 0.5, 1.0, 1.25

    Strings     'a', 'aa', 'aaa', 'Hello!', '11 cats'
"""

# This program says hello and asks for my name.
print("Hello World")
print("What is your name?") #Ask for their name
myName = input()
print("Its good to meet you, " + myName)
print("The lenght of your name is: ")
print(len(myName))
print("What is your age?") #Ask for their age
myAge = input()
print("You will be "+ str(int(myAge) + 1) + " in a year")


#==========================================================================
# Functions
#==========================================================================
def hello():
    print('Howdy!')
print('Howdy!!!')
print('Hello there.')
hello()
hello()
hello()


def hello(name):
    print('Hello ' + name)

hello('Alice')
hello('Bob')