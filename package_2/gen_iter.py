# import time

# def print_text(text:str):
#     for i in range(3):
#         yield text + str(i)
#         # print(text)

# generated_value = print_text("Hello, World!")

# # generated_value = iter([1,2,3,4,5,6,7,8,9,10])

# for i in generated_value:
#     print("Countdown starts...")
#     print("Yielded Value >> ",i)
#     time.sleep(3)
#     print("3 seconds passed...")



# Fibonacci Series

# Output: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ... 

def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a = b
        b = a+b


fib_gen = fibonacci(12)

# print([i for i in fib_gen])
print(list(fib_gen))

# Generate even numbers from 0 to n