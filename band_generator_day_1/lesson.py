#Day 1 Lesson 1 
"""
Instructions:
    Write a program in main.py that prints the same notes from the previous lesson using what you have learnt about the Python print function.

    Warning: The output in your program should match the example output shown below exactly, character for character, even spaces and symbols should be identical, otherwise the tests won't pass.

    Example Output
    After you have written your code, you should run your program and it should print the following:
    Day 1 - Python Print Function
    The function is declared like this:
    print('what to print')"""

print('Day 1 - Python Print Function')
print('The function is declared like this:')
print("print('what to print')") 

#Day 1 Lesson 2 
"""Instructions
    Look at the code in the code editor on the right. There are errors in all of the lines of code. Fix the code so that it runs without errors.

    Warning: The output in your program should match the example output shown below exactly, character for character, even spaces and symbols should be identical, otherwise the tests won't pass.

    Example Output
    When you run your program, it should print the following:

    Day 1 - String Manipulation
    String Concatenation is done with the "+" sign.
    e.g. print("Hello " + "world")
    New lines can be created with a backslash and n.""" 
    #Fix the code below 👇
    # print(Day 1 - String Manipulation")
    # print("String Concatenation is done with the "+" sign.")
    #   print('e.g. print("Hello " + "world")')
    # print(("New lines can be created with a backslash and n.")

print("Day 1 - String Manipulation")
print('String Concatenation is done with the "+" sign.')
print('e.g. print("Hello " + "world")')
print("New lines can be created with a backslash and n.")


#Day 1 Lesson 3 
"""Instructions
    Write a program that prints the number of characters in a user's name. You might need to Google for a function that calculates the length of a string.

    e.g.

    https://www.google.com/search?q=how+to+get+the+length+of+a+string+in+python+stack+overflow

    Warning. Your program should work for different inputs. e.g. any name that you input.

"""

name = input('What is your name? ')
print(len(name))  

#Day 1 Lesson 4 
"""Instructions
    Write a program that switches the values stored in the variables a and b.

    Warning. Do not change the code on lines 1-4 and 12-18. Your program should work for different inputs. e.g. any value of a and b.

    Example Input
    a: 3
    b: 5
    Example Output
    a: 5
    b: 3
    e.g. When you hit run, this is what should happen:""" 

a = input("a: ")
b = input("b: ")
a,b = b,a 
print(f"a: {a}")
print(f"b: {b}") 

#Day 1 - Project BAND GENERATOR 
#1 Create A Greeting for your program 
#2 Ask the User for a City they grew up in
#3 Ask the User for a name of a pet 
#4 Combine the name of their pet and city and then show them the band name 
#5 Make sure the cursor shows on a new li