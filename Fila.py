from Elemento import Elemento

class Fila:
    def __init__(self, limite):
        self.__limite = limite
        self.__fim = None
        self.__inicio = None

    def get_inicio(self):
        return self.__inicio

    
    def get_fim(self):
        return self.__fim


    def fila_vazia(self):
        if self.__inicio == None:
            return True
        else:
            return False


    def fila_cheia(self):
        if self.__fim == None and self.__inicio == None:
            return False
        else:
            i = 0
            element = self.__inicio
            while self.__inicio.get_anterior() != None:
                i += 1
                element = element.get_anterior()
            return self.__limite == i
    
    
    def pop(self): #Alternar nome
        if self.fila_vazia() == True:
            raise Exception("A fila está vazia!")
        else:
            if self.__inicio == self.__fim:
                self.__inicio = None
                self.__fim = None
            else:
                element = self.__inicio
                self.__inicio = element.get_anterior()
    

    def push(self, elemento:object):  #Alterar nome
        if isinstance(elemento, Elemento) and self.fila_cheia != True:
            
            if self.__inicio == None: #Significa que a fila esta vazia
                self.__inicio = elemento
                self.__fim = elemento
                return self.__inicio.get_numero()
            
            else:
                
                if self.__fim == None:
                    self.__fim = elemento
                    return self.__fim.get_numero()
                
                else:
                    elemento.set_anterior(self.__fim)
                    self.__fim = elemento
                    return
        
        else:
            raise Exception("Algo deu errado...")

# TESTES #

e = Elemento(9)
f = Fila(10)
f.push(e)
print(f.fila_cheia())
print(f.fila_vazia())
f.pop()
print(f.fila_vazia())

d = Elemento(5)
f.push(d)
print(f.get_inicio())
print(f.get_fim())
