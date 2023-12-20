class Bicicleta:
    def __init__(self, cor, modelo, ano, valor, nro_marcha):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor
        self.nro_marcha = nro_marcha

    def buzinar(self):
        print("Plim plim...")

    def parar(self):
        print(f"Parando bicicleta {self.modelo}...")
        print("Bicicleta parada!")

    def trocar_marcha(self, nro_marcha):
        _self = self.nro_marcha

        if _self < nro_marcha:
            print("trocou a marcha")
        else:
            print("não trocou a marcha") 

    def correr(self):
        print("Vrummmmm...")

    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"


b1 = Bicicleta("vermelha", "caloi", 2022, 600, 5)
b1.buzinar()
b1.correr()
b1.parar()
b1.trocar_marcha(10)
print(b1.cor, b1.modelo, b1.ano, b1.valor)

b2 = Bicicleta("verde", "monark", 2000, 189, 5)
print(b2)
b2.correr()
