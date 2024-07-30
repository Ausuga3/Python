class humano:
    def __init__(self,edad):
        self.edad = edad
        
    def hablar(self,mensaje):
        print(mensaje)
            

pedro = humano(26)
raul = humano(21)

print(f'soy pedro y tengo {pedro.edad} años')
print(f'soy raul y tengo {raul.edad} años')

pedro.hablar('Hola')
raul.hablar('Hola Pedro')