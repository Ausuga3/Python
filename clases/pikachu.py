class Pikachu:
    #estas son generales
    tipo = 'Electrico'


    #estas son especificas
    def __init__(self,nombre,nivel,sal):
        self.nombre = nombre
        self.nivel = nivel
        self.salud = sal

    
    def atacar(self):
        print(f"pikachu ataca y genera {self.nivel/4} de daño")

pikachu1= Pikachu('Pepe',750,500)
pikachu2=Pikachu('Roco',1200,1000)

#print(pikachu1.tipo,pikachu1.nombre,pikachu1.salud)
print(f"El pikachu llamado {pikachu1.nombre} ataca.")
pikachu1.atacar()

print(f"El pikachu llamado {pikachu2.nombre} ataca.")
pikachu2.atacar()






