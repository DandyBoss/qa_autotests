def factrl(n):
    if n<0:
        return "input error"
    else:
        res = 1
        for i in range(1,n+1):
            res*=i
        return res



