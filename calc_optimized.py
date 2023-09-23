
not_valid = True

while not_valid:
    eqn = input()
    if(eqn.find("+")!=-1):
        sign = "+"
        input1 = int(eqn[0:eqn.find(sign)])
        input2 = int(eqn[eqn.find(sign)+1:])
        result = input1+input2
        not_valid = False
    elif(eqn.find("-")!=-1):
        sign = "-"
        input1 = int(eqn[0:eqn.find(sign)])
        input2 = int(eqn[eqn.find(sign)+1:])
        result = input1-input2
        not_valid = False
    elif(eqn.find("*")!=-1):
        sign = "*"
        input1 = int(eqn[0:eqn.find(sign)])
        input2 = int(eqn[eqn.find(sign)+1:])
        result = input1*input2
        not_valid = False
    elif(eqn.find("/")!=-1):
        sign = "/"
        input1 = int(eqn[0:eqn.find(sign)])
        input2 = int(eqn[eqn.find(sign)+1:])
        result = input1/input2
        not_valid = False
    else:
        print("Please input a valid arithmatic operation: \n")

print("""
_________________
|""",result,"""
|___________| + |
| 7 | 8 | 9 | - |
| 4 | 5 | 6 | * |
| 1 | 2 | 3 | / |
|___________|___|
    """)

