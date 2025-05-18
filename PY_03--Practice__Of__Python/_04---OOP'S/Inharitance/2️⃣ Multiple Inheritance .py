class Father:
    def Quality1(self):
        print("Hardworking")

class Mather:
    def Quality2(self):
        print("Loving")

class Chiled(Father,Mather):
    def Quality3(self):
        print("Donon Hai Parent Ki")

ob = Chiled()
ob.Quality1()
ob.Quality2()
ob.Quality3()