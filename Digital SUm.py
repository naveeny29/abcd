def sod(num):
    sum = 0
    while num>0:
        rem = num%10
        sum = sum +rem
        num //= 10
    return sum



num = 4785949
while len(str(num))>1:
    ans = sod(num)
    num = ans
print(ans)
<<<<<<< Updated upstream
=======
#comment
>>>>>>> Stashed changes
