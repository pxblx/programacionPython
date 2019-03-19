from src.practica04.E08.Terminal import Terminal


class Movil(Terminal):
    def __init__(self, numero, tarifa):
        super().__init__(numero)
        self.__tarifa = tarifa
        self.__gastado = 0

    def llama(self, terminal, tiempo):
        self.tiempo = self.tiempo + tiempo
        terminal.tiempo = terminal.tiempo + tiempo

        if self.__tarifa == "rata":
            self.__gastado = self.__gastado + tiempo * 0.001
        elif self.__tarifa == "mono":
            self.__gastado = self.__gastado + tiempo * 0.002
        elif self.__tarifa == "bisonte":
            self.__gastado == self.__gastado + tiempo * 0.005
        else:
            self.__gastado = 0

    def __str__(self):
        return "Nº " + self.numero +" - " + str(self.tiempo) + "s de conversación - tarificados " + '{0:.2f}'.format(self.__gastado) + " euros"
