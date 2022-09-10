def mulyiply( *numbers):
    print(numbers)
mulyiply(3,4,5,6,7)

print("******************************************")

def mulyiply( *numbers):
    for number in numbers:
       print(number)

mulyiply(3,4,5,6,7)
print("******************************************")

def multyply(*numbers):
    total =1
    for number in numbers:
        total *= number
    return total
print(multyply(2, 3, 4, 5))


