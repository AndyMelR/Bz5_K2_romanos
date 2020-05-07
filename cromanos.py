romanos = {'M':1000,
        'D':500,
        'C':100,
        'L':50,
        'X':10,
        'V':5,
        'I':1
    }     

    def __init__(self,valor):
        if instance(valor, str):
            self.value = self.romano_a_entero(valor)
            if self.value = 'Error en formato'
                self.rvalue == self.value
            else:
                 self.rvalue = valor
        else:
            self.value = valor
            self.rvalue = self.entero_a_romano()
            if self.value == 'Overflow'
                self.value = self.rvalue
    
def romano_a_entero(self,valor):
        if numero_romano == '':
            return 'Error en formato'
        entero = 0 
        numRepes = 1 #guardamos número de repeticiones
        letraAnt = ''
        fueResta = False
        for letra in numero_romano:#bucle para recorrer cada letra del digito introducido

        if letra in romanos:
            if letraAnt == '' or  romanos[letraAnt] >= romanos[letra]:    
                entero += romanos[letra] #acumulamos
                fueResta = False #primera resta
            else:
                if letraAnt + letra in existen and numRepes < 2 and not fueResta: #si estan en existen
                     entero = entero - romanos[letraAnt] * 2 + romanos[letra] 
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

def __repr__(self)
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
    return resultado

def __rsub__(self,other):
    return self.__sub__(other)

def __eq__(self,other):
    return self.value == other.value

