str1 = "        My name is vedant and i am studying cse engineering          "
Sliceddata = str1[0:18:2]
print(Sliceddata)
Mylist = [1,2,3,4,5,6,7,8,9,10]
Slicedlist = Mylist[0:7:2]
print(Slicedlist)
print(Mylist[0])
print(Mylist[3])
print(Mylist[5])
print(str1.upper())
print(str1.title())
print(str1.strip())
print(str1.lstrip())
print(str1.rstrip())
"""
Indexing and Slicing the diffrence is that indexing is 
calling only one character and slicing is called 
when 2 or more characters are going to be called
"""


#Formatting of string is explained below

name = 'vedant'
course = "code unnati 2.0"
print(f"My name is {name} and i am studing in {course}")

list = ["Vedant" , 20 , "Maithili" , 12 ,1, 2, 3, 4,5,6]
print(list[3])
print(list[2:4])

list.append("code")
list.insert(4, "GOD")
list[1]= "NAME"
print(list)
list.pop(2)
print(list)
list.remove("code")
print(list)
list1 = ["vedant", "code", "maithili","XD"]
list1.sort()
print(list1)
touple= (1 ,2 ,3 ,4 ,"vedant", "maithili")
print(touple[2:5])
print(touple)
print(touple[4])
Dictionary = {"Vedant":20,
              "maithili":19,
              "XD":1212121212}
print(Dictionary.values())
Dictionary.update({"Vedant": 22})
Dictionary["AGE"] = 60
print(Dictionary)

subjects1 = {'Physics','Hindi','Chemistry' , 123 ,123 ,2143, 3445, 123, 123, 123}
print(subjects1)
print(type(subjects1))

House = ["6 log the " , "2 log gaye" , " 4 wapas agaye"]
print(House[0])
print(House[1])
print(House[2])

log = 6
log2 = 6-2
log3 = 6-2+4
print(f"{log} the , {log2} log gaye, {log3} log wapas agaye")

#family mein log hai unki salary mentioned hai usme banda add hora hai aur 2 bande exisiting hai unme ek ki kaam hui ek ki badh gayi

family = { "Vedant":2000,
        "Maithili":3000
}

print(family)
family.update({"Code":4000})
print(family)
family.update({"Vedant":1000})
family.update({"Maithili":2000})
print(family)

n = 1
print(type(n))
n = float(n)
print(type(n))
n = bool(n)
print(type(n))
n = str(n)
print(type(n))


XDXD = [12,123, "abc"]
print(type(XDXD))



XDXD1 = ["Vedant" , "Code" , "Maithili"]
XDXD2 = [123, 2134 , 2354]

print(XDXD1,XDXD2)

