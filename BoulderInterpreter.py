   
import sys

class BoulderInterpreter:
    def __init__(self):
        self.stack = []
        
    def interpret(self, code, i):
        instructions = code
        while i < len(instructions):
            instruction = instructions[i]
            if instruction.startswith('BETA'):
                user_input = input("BETA: ")
                self.stack.append(user_input)
            elif instruction.startswith('DYNO'):
                user_input = input("DYNO: ")
                print(user_input)
            elif instruction.startswith('CAMPUS'):
                user_input = input("CAMPUS: ")
                print(int(user_input))
            elif instruction.startswith('FLASH'):
                print(instruction[6:])
            elif instruction.startswith('CHALK'):
                self.stack.append(instruction[6:])
            elif instruction.startswith('FLAG'):
                print(str(self.stack.pop()))
            elif instruction.startswith('SMEAR'):
                print(int(self.stack.pop()))
            elif instruction.startswith('MATCH'):
                x = self.stack.pop()
                print(x)
                self.stack.append(x)
            elif instruction.startswith('GASTON'):
                while len(self.stack) > 0:
                    sys.stdout.write(self.stack.pop()),
            elif instruction.startswith('JUG'):
                self.stack.append(int(self.stack.pop()) + int(self.stack.pop()))
            elif instruction.startswith('POCKET'):
                operand2 = int(self.stack.pop())
                operand1 = int(self.stack.pop())
                self.stack.append(operand1 - operand2)
            elif instruction.startswith('SLOPE'):
                operand2 = int(self.stack.pop())
                operand1 = int(self.stack.pop())
                self.stack.append(operand1 * operand2)
            elif instruction.startswith('CRIMP'):
                operand2 = int(self.stack.pop())
                operand1 = int(self.stack.pop())
                if operand2 != 0:
                    self.stack.append(operand1 / operand2)
                else:
                    print("Error: Division by zero")
            elif instruction.startswith('TRAVERSE'):
                count = int(self.stack.pop())
                traverse_code = []
                i += 1
                j = i
                while j < len(instructions) and not instructions[j].startswith('END TRAVERSE'):
                    traverse_code.append(instructions[j])
                    j += 1
                for _ in range(count):
                    self.interpret(traverse_code, 0)
                i += len(traverse_code)
            elif instruction.startswith('SEND'):
                user_input = input("SEND: ")
                for char in user_input:
                    self.stack.append(char)
            i += 1

if __name__ == "__main__":
    interpreter = BoulderInterpreter()
    try:
        fileName = 'ReverseString.bldr'
        file = open(fileName)
        code = file.read().split('\n')
        interpreter.interpret(code, 0)
        file.close
    except Exception as e:
        print(f"error while opening file:\n{e}")
        sys.exit(0)
    
