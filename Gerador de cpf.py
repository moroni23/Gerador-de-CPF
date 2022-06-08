from random import randint
numero = str(randint(100000000, 999999999))
novo_cpf = numero     # Elimina os dois ultimos digitos do cpf
total = 0
reverso = 10          # Contador Reverso
for index in range(19):
    if index > 8:     # Primeiro Indice vai de 0 a 9
        index -= 9    # São os 9 primeiros digitos do CPF
    total += int(novo_cpf[index]) * reverso   # Valor Total da multiplicação

    reverso -= 1      # Descrementa o contador reverso
    if reverso < 2:
        reverso = 11
        d = 11 - (total % 11)

        if d > 9:
            d = 0

        total = 0
        novo_cpf += str(d)
print(novo_cpf)