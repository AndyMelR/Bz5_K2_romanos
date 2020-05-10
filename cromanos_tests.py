import unittest
import cromanos

class RomanNumberTest(unittest.TestCase):
    def setUp(self):
        self.nr = cromanos.RomanNumber()

    def test_symbols_romans(self):

        self.assertEqual(self.nr.romano_a_entero('I'),1)
        self.assertEqual(self.nr.romano_a_entero('V'),5)
        self.assertEqual(self.nr.romano_a_entero('X'),10)
        self.assertEqual(self.nr.romano_a_entero('L'),50)
        self.assertEqual(self.nr.romano_a_entero('C'),100)
        self.assertEqual(self.nr.romano_a_entero('D'),500)
        self.assertEqual(self.nr.romano_a_entero('M'),1000)
        self.assertEqual(self.nr.romano_a_entero('K'),'Error en formato')
        self.assertEqual(self.nr.romano_a_entero(''),'Error en formato')
    
    def test_repetitions(self):
        self.assertEqual(self.nr.romano_a_entero('II'),2)
        self.assertEqual(self.nr.romano_a_entero('MMM'),3000)
        self.assertEqual(self.nr.romano_a_entero('KKK'),'Error en formato')
        self.assertEqual(self.nr.romano_a_entero('MK'),'Error en formato')

    def test_only_three(self):
        self.assertEqual(self.nr.romano_a_entero('IIII'),'Error en formato')

    def test_digitos_decrecientes(self):
        self.assertEqual(self.nr.romano_a_entero('XVIII'),18)
        self.assertEqual(self.nr.romano_a_entero('XI'),11)
        self.assertEqual(self.nr.romano_a_entero('XV'),15)
        self.assertEqual(self.nr.romano_a_entero('XX'),20)
        
    
    def test_digitos_restan(self):
        self.assertEqual(self.nr.romano_a_entero('XIX'),19)
       

    def test_resta_separacion_un_grado(self):
        self.assertEqual(self.nr.romano_a_entero('XC'),90)
        self.assertEqual(self.nr.romano_a_entero('XD'),'Error en formato')
        self.assertEqual(self.nr.romano_a_entero('XM'),'Error en formato')
        self.assertEqual(self.nr.romano_a_entero('IL'),'Error en formato')

    def test_resta_de_multiplos_de_5_no(self):
        self.assertEqual(self.nr.romano_a_entero('VC'),'Error en formato')
        self.assertEqual(self.nr.romano_a_entero('XCV'),95)

    def test_resta_un_solo_simbolo(self):
        self.assertEqual(self.nr.romano_a_entero('XXL'),'Error en formato')
        self.assertEqual(self.nr.romano_a_entero('IXL'),'Error en formato')
        self.assertEqual(self.nr.romano_a_entero('XXX'),30)

    def test_crea_romano(self):
        nr = cromanos.RomanNumber(25) #primer numero romano
        self.assertEqual(nr.value,25)
        self.assertEqual(nr.rvalue,XXV)

        snr = cromanos.RomanNumber('XXIV') #segundo numero romano
        self.assertEqual(snr.value,24)
        self.assertEqual(snr.rvalue,'XXV')

        tnr = cromanos.RomanNumber('XXXX') #tercer numero romano
        self.assertEqual(tnr.value,'Error en formato')
        self.assertEqual(tnr.rvalue,'Error en formato')

        cnr = cromanos.RomanNumber(0)# cuarto numero romano
        self.assertEqual(cromanos.rvalue,'Overflow')
        self.assertEqual(cromanos.rvalue,'Overflow')

        qnr = cromanos.RomanNumber (4000) #quinto numero romano
        self.assertEqual(qnr.value,'Overflow')
        self.assertEqual(qnr.rvalue,'Overflow')

    def test_representation(self):
        nr = cromanos.RomanNumber(25)
        self.assertEqual(str(nr), 'XXV')
        self.assertEqual(nr, 'XXV')
    
    def test_equal_romanos(self):
        nr1 = cromanos.RomanNumber(25)
        nr2 = cromanos.RomanNumber('XXV')
        self.assertEqual(nr1, nr2)

    def test_add_roman(self):
        nr1 = cromanos.RomanNumber(1)
        nr2 = cromanos.RomanNumber('XXIV')
        nr3 = nr1 + nr2
        self.assertEqual(nr1 + nr2,RomanNumber(25))
        self.assertEqual(nr3,value, 25)
        self.assertTrue(isinstance(nr3, cromanos.RomanNumber))
    
    def test_add_integer(self):
        nr1 = cromanos.RomanNumber(23)
        nr3 = nr1 + 1
        self.assertEqual(nr3, cromanos.RomanNumber,24)
        self.assertTrue(isinstance(nr2, cromanos.RomanNumber)


if __name__ == '__main__':
    unittest.main()


