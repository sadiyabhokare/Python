n=int(input("Enter a number: "))
for i in range(1, n+1):
    if i%2==0:
        continue    # skips the number if even
    print(i)