#1) square star pattern

# def square(n):
    
#     for i in range(n):
#         for j in range(n):
#             print("*",end=" ")
#         print()
# square([5])



#2) right Traiangale pattern

# def rightTrainangele(n):
    
#     for i in range(1,n+1):
#         for j in range(i):
#             print("*",end=" ")
#         print()
# rightTrainangele(5)


# inverted Triangle

# def invert(n):
    
#     for i in range(n,0,-1):
#         for j in range(i):
#             print("*",end=" ")
#         print()
# invert(5)



#4)pyramid pattern

# n = 5

# for i in range(1,n+1):
#     print(" " * (n-i),end="")
#     for i in range(i):
#         print("* ",end="")
    
    

  
#5) reverse String 


# def my_func(n):
    
#     rev = ""
    
#     for i in n:
#         rev = i + rev
#     return rev
# print(my_func("hello"))  
    

#6) check palindrom

# def palindrom(n):
    
#     rev = ""
    
#     for i in n:
        
#         rev = i + rev
        
#     if rev == n:
#         print("True")
#     else:
#         print("false")
# palindrom("noon")   


#7) Write a program to print the Fibonacci series up to n terms.

# def Fibonacci(n):
#     a,b=0,1
    
#     for i in range(n):
#         print(a,end=" ")
        
#         temp = a + b
#         a = b
#         b = temp
# Fibonacci(10)
        
        

        
        


    
            


