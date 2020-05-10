import romanos

class RomanNumber():

    __symbols = {'M':1000,
            'CM':900,
            'D':500,
            'CD':400,
            'C':100,
            'XC':90,
            'L':50,
            'XL':40,
            'X':10,
            'IX':9,
            'V':5,
            'IV':4,
            'I':1
        }


    def  __init__(self,valor):
        if isinstance(valor, str):
            self.value = self.romano_a_entero(valor)
            if self.value =='Error en formato':
                self.rvalue = self.value
            else:
                    self.rvalue = valor
        else:
            self.value = valor
            self.rvalue = self.entero_a_romano()
            if self.value == 'Overflow':
                self.value = self.rvalue   

             
        
    def romano_a_entero(self,numero_romano):
        if numero_romano == '':
            return 'Error en formato'
        entero = 0 
        numRepes = 1 #guardamos número de repeticiones
        letraAnt = ''
        fueResta = False

        for letra in numero_romano:#bucle para recorrer cada letra del digito introducido

            if letra in self.__symbols:
                if letraAnt == '' or  self.__symbols[letraAnt] >= self.__symbols[letra]:    
                    entero += self.__symbols[letra] #acumulamos
                    fueResta = False #primera resta
                else:
                    if letraAnt + letra in __self.symbols.keys() and numRepes < 2 and not fueResta: #si estan en existen
                        entero = entero - __self.symbols[letraAnt] * 2 + self.__symbols[letra] 
                        fueResta = True 
                    else:
                        return 'Error en formato'
            else:
                return 'Error en formato'
            
            if letra == letraAnt and numRepes == 3:
                return 'Error en formato'
            elif letra == letraAnt : #validamos letra Ant en este bucle
                numRepes += 1 #acumulamos letras hasta llegar a 3
            else:
                numRepes = 1
            
            letraAnt = letra #siempre debe ser lo último. Las igual para poder compararlas y saber si ya ha salido
                
        return entero

    def entero_a_romano(self):
        if self.value <1 or self.value > 3999:
            return 'Overflow'
            if valor > 3999 :
        return 'Overflow'
    
    '''componentes = descomponer(valor)

    res=''
    for valor in componentes :
        while valor > 0:
            k, v = __busca_valor_menor_o_igual(valor)
            valor -= v
            res += k
    return res'''
    
    def __busca_valor_menor_o_igual(self,v):
        for key ,value in self.__symbols.items():
            if value <= v:
                return key,value

    def __descomponer(self, numero):
        res = []
        for orden in range(3, 0, -1):
            resto = numero %10 ** orden
            res.append(numero - resto)
            numero = resto
        res.append(numero)
        return res

    def __str__(self):
        return self.rvalue

    def __repr__(self):
        return self.rvalue

    def __add__(self,other): #metodo magico
        if isinstance(other,int):
            suma = self.value + other
        else:
            suma = self.value + other.value #ahora debo crear otra instancia:
        resultado = RomanNumber(suma) #tengo que crear una nueva instancia. Le asignamos una variable para instanciarla
        return resultado

    def __radd__(self,other): #metodo magico
        return self.__add__(other)
        '''if isinstance(value,int) #principio de no repetirse de programacion
            suma = self.value +second_value
        else:
            suma = self.value + second_value.value #ahora debo crear otra instancia:
        resultado = RomanNumber(suma) #tengo que crear una nueva instancia. Le asignamos una variable para instanciarla
        return resultado'''

    def __sub__(self,other):
        if isinstance(other,int):
            resta = self.value - other
        else:
            resta = self.value - other.value
        resultado = RomanNumber(resta)
        return resultado

    def __rsub__(self,other):
        return self.__sub__(other)

    def __eq__(self,other):
        return self.value == other.value

