import time

def relogio(num_quadros, lista_referencias):
    tempo_inicial = time.time()

    page_faults = 0

    quadros = {} #a chave é o num da página e o valor é o bit R

    for ref in lista_referencias:
        if ref not in quadros.keys():
            page_faults += 1
            if len(quadros) == num_quadros:
                find_zero = False
                ponteiro = 0
                while find_zero == False:
                    lista_chaves = list(quadros.keys())             
                    chave = lista_chaves[ponteiro]

                    if quadros[chave] == 0:
                        del quadros[chave]
                        find_zero = True
                        break

                    else:
                        quadros[chave] = 0

                        if ponteiro == num_quadros - 1:
                            ponteiro = 0

                        else:
                            ponteiro += 1
        quadros[ref] = 1

    tempo_final = time.time()
    tempo_execucao = tempo_final - tempo_inicial
    tempo_execucao = round(tempo_execucao, 4)

    print(f"Tempo de execução: {tempo_execucao} segundos")

    return page_faults

# =====

#Leitura arquivo de testes 1
with open('input_teste1.txt', 'r') as file:
    linhas = file.readlines()

lista_referencias = [linha.strip() for linha in linhas[1:]]
num_quadros = int(linhas[0].strip()) 

#TESTE 1
print("=== TESTE 1.1 === ")
page_faults = relogio(num_quadros, lista_referencias)
print(f"Houve {page_faults} page faults!")

#Leitura arquivo de testes 2
with open('input_teste2.txt', 'r') as file:
    linhas = file.readlines()

lista_referencias = [linha.strip() for linha in linhas[1:]]
num_quadros = int(linhas[0].strip()) 

#TESTE 2
print("=== TESTE 1.2 === ")
page_faults = relogio(num_quadros, lista_referencias)
print(f"Houve {page_faults} page faults!")

#Leitura arquivo de testes 2.1
with open('input2_teste1.txt', 'r') as file:
    linhas = file.readlines()

lista_referencias = [linha.strip() for linha in linhas[1:]]
num_quadros = int(linhas[0].strip()) 

#TESTE 1
print("=== TESTE 2.1 === ")
faults = relogio(num_quadros, lista_referencias)
print(f"Houve {faults} page faults!")


#Leitura arquivo de testes 2.2
with open('input2_teste2.txt', 'r') as file:
    linhas = file.readlines()

lista_referencias = [linha.strip() for linha in linhas[1:]]
num_quadros = int(linhas[0].strip()) 

#TESTE 2
print("=== TESTE 2.2 === ")
faults = relogio(num_quadros, lista_referencias)
print(f"Houve {faults} page faults!")