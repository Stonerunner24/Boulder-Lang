   
import sys

instructions = []  
try:
    fileName = 'Multiply.bldr'
    file = open(fileName)
    instructions = file.read().split("\n")
    file.close
except Exception as e:
    print(f"error while opening file:\n{e}")
    sys.exit(0)

stack = []


for instruction in instructions:
    if instruction.startswith('BETA'):
        user_input = input("BETA: ")
        stack.append(user_input)
    elif instruction.startswith('DYNO'):
        user_input = input("DYNO: ")
        print(user_input)
    elif instruction.startswith('CAMPUS'):
        user_input = input("CAMPUS: ")
        print(int(user_input))
    elif instruction.startswith('FLASH'):
        print(instruction[6:])
    elif instruction.startswith('CHALK'):
        stack.append(instruction[6:])
    elif instruction.startswith('FLAG'):
        print(str(stack.pop()))
    elif instruction.startswith('SMEAR'):
        print(int(stack.pop()))
    elif instruction.startswith('JUG'):
        stack.append(int(stack.pop()) + int(stack.pop()))
    elif instruction.startswith('POCKET'):
        operand2 = int(stack.pop())
        operand1 = int(stack.pop())
        stack.append(operand1 - operand2)
    elif instruction.startswith('SLOPE'):
        operand2 = int(stack.pop())
        operand1 = int(stack.pop())
        stack.append(operand1 * operand2)
    elif instruction.startswith('CRIMP'):
        operand2 = int(stack.pop())
        operand1 = int(stack.pop())
        if operand2 != 0:
            stack.append(operand1 / operand2)
        else:
            print("Error: Division by zero")