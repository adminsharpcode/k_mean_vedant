"""
Model lauch karna hai jaha mere model number mein 201 ata hai compulsory hai ye baat honi hi chahiye
"""

def Numbertoprint():
 numberlist = [number for number in range (1,10000) if "201" in str(number)]
 print(numberlist)

Numbertoprint()


def numtoprint():
    numberlist=[12837201,1522019162,92163782201,72153201263,201872637,8712637198,9162387123,8917238129836,1273981623]
    for number in numberlist:
        if "201" in str(number):
            print("number 201 has occured following times")
            print(number)

numtoprint()
