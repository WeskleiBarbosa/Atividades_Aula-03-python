
numero_final = int(input("Digite um número para contar até ele: "))
contador = 1
while contador <= numero_final:

    if contador % 2 != 0:
        print(contador)
    contador += 1

print("Contagem finalizada!")