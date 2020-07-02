def decorators1 (func1):
    def wrap_function():
        print ("decorating the header ")
        func1()
        print ("decorating the footer ")
    return wrap_function()

@decorators1
def prnt1():
    print ("Undecorated function ")

