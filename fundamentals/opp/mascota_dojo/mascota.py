class Mascota:

    def __init__(self, nombre , tipo, golosinas, salud, energia):
        self.nombre = nombre
        self.tipo = tipo
        self.golosinas = golosinas
        self.salud = 100
        self.energia = 50
        

    def dormir(self):
        self.energia += 25
        return self

    def comer(self):
        self.energia += 5
        self.salud += 10
        return self

    def jugar(self):
        self.salud += 5
        self.energia -= 15
        return self

  



class Ninja:
    def __init__(self, nombre, apellido , golosina, alimento, mascota):
        self.nombre = nombre
        self.apellido = apellido
        self.golosina = golosina
        self.alimento = alimento
        self.mascota = mascota

    def caminar(self):
        self.mascota.jugar()
        return self

    def feed(self):

        if len(self.alimento) > 0:
            food = self.alimento()
            print(f"Alimentacion{self.mascota.nombre} {food}!")
            self.mascota.comer()
        else:
            print("Necesitas más comida para mascotas")
        return self

    def bathe(self):
        self.pet.noise()

mi_alimento = ['Snausage','Bacon',"Trash Bag"]
mi_golosina = ['Pizza','Burger']

bocados = Mascota("Fido","Jack",['nibbles on things','is invisible'],"Hey Hey")

adrien = Ninja("Adrien","Dion",mi_golosina,mi_alimento, bocados)

adrien.feed();
adrien.feed();
adrien.feed();