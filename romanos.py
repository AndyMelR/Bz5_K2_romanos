romanos = {'M':1000,
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



def romano_a_entero(numero_romano):
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
                if letraAnt + letra in romanos.keys() and numRepes < 2 and not fueResta:
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

def entero_a_romano(valor):
    if valor > 3999 :
        return 'Overflow'
    
    componentes = descomponer(valor)

    res=''
    for valor in componentes :
        while valor > 0:
            k, v = busca_valor_menor_o_igual(valor)
            valor -= v
            res += k
    return res

def busca_valor_menor_o_igual(v):
    for key,value in romanos.items():
        if value <= v:
            return key,value

def descomponer(numero):
    res = []
    for i in range(3,0,-1):
        resto = numero % 10**i
        res.append(numero - resto)
        numero = resto
    res.append(numero)
    return res


