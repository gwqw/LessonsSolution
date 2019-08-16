def fib_digit(n):
    # put your code here
    if n <= 1: return 1
    f = [1, 1]
    for i in range(2, n):
        if f[i-1] > 1000:
            f.append((f[i-1] + f[i-2]) % 10)
        else:
            f.append(f[i-1] + f[i-2])
    return f[n-1] % 10

def main():
    n = int(input())
    print(fib_digit(n))


if __name__ == "__main__":
    main()
