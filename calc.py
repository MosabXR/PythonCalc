calc = """
_________________
|
|___________| + |
| 7 | 8 | 9 | - |
| 4 | 5 | 6 | * |
| 1 | 2 | 3 | / |
|___________|___|
"""

print(calc)

input1 = int(input("Enter first input: "))
inputsign = input("Enter operation sign: ")
input2 = int(input("Enter second input: "))

if(inputsign == '+'):
    print("""
    _________________
|""",input1+input2,"""
|___________| + |
| 7 | 8 | 9 | - |
| 4 | 5 | 6 | * |
| 1 | 2 | 3 | / |
|___________|___|
    """)
    
elif(inputsign == '-'):
    print("""
    _________________
|""",input1-input2,"""
|___________| + |
| 7 | 8 | 9 | - |
| 4 | 5 | 6 | * |
| 1 | 2 | 3 | / |
|___________|___|
    """)
elif(inputsign == '*'):
    print("""
    _________________
|""",input1*input2,"""
|___________| + |
| 7 | 8 | 9 | - |
| 4 | 5 | 6 | * |
| 1 | 2 | 3 | / |
|___________|___|
    """)
elif(inputsign == '/'):
    print("""
    _________________
|""",input1/input2,"""
|___________| + |
| 7 | 8 | 9 | - |
| 4 | 5 | 6 | * |
| 1 | 2 | 3 | / |
|___________|___|
    """)
else:
    print("Please enter valid inputs.")
