from main_stu import lista, produtos, pessoas

nova_lista = filter(lambda x: x > 5, lista)
print(list(nova_lista))

print('===================================================================')

def filtrar(produto):
    if produto['preco'] > 50:
        return True
    else:
        return False

novo_produto = filter(filtrar, produtos)

for produto in novo_produto:
    print(produto)

print('===================================================================')

def buscar(pessoa):
    if pessoa['idade'] >= 18:
        return True
    else:
        False


nova_idade = filter(buscar, pessoas)

for idade in nova_idade:
    print(idade)