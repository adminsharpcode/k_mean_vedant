"""
fuctions perform karo
"""
def numberoperation():

    num1 = float(input("Enter the value of num1"))
    num2 = float(input("Enter the value of num2"))
    result = num1 + num2
    print(result)
    result = num1 * num2
    print(result)
    result = num1 - num2
    print(result)
numberoperation()

def House():

    number = int(input("Enter the Ages of the member 1"))
    number1 = int(input("Enter the Ages of the member 2"))
    number2 = int(input("Enter the Ages of the member 3"))
    number3 = int(input("Enter the Ages of the member 4"))

    if  number > number1 > number2 > number3:
        print("Person 1 is Aged that everyone:")
    elif number < number1 < number2 < number3:
        print("person 4 is aged than everyone:")
    elif number < number1 < number3 < number2:
        print("person 3 is aged than everyone:")
    elif number < number2 < number3 < number1:
        print("person 2 is aged than everyone:")

House()

"""" for i in range (10):
print(i)
"""

"""counter = 0
   while counter < 3:
       print('hellow world')
       counter = counter+1"""

# for car with diff numberplates car ke name bhi hai usme even day pe konsi gadi niklegi odd day pe konsi niklegi



def cars():
    listcarname= ["maruti", "suzuki", "beloro"]
    listcarnumber=[2003 , 2004 , 2005]

    cardictionary = dict(zip(listcarname,listcarnumber))
    print(cardictionary)
    counter = 0
    i = 0
    j = 0

    while counter <3:
        if listcarnumber[i] % 2 == 0:
            print(listcarname[i],listcarnumber[i])
            counter = counter + 1
            i = i + 1
            print("will work on even days")
        elif listcarnumber[i] % 2 != 0:
            print("car number is not even")
            print(listcarname[i], listcarnumber[i])
            counter = counter+1
            i = i+1
            print("wont work on even days")

cars()