class Elemento:
    def __init__(self, num):
        self.__num = num
        self.__anterior = None
    

    def get_numero(self):
        return self.__num
    

    def get_anterior(self):
        return self.__anterior
    

    def set_anterior(self, elemento):
        self.__anterior = elemento
