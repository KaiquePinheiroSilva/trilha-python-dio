class CoisasQueVoam:
    def voar(self):
        print("Voando...")


class Pardal(CoisasQueVoam):
    def voar(self):
        print("Pardal pode voar")
        return super().voar()


class Avestruz(CoisasQueVoam):
    def voar(self):
        print("Avestruz não pode voar")
        


# NOTE: exemplo ruim do uso de herança para "ganhar" o método voar
        # NOTE: incongruência consertado mudando o nome da classe de Passaros para CoisasQueVoam
class Aviao(CoisasQueVoam):
    def voar(self):
        print("Avião está decolando...")
        return super().voar()

def plano_voo(obj):
    obj.voar()

p1 = Pardal()
p2 = Avestruz()
p3 = Aviao()

plano_voo(p1)
plano_voo(p2)
plano_voo(p3)

Pardal().voar()