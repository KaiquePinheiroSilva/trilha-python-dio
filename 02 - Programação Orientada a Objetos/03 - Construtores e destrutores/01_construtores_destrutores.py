class Cachorro:
    def __init__(self, nome, cor, acordado=True):
        print("Inicializando a classe...")
        self.nome = nome
        self.cor = cor
        self.acordado = acordado

    def __del__(self):
        print("Removendo a instância da classe.")
        print("it's over")

    def falar(self, acordado):
        if acordado:
            print("auau")
        else:
            print("a mimir")


def criar_cachorro():
    c = Cachorro("Zeus", "Branco e preto", False)
    print(c.nome)
    c.falar(c.acordado)

def criar_cachorro2():
    c = Cachorro("Jorge", "preto", True)
    print(c.nome)
    c.falar(c.acordado)

# c = Cachorro("Chappie", "amarelo")
# c.falar()

# print("Ola mundo")

# del c

print("Ola mundo")
print("Ola mundo")
print("Ola mundo")

criar_cachorro()
criar_cachorro2()

