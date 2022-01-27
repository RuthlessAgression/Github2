# # a = 'static method'
# # b = 'class method and'
# # print(f'this is {b} {a}', 'testing'
# example = {}
# example["AR"] = {
#     "name" : "Python: Current File",
#             "type" : "python",
#             "request" : "launch",
#             "program" : "testing",
#             "console" : "integratedTerminal"
# }
# import json
# a=json.dumps(example)
# with open("c://tempfile//new.txt", "w") as f:
#     f.write(a)
# f = open("c://tempfile//new.txt", "r")
# a = f.read()
# print(a)
# example = json.loads(a)
# print(example)
# b = example['AR']['type']
# print(b)
# for person in example:
#     print(example[person])

# f.close()
# print(f.closed)
