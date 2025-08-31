#1
def remove_and_collect_evens(lst):
    result = []
    for num in lst:
        if num % 2 == 0:
            result.append(num)
    print(result)





#5
def calculate(a, b, operator):
    if operator == "+":
        print(a + b)
    elif operator == "-":
        print(a - b)
    elif operator == "*":
        print(a * b)
    elif operator == "/":
        if b == 0:
            print("cant divide by zero")
        else:
            print(a / b)
    else:
        print("incorrect")




#7
def alphabet_n(n):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    result = ""
    i = 0
    while i < n:
        result = result + alphabet[i]
        i = i + 1
    print(result)


#8
def hello_world():
    print("hello world")
