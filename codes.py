import random

x = random.randint(0,99)
y = random.randint(0,99)

attempts = 4
while attempts > 0:
    getAns = int(input(f"{x}+{y}== "))
    if getAns == (x+y):
        print("correct..!")
        break
    else:
        print("EEE")
        attempts -= 1
        
print(f"{x}+{y}=={x+y}")


