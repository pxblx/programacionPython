import re

class Terminal(object):
    def __init__(self, numero):
        self.set_numero(numero)
        self.tiempo = 0

    def set_numero(self, numero):
        re_numero = re.compile("[0-9]{3} [0-9]{2} [0-9]{2} [0-9]{2}")
        if re_numero.match(numero):
            self.numero = numero

    def llama(self, terminal, tiempo):
        self.tiempo = self.tiempo + tiempo
        terminal.tiempo = terminal.tiempo + tiempo

    def __str__(self):
        return "Nº " + self.numero +" - " + str(self.tiempo) + "s de conversación"
