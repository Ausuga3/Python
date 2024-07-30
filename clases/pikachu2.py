class Pikachu:
    #estas son generales
    tipo = 'Electrico'


    #estas son especificas
    def __init__(self,nombre,nivel,salud,voltajeMax,amperajeMax,color):
        self.nombre = nombre
        self.nivel = nivel
        self.salud = salud
        self._voltajeMaximo = voltajeMax
        self._amperajeMaximo = amperajeMax
        self.color = color

    
    def atacar(self):
        print(f"pikachu ataca y genera {self.nivel/4} de daño")

pikachu1=Pikachu('Pika',780,100,6,2,'Amarillo')
pikachu1.nivel= 900
print(f"El pikachu llamado {pikachu1.nombre} es nivel {pikachu1.nivel} y es de tipo {pikachu1.tipo}")

