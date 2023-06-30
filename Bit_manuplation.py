def add_one(num):
    mask = 1
    while num & mask:
        num = num ^ mask
        mask <<= 1

    num = num ^ mask
    return num
num = 42
num = add_one(num)
print("The new value of num is {num}")

