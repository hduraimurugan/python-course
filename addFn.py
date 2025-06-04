# def add(a,b):
#     return a+b

def add(*args):
    total=0
    print("Args",args) #tuple
    for num in args:
        total+=num
    return total