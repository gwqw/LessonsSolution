import math

n=100000

print("log(log(n))=", math.log(math.log(n, 2)))
print("sqrt(log_4(n))=", math.sqrt(math.log(n, 4)))
print("log_3(n)=", math.log(n, 3))
print("log(n)^2=", math.log(n, 2) ** 2)
print("sqrt(n)=", math.sqrt(n))
print("n/log(n)=", n / math.log(n, 5))
print("log(n!)=", math.log(math.factorial(n),2))
print("3^log(n)=", 3 ** math.log(n, 2))
print("n^2=", n ** 2)
print("7^log(n)", 7 ** (math.log(n, 2)))
"""
print(math.log(n, 2) ** (math.log(n, 2)))
print(n ** (math.sqrt(n)))
print(n ** (math.log(n, 2)))
print(2 ** n)
print(4 ** n)
print(2 ** (3 * n))
print(math.factorial(n))
print(2 ** (2 ** n))
"""
