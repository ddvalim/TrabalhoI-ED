from Elemento import Elemento

class Fila:
    def __init__(self, limite:int):
        self.__limite = limite
        self.__fim = None
        self.__inicio = None
        self.__numero_de_elementos = 0


    def get_inicio(self):
        return self.__inicio

    
    def get_fim(self):
        return self.__fim


    def fila_vazia(self):
        return self.__numero_de_elementos == 0


    def fila_cheia(self):
        return self.__numero_de_elementos == self.__limite
    
    
    def retira_elemento(self):
        if self.fila_vazia() == True:
            raise Exception("A fila está vazia!")
        else:
            if self.__inicio == self.__fim:
                self.__inicio = None
                self.__fim = None
                self.__numero_de_elementos -= 1
                return self.__inicio
            else:
                element = self.__inicio
                self.__inicio = element.get_anterior()
                self.__numero_de_elementos -= 1
                return self.__fim.get_numero()
    

    def insere_elemento(self, elemento:object):
        if isinstance(elemento, Elemento):
            if self.fila_cheia() != True:
                if self.__numero_de_elementos == 0: #Significa que a fila esta vazia
                    self.__inicio = elemento
                    self.__fim = elemento
                    self.__numero_de_elementos += 1
                    return self.__inicio.get_numero()
                else:
                    elemento.set_anterior(self.__fim)
                    self.__numero_de_elementos += 1
                    self.__fim = elemento
                    return
            else:
                raise Exception("A fila está cheia, impossível adicionar um novo elemento!")
        else:
            raise Exception("O parâmetro passado não é do tipo Elemento!")

# TESTES #

e = Elemento(9)
f = Fila(10)
f.insere_elemento(e)
print(f.fila_cheia())
print(f.fila_vazia())
f.retira_elemento()
print(f.fila_vazia())

# ------------- #

d = Elemento(5)
f.insere_elemento(d)
print(f.get_inicio())
print(f.get_fim())
f.retira_elemento()

# ------------- #

y = Elemento(2)
a = Elemento(6)
u = Elemento(7)
i = Elemento(4)
k = Elemento(23)
p = Elemento(89)
q = Elemento(13)
l = Elemento(22)

f.insere_elemento(e)
f.insere_elemento(d)
f.insere_elemento(y)
f.insere_elemento(a)
f.insere_elemento(u)
f.insere_elemento(i)
f.insere_elemento(k)
f.insere_elemento(p)
f.insere_elemento(q)
f.insere_elemento(l)

print(f.fila_cheia())
print(f.fila_vazia())

print(f.retira_elemento())
elemento_final = Elemento(76)
print(f.insere_elemento(elemento_final))
#print(f.insere_elemento(48))
