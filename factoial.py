def factrorial(x):
    '''this is a recursive function to find factorial of a int'''
    if x==0 or x==1:
        return 1
    else:
        return x*factrorial(x-1)
    
print(factrorial.__doc__)
print("the factororial of 0:",factrorial(0))
print("the factororial of 1:",factrorial(1))
print("the factororial of 4:",factrorial(4))
print("the factororial of 5:",factrorial(5))
print("the factororial of 10:",factrorial(10))