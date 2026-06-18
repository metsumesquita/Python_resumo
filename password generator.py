import string
import random
lista_letras_lower=list(string.ascii_lowercase)
lista_numeros=list(string.digits)
lista_special=list(string.punctuation)
lista_letras_upper=list(string.ascii_uppercase)

tamanho_senha = int(input("Qual o tamanho total da senha? "))
qtd_especial = int(input("Quantos símbolos especiais sua senha terá? "))
qtd_numeros = int(input("Quantos números sua senha terá? "))
qtd_letra_alta = int(input("Quantas letras maiúsculas sua senha terá? "))
qtd_letra_baixa = int(input("Quantas letras minúsculas sua senha terá? "))

soma_caracteres = qtd_especial + qtd_numeros + qtd_letra_alta + qtd_letra_baixa
if soma_caracteres != tamanho_senha:
    print(f"\n[Aviso]: A soma dos caracteres ({soma_caracteres}) é diferente do tamanho total pedido ({tamanho_senha}).")
    tamanho_senha = soma_caracteres # Ajusta o tamanho total para corresponder à soma real
senha=[]

while qtd_especial>0:
  especial_radom=random.choice(lista_special)
  senha.append(especial_radom)
  qtd_especial-=1

while qtd_numeros>0:
  numero_random=random.choice(lista_numeros)
  senha.append(numero_random)
  qtd_numeros-=1

while qtd_letra_alta>0:
  letra_alta_random=random.choice(lista_letras_upper)
  senha.append(letra_alta_random)
  qtd_letra_alta-=1

while qtd_letra_baixa>0:
  letra_baixa_random=random.choice(lista_letras_lower)
  senha.append(letra_baixa_random)
  qtd_letra_baixa-=1

random.shuffle(senha)
senha="".join(senha)

print("A sua senha final é :"+senha)
