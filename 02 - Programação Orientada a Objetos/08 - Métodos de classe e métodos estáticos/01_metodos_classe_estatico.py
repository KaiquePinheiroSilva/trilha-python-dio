class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    @classmethod #recebe parametros da classe
    def criar_de_data_nascimento(cls, ano, mes, dia, nome):
        idade = 2022 - ano
        return cls(nome, idade)

    @staticmethod #não recebe parametros da classe mas "faz sentido" que esteja contida na clas
    def e_maior_idade(idade):
        return idade >= 18

    @staticmethod
    def qual_o_sexo(sexo):
        if sexo == "f":
            return "feminino" 
        else: 
            return "masculino"
        
p = Pessoa.criar_de_data_nascimento(1994, 3, 21, "Guilherme")
print(p.nome, p.idade)

print(Pessoa.e_maior_idade(18))
print(Pessoa.e_maior_idade(8))
print(Pessoa.qual_o_sexo("m"))