import json

test1 = {'t1': [('a', 5), (None, 3), ('b', 2)], 
             't2': [('c', 2), ('d', 1), (None, 3), ('c', 2)],
             't3': [('e', 1), ('f', 2), (None, 7), ('f', 5)]}
test2 = {'t1': [('a', 3), ('b', 2), ('c', 1)],
            't2': [('d', 1), ('e', 2), ('f', 3)],
            't3': [('g', 1), ('h', 2), ('i', 3)]}


with open('convert.json', 'w') as convert_file:
    convert_file.write(json.dumps(test1))
    convert_file.write(json.dumps(test2))

