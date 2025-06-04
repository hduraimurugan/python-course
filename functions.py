from addFn import add

# def greet(name):
#     print(f"Hello and Welcome {name}!" )
#
# greet("Durai")
#
# def add(a,b):
#     return a+b

# result= add(1,4,5,6,7,8,9)
# print(result)

def create_profile(**kwargs):
    print("Kwargs",kwargs) #Dict - datatype
    print("---User Profile---")
    for key,value in kwargs.items():
        print(f"{key} : {value}")
    print("--- --- ---")

create_profile(name="Durai", age=26, job="FSD")