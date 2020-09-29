
def left_join(d1,d2):
    output = []
    for key in d1.keys():
       if key in d2.keys():
           output.append([key,d1[key],d2[key]])
       else:
           output.append([key,d1[key],'NULL'])
    return output



dict1 = {'fond':'enamored','wrath':'anger','diligent':'employed','outfit':'garb','guide':'usher','hello':'everyone'}
dict2 = {'fond':'averse','wrath':'delight','diligent':'idle','guide':'follow','flow':'jam'}

print(left_join(dict1,dict2))


