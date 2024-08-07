# lista
nomes = ['Fulano', 'Ciclano', 'Beltrano', 'João', 'Maria', 'José']

# exibir a lista e seus respectivos indices
for i in range(len(nomes)):
    print(f'Índice {i}: {nomes[i]}.')
    #quebra de linha
print('\n')

# usuário o informa o indice
try:
    indice = int(input('Informe o número do indice: '))

    #faz a alteração
    nomes[indice] = input('Infome o novo nome: \n').capitalize()

except:
    print('Não foi possível fazer a alteração.')
print('\n')
# exibe a nova lista
for i in range(len(nomes)):
    print(f'Índice {i}: {nomes[i]}.')
print('\n')