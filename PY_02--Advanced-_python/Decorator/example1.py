# kisi bhi function ko bina change kiye uska output behaviour aleg aaye to decorartoe hai 
# higher order function hai
# function argument me  lega or function hi return kartha hai or function hi return 

# def outer():
#     def inner():
#         print("Hello")
#     return inner

# def new():
#     pass

# x = outer()


def outer_fun(new):
    def inner_fun():
        print("Hello")
    return inner_fun
@outer_fun
def new():
    pass
new()