import json

#test = {'t1':{'x1':(1, 2), 'x2':(2, 3), 'x3':(1, 3), 'x4':(3, 4), }}#, 't2':[(7, 8), (9, 10), (11, 12)]}
test2 = {'t1':{'x1_0':(1, 2), 'x2_0':(2, 3), 'x3_0':(2, 4), 'x1_1':(4, 5), 'x3_1':(7, 9)}}

with open('convert.json', 'w') as convert_file:
    convert_file.write(json.dumps(test2))