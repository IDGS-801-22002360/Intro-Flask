"""
> >
"""

class Cinepolis:

    def __init__(self):
        self.op = 0
        self.nom = ""
        self.pre = 12
        self.per = 0
        self.bol = 0
        self.total = 0
        self.registros = []

    def menu(self):
        print("========= Cinepolis =========")
        print("1.- Comprar boletos")
        print("2.- Terminar")
        self.op = int(input("Ingrese una opcion: "))
    
    def menuEmergente(self):
        print("1.- Cambiar Persona")
        print("2.- Cambiar Boletos")
        self.op = int(input("Ingrese una opcion: "))

    def nombre(self):
        self.nom = input("Ingrese el nombre: ")
    
    def personas(self):
        self.per = int(input("Ingrese el numero de personas: "))

    def boletos(self):
        self.bol = int(input("Ingrese el numero de boletos: "))
    
    def verificar(self):
        while self.bol > self.per * 7:
            print("Solo se permiten 7 boletos por persona.")
            self.menuEmergente()
            if self.op == 1:
                self.personas()
            elif self.op == 2:
                self.boletos()

    def calcular(self):
        self.total = self.bol * self.pre
        if self.bol > 5:
            self.total *= 0.85
        tarjeta = input("¿Cuentas con tarjeta CINECO? (s/n): ")
        if tarjeta.lower() == 's':
            self.total *= 0.90

    def corte(self):
        CorteTotal = sum([registro[1] for registro in self.registros])
        print(f"El costo total de todas las ventas es: {CorteTotal}")

    def escribir(self):
        with open("archivo.txt", "w") as file:
            file.write(f"Nombre: {self.nom}\n")
            file.write(f"Total: {self.total}\n")
            file.write("------------------------------\n")
        self.registros.append([self.nom, self.total])
    
    def run(self):
        self.nombre()
        self.personas()
        self.boletos()
        self.verificar()
        self.calcular()
        self.escribir()
    
    def main():
        cine = Cinepolis()
        while True:
            cine.menu()
            if cine.op == 1:
                cine.run()
            elif cine.op == 2:
                cine.corte()
                break

if __name__ == "__main__":
    Cinepolis.main()

