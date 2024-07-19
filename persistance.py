def persistence(n):
    def helper(n ,counter):
        if n < 10:
            return counter

        result = 1
        for i in str(n):
            result = result * int(i)
        return helper(result , counter +1)
    return helper(n , 0)
       
print(persistence(999))