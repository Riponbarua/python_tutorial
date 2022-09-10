def save_youser(**user):
    print(user)

save_youser(id=1,name="john",age=22)

print("********************************************")

def save_youser(**user):
    print(user["id"])

save_youser(id=1,name="john",age=22)

print("**********************************************")

def save_youser(**user):
    print(user["name"])

save_youser(id=1,name="john",age=22)
