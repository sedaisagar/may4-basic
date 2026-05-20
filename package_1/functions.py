# Input , Output
# Y -> YES, X -> No

# X , X
# Y , X
# X , Y
# Y , Y

# # No input , no output
# def make_something():
#     print("Making something!")

# # Yes input , no output
# def make_something(text):
#     print(text)

# No input , yes output
# def make_something():
#     text="Making something!"
#     print("Inner >> ",text)
#     return text

# yes input , yes output
# def make_something(text:str):
#     print("Inner >> ",text)
#     return text + " is made!"

# return_value = make_something()
# return_value = make_something("Making something!")
# return_value = make_something()
# return_value = make_something("Making something!")

# print("The returned value is \t >>>> ", return_value)




# def do_something(a,b,c):
#     return a,b,c

# v1,v2,v3 = do_something(1,2,3)


# def do_something(a, *args, **kwargs, f=1):
#     # breakpoint()
#     return tuple(kwargs.values())[:3]


# v1,v2,v3 = do_something(e=7,d=8,b=9,c=100,a=6,)

# # kwargs

# print(v1,v2,v3)

# Write a program

# Suppose you have a list of numbers
# numbers = [1,2,3,4,5, 20,15,17,13,9,7,11]
# Write a function that takes a list of numbers and returns the sum of the even numbers in the list.
# use args, kwargs to implement the function

# Anonymous functions (lambda)

# func = lambda x,y,z,a,b,c : x+y+z+a+b+c

# son= func(1,2,3,4,5,6)

# print(son)


# Nested Functions


# def outer_function(text):
    
#     def inner_function_1():
#         print("Inner function 1 is called!")
#         # return text.upper()

#         def inner_function_11():
#             print("Inner function 11 is called!")
#         return inner_function_11()
    
#     def inner_function_2():
#         print("Inner function 2 is called!")
#         return text.upper()

#         def inner_function_21():
#             print("Inner function 21 is called!")
    
#     return inner_function_1()

# func = outer_function("Hello World!")
# print(func)


# Decorators

def prettier(func):

    def inner(text, *args, **kwargs):
        if text:
            text = "------- " + text + " -------"
            return func(text)
        else:
            print("No text provided!")

    return inner

x = "??????????????? End Statement"

@prettier # this is decorator decorating the function pretty_print
def pretty_print(text):
    global x
    x = "<<<<<<<<< End Statement"

    print(text + x)

# -----------I am beautiful / handsome!----------------
pretty_print("I am sagar",1,2,3,4,5,6,7,"asdfsda","asdfasdf")


print(x)



# Write a decorator function that takes list of numbers,
# Separates the even and odd numbers into two different lists and then returns both lists to the decorated func.
# So the decorated function should take two lists as input and return the sum of the even numbers and the sum of the odd numbers.




def prettier(func):

    def inner(list_of_numbers, *args, **kwargs):
        if list_of_numbers:
            even_numbers = [num for num in list_of_numbers if num % 2 == 0]
            odd_numbers = [num for num in list_of_numbers if num % 2 != 0]
            return func(even_numbers, odd_numbers)
        else:
            print("No numbers provided!")

    return inner


@prettier # this is decorator decorating the function pretty_print
def sum_finder(even_numbers, odd_numbers):
    sum_even = sum(even_numbers)
    sum_odd = sum(odd_numbers)
    return sum_even, sum_odd

# numbers = [1,2,3,4,5, 20,15,17,13,9,7,11]
# sum_even, sum_odd = sum_finder(numbers)

# print("Sum of even numbers: ", sum_even)
# print("Sum of odd numbers: ", sum_odd)


# Task 
def changecase(func):

    def inner(text):
        original = text
        upper = text.upper()
        lower = text.lower()
        return func(original, lower, upper)
    
    return inner

@changecase
def print_text(original, lower, upper):
    print("text is executing")
    return original, lower, upper

original, lower, upper = print_text("I want to learn Python")

print("--- print text ---")
print(f"Original: {original}")
print(f"Lowered: {lower}")
print(f"Uppered: {upper}")











