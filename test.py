district = list()

with open('test.txt','r') as file:
    for i in file.readlines():
        sets = (i,i)
        district.append(sets)
    

print(district)

