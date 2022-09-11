for number in range(1,10):
    print(number)
print("*************************************")
for number in range(1,10):
    if number % 2 ==0:
        print(number)

print("*************************************")
count = 0
for number in range(1,10):
    if number % 2 ==0:
        count+=1
        print(number)