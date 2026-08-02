print('Conversor de Tempo - Minutos em Horas')

minutos_para_converter = 234 # Insira aqui os minutos para conversão

# Parte 1 - Descobrir o número de horas
# Encontra a versão decimal do número de horas e obtém o número inteiro de horas convertendo para um tipo inteiro

horas_decimal = minutos_para_converter / 60 # 1 hora tem 60 min 
horas_parte = int(horas_decimal) # Armazena o número de horas convertidas em número inteiro 

# Parte 2 - Descobrir o número de minutos
# Usa o resto da divisão do número de minutos por 60 para obter os minutos inteiros

minutos_parte = minutos_para_converter % 60 # O resto indica o número de minutos restantes

# Parte 3
# Imprime os resultados

print('Horas')
print(horas_parte)
print('Minutos')
print(minutos_parte)