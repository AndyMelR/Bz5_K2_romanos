romanos = {'M':1000,
        'D':500,
        'C':100,
        'L':50,
        'X':10,
        'V':5,
        'I':1
    }     
existen = ['IV','IX','XL','XC','CD','CM'] #combinaciones aceptadas de menor a mayor y que restan

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

