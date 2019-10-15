def RecursiveFactorial(num):
    if num <=1:
        return num
    else:
        return num * RecursiveFactorial(num - 1)

print(RecursiveFactorial(5))