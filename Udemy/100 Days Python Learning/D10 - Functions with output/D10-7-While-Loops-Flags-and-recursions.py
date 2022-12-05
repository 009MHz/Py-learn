# MISSION: looping the calculation
# math operations
def add(n1, n2):
  return n1 + n2

def subtract(n1, n2):
  return n1 - n2

def multiply(n1, n2):
  return n1 * n2

def divide(n1, n2):
  return n1 / n2
# converting math ops into symbol
operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide
}

def calculator(): # define calculator mechanism
    num1 = int(input("What's the first number?: "))  # user interaction yg berada di luar looping process
    
    calculation = True # looping flags condition
    while calculation:
        operation_symbol = input("Pick an operation: ")
        num2 = int(input("What's the next number?: "))  # berfungsi sebagai second argumen
        calculation_function = operations[operation_symbol]  # converting symbol input to the function name
        answer = calculation_function(num1,num2)  # math operations based on both user arguments
        print(f"{num1} {operation_symbol} {num2} = {answer}")  # displaying the output
        if input(f'Last ouput: {answer}\nType "y" to continue, type "n" to restart the calculation\n') == "y": # prompt to continue or restart the programs
            num1 = answer  # converting last output into first argument math function
        else:
            calculation = False  # ending current session
            calculator() # recall the calculator function to restart the program (recursion)


calculator()  # using the calculator programs