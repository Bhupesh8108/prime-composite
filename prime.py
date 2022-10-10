a = 1000
number = list(i for i in range(2, a))
for num in range(4, a):
    for div in range(2, int(num/2)+2):
        if num % div == 0:
            try:
                number.remove(num)
                continue
            except:
                pass
prime = number

print(prime)














