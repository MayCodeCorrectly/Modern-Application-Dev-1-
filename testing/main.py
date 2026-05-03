from math import sqrt,floor

def is_prime(num:int)->bool:
    if num<2:
        return False
    elif num==2 or num==3:
        return True
    else:
        for i in range(2,floor(sqrt(num)+1)):
            if num%i == 0:
                return False
        return True
