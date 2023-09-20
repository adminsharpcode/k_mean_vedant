def salary():
    salarylist = [2000,5000,6000,1000,2000,3000,6000]
    personname = ["vedant","Maithili","atharva","Lol"]

    counter = 0
    i=0
    sum=0.0
    while counter<7:
        sum = sum + salarylist[i]
        counter = counter + 1
        avg=sum/7
        i = i +1

    print(avg)
    print(personname[0])

salary()
