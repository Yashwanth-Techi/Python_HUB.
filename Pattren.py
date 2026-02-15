# 1. Right-Angle Triangle
# n = 5
# for i in range(1, n+1):
#     print("*" * i)

# for i in range(1, 6):
#     print("*" * i)



# 2. Inverted Right Triangle


# n = int(input("enter the n:"))

# for i in range(n,0,-1):
#     print("*" * i)


# 3. Pyramid Pattern
# n = int(input("Enter number of rows: "))

# for i in range(n):
#     spaces = " " * (n - i - 1)
#     stars = "*" * (2 * i + 1)
#     print(spaces + stars)

##Q4) Diamond Pattern 

# n = int(input("Enter number of rows: "))

# # Upper part
# for i in range(n):
#     print(" " * (n - i - 1) + "*" * (2 * i + 1))

# # Lower part
# for i in range(n - 2, -1, -1):
#     print(" " * (n - i - 1) + "*" * (2 * i + 1))

