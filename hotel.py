class Acomodacao:

    contador = 0

    def __init__(self, tipo, preco, camas, dias):
        Acomodacao.contador += 1
        self.tipo = tipo
        self.preco = preco
        self.camas = camas
        self.dias = dias
        
    def calc_total(preco, dias):
        return preco * dias
    



class suite(Acomodacao):
    def calc_total(dias):
        return 400 * dias

class quartoStandard(Acomodacao):
    def calc_total(dias):
        return 200 * dias
    
class quartoDeluxe(Acomodacao):
    def calc_total(dias):
        return 300 * dias
    

    class Hotel(Acomodacao):
        def __init__(self):
            self.reservas = []

            def listaReserva(self, reservas):
                self.reservas.append(contador)

