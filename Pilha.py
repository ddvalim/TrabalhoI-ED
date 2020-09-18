from Elemento import Elemento

class Pilha:
    def __init__(self, limite):
        self.__limite = limite
        self.__top = None


    def pilha_cheia(self):
        if self.__top == None:
            return False
        else:
            i = 0
            element = self.__top
            while element.get_anterior() != None:
                element = element.get_anterior()
                i += 1
            return i == self.__limite


    def pilha_vazia(self):
        return self.__top == None


    def get_top(self):
        if self.__top == None:
            raise Exception("Pilha vazia!")
        else:
            return self.__top.get_numero()


    def push(self, elemento:object):
        if isinstance(elemento, Elemento) and self.pilha_cheia() != True:
            if self.__top == None:
                self.__top = elemento
                return elemento.get_numero()
            else:
                elemento.set_anterior(self.__top)
                self.__top = elemento
                return elemento.get_numero()
        else:
            raise Exception("Algo deu errado...")


    def pop(self):
        if self.__top == None:
            raise Exception("Não há nada para eliminar!")
        else:
            elemento = self.__top
            self.__top = elemento.get_anterior()

# TESTES #

e = Elemento(9)
p = Pilha(10)
p.push(e)
print(p.pilha_vazia())
print(p.pilha_cheia())
print(p.get_top())
p.pop()
print(p.get_top())