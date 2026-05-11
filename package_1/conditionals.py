# if else elif
# 


# name = input("Enter your full name \t") # "  lara  "

# if name.strip().lower().startswith("sa"):
#     print(f"{name} is starting with 'sa'")

#     if name.strip().lower().endswith("r"):
#         print(f"{name} endswith r")
#     elif name.strip().lower().endswith("v"):
#         print(f"{name} endswith v")
#         if name.strip().lower().endswith("r"):
#             print(f"{name} endswith r")
#         elif name.strip().lower().endswith("v"):
#             print(f"{name} endswith v")
    
# elif name.strip().lower().startswith("su"):
#     print(f"{name} is starting with 'su'")
#     if name.strip().lower().endswith("r"):
#         print(f"{name} endswith r")
#     elif name.strip().lower().endswith("v"):
#         print(f"{name} endswith v")
# elif name.strip().lower().startswith("aa"):
#     print(f"{name} is starting with 'aa'")
#     if name.strip().lower().endswith("r"):
#         print(f"{name} endswith r")
#     elif name.strip().lower().endswith("v"):
#         print(f"{name} endswith v")
# elif name.strip().lower().startswith("la"):
#     print(f"{name} is starting with 'la'")
#     if name.strip().lower().endswith("i"):
#         print(f"{name} endswith i")
#     elif name.strip().lower().endswith("a"):
#         print(f"{name} endswith a")
# else:
#     print(f"{name} is not what we searched for!")
#     if name.strip().lower().endswith("r"):
#         print(f"{name} endswith r")
#     elif name.strip().lower().endswith("v"):
#         print(f"{name} endswith v")


# WAP to
# Ask for username from terminal for 5 times add those names in list
# Display if these name contains some chars like 'sa', 'as' and so on 


# for loop -> is used to iterate over list / iterables

# while condition

# counter = 1

# while counter < 50:
#     counter += 1 # counter = counter + 1

#     if counter % 2 == 0 : # This ensures even number 
#         continue

#     print(f"Looping over {counter}")

#     if counter == 10:
#         break


# for i in range(50):
#     if i % 2 != 0:
#         continue
#     print(f"Looping over {i}")

#     if i == 20:
#         break


# full_name = "Ram Bahadur Thapa Badal"
# full_name = ('Sita', 'Rita', 'Laxmi', 'Sunita', 'Prativa') # tuple

# tuple, set, list

# full_name = {
#     'a':'First',
#     'b' : 'Name',
#     'c' : 'Is'
# }
# for i in full_name:
#     print(i)
#     if i == 'b':
#         break
# else:
#     pass
#     # print("Finally ok")


# WAP to
# Ask for full_name from terminal, 
# if name startswith 'a' and endswith 'n' break therein 
# else keep on scanning the name


# and , or


# if stm1 and stm2
# if stm1 or stm2



while True:
    full_name = input("Enter Your Full Name \t")
    full_name = full_name.strip().lower()

    if full_name.startswith('a') or full_name.endswith('n'):
        print("The condition is satisfied!")
        break
    else:
        print("Scanning for next \n")

