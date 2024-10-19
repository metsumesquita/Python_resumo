# Definição do dicionário de produtos e listas de itens
produtos = {
    "Bebidas": ["coca", "cha mate", "agua", "chocolate quente"],
    "Comida": ["bolo", "file com fritas", "chocolate"],
    "Custo_Bebidas": [5.0, 2.4, 0.5, 2],
    "Custo_Comida": [10, 20, 5.3]
}

bebidas_list = produtos["Bebidas"]
alimentos_list = produtos["Comida"]

custoC_list = produtos["Custo_Comida"]
custoB_list = produtos["Custo_Bebidas"]

# Função para exibir os produtos disponíveis
def exibir_produtos():
    print("Produtos disponíveis:")
    print("Lista de Bebidas:")
    for i, bebida in enumerate(bebidas_list):
        print(f"{i + 1}. {bebida} - R${produtos['Custo_Bebidas'][i]:.2f}")
    print("Lista de Comida:")
    for i, comida in enumerate(alimentos_list):
        print(f"{i + 1}. {comida} - R${produtos['Custo_Comida'][i]:.2f}")

# Função para obter a posição do item na lista de bebidas
def itemPosiçãoB(item):
    achou = False
    i = 0
    while i < len(bebidas_list):
        if bebidas_list[i] == item:
            achou = True
            break
        i += 1
    if achou:
        return i
    else:
        return -1

# Função para obter a posição do item na lista de alimentos
def itemPosiçãoC(item):
    achou = False
    i = 0
    while i < len(alimentos_list):
        if alimentos_list[i] == item:
            achou = True
            break
        i += 1
    if achou:
        return i
    else:
        return -1
    
# Função para calcular o preço da bebida com base na quantidade
def calcular_preço_bebida(posição):
    qtd = int(input("Informe a quantidade do item que você deseja: "))
    valor = custoB_list[posição] * qtd
    return valor

# Função para calcular o preço da comida com base na quantidade
def calcular_preço_comida(posição):
    qtd = int(input("Informe a quantidade do item que você deseja: "))
    valor = custoC_list[posição] * qtd
    return valor

# Saudação inicial
print("Seja bem-vindo à loja")
exibir_produtos()

# Obtenção da opção do usuário
opçãolista = int(input("Selecione 1 para selecionar algum item da lista de bebidas disponíveis\nSelecione 2 para selecionar algum item da lista de alimentos disponíveis\nSelecione 0 para sair do menu: "))

if opçãolista == 1:
    escolhido = input("Informe por escrito qual o nome do item selecionado: ")
    posição = itemPosiçãoB(escolhido)
    if posição != -1:
        totalB = calcular_preço_bebida(posição)
        print(f"O valor total para {escolhido} é: R${totalB:.2f}")
    else:
        print("Item não encontrado na lista de bebidas.")
        
elif opçãolista == 2:
    escolhido = input("Informe por escrito qual o nome do item selecionado: ")
    posição = itemPosiçãoC(escolhido)
    if posição != -1:
        totalC = calcular_preço_comida(posição)
        print(f"O valor total para {escolhido} é: R${totalC:.2f}")
    else:
        print("Item não encontrado na lista de alimentos.")

elif opçãolista == 0:
    print("Obrigado por visitar nossa loja. Até logo!")

else:
    print("Opção inválida. Por favor, selecione uma opção válida.")

