# Calculator
from art import logo
#Add
def add(n1,n2):
    return n1+n2

#Subtract
def subtract(n1,n2):
    return n1-n2

#Multiply
def multiply(n1,n2):
    return n1*n2

#Divide
def divide(n1,n2):
    return n1/n2

def calculator(firs_num , second_num):
    for key in operations:
        print(f"{key} ")
    operation = input("Pick an operation from the list above: ")
    function = operations[operation]
    answer = function(firs_num, second_num)
    print(f"{firs_num} {operation} {second_num} = {answer}")
    return answer
    

operations = {
    "+":add,
    "-":subtract,
    "*":multiply,
    "/":divide,
}

def main():
    print(logo)
    num1 = int(input("What is the first number: "))
    anotherOperation = True

    while anotherOperation:
        num2 = int(input("What is the next number: "))
        answer = calculator(num1, num2)
        continue_calc = input(f"continue calculating with {answer}? y or n:  ")
        if continue_calc == "y":
            num1 = answer
        else:
            anotherOperation = False
            main()

main()