# Calculator

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


operations = {
    "+":add,
    "-":subtract,
    "*":multiply,
    "/":divide,
}

num1 = int(input("What is the first number: "))
num2 = int(input("What is the second number: "))

for key in operations:
    print(f"{key} ")

operation = input("Pick an operation from the list above: ")
function = operations[operation]

answer = function(num1, num2)

print(f"{num1} {operation} {num2} = {answer}")