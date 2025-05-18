def wraper(func):
    def greet():
      func()
      print("Hello good morning : ")

@greet
def Data():
    print("Vineet")


Data()