dict1={}

numbers=24718961277464127864127412547126408127090089508094886742767524858
for number in [*str(numbers)]:
    if number not in dict1:
        dict1[number]=1
    else:
        dict1[number]+=1


print(dict1)