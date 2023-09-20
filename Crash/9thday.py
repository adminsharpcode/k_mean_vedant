def AGECHECKER():
 name = ["Vedant", "maithili", "atharva", "XD", "LOL", "ROLF"]
 Age = [17, 20, 21, 24, 56, 10]

 counter = 0
 i = 0

 while counter!=6:
    if Age[i]%2==0:
        print(f"{name[i]} has {Age[i]} and is not prime")
        counter = counter + 1
        i = i + 1
    elif Age[i]%3==0:
        print(f"{name[i]} has {Age[i]} and is not prime")
        counter = counter + 1
        i = i + 1
    elif Age[i]%5==0:
        print(f"{name[i]} has {Age[i]} and is not prime")
        counter = counter + 1
        i = i + 1
    elif Age[i]%7==0:
        counter = counter + 1
        print(f"{name[i]} has {Age[i]} and is not prime")
        counter = counter + 1
        i = i + 1
    elif Age[i]%9==0:
        print(f"{name[i]} has {Age[i]} and is not prime")
        counter = counter + 1
        i = i + 1
    else :
        print(f"{name[i]} has {Age[i]} and is prime")
        counter = counter + 1
        i = i + 1

AGECHECKER()

