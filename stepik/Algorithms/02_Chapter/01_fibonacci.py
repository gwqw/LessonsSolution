def fib(n):
    # put your code here
    if n <= 1: return 1
    f = [1, 1]
    for i in range(2, n):
        f.append(f[i-1] + f[i-2])
    return f[n-1]

def main():
    n = int(input())
    print(fib(n))


if __name__ == "__main__":
    main()
