from hashlib import new


class g():
    #def imprime(self):
    #    print("G")
    pass

class f():
    #def imprime(self):
    #    print("F")
    pass
        
class e(g):
    #def imprime(self):
    #    print("E") 
    pass

class d():
    def imprime(self):
        print("D")                   

class c(f):
    #def imprime(self):
    #    print("C")
    pass

class b(c, e):
    #def imprime(self):
    #    print("B")
    pass

class a(b, d):
    #def imprime(self):
    #    print("A") 
    pass

teste = a()

teste.imprime()