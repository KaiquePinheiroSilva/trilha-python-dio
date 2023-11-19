salario = 2000

# listas são objetos imutáveis, e então são alterados mesmo por métodos em escopo local de funções

def salario_bonus(bonus, lista):
    global salario
    lista_2 = lista.copy()
    lista_2.append(2)
    salario += bonus
    print(lista_2)
    return salario

lista = [1]
salario_bonus(500, lista) # 2500
print(salario)
print(lista)