import json

#test = {'t1':{'x1':(1, 2), 'x2':(2, 3), 'x3':(1, 3), 'x4':(3, 4), }}#, 't2':[(7, 8), (9, 10), (11, 12)]}
test2 = {'t1':{'x1':[(1, 2), (4, 5)], 'x2':[(2, 3)], 'x3':[(2, 4), (7, 9)]},
         't2':{'x1':[(2, 3), (5, 6)], 'x2':[(3, 4)], 'x3':[(3, 5), (8, 10)]}}

with open('convert.json', 'w') as convert_file:
    convert_file.write(json.dumps(test2))

