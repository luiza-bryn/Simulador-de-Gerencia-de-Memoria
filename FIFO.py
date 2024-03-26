import time

def fifo_page(blocos, paginas):
    tempo_inicial = time.time()

    tab_pag = {}  # Dicionário para representar a página e seu bit de presença
    pag_fila = []  # Fila para manter a ordem das páginas

    page_faults = 0  # Contador de page faults

    for pag in paginas:
        pag = int(pag)
        if pag not in tab_pag:  # Se a página não está na tabela de páginas
            if len(pag_fila) < blocos:  # Se ainda houver blocos disponíveis
                tab_pag[pag] = 1  # Define o bit de presença como 1 (alocada)
                pag_fila.append(pag)  # Adiciona a página na fila
                page_faults += 1 
            else:
                # Remove a primeira página adicionada (FIFO)
                pag_removida = pag_fila.pop(0)
                tab_pag.pop(pag_removida)  # Remove da tabela de páginas

                # Adiciona a nova página no final da fila e na tabela de páginas
                pag_fila.append(pag)
                tab_pag[pag] = 1
                page_faults += 1  # Incrementa o contador de page faults
    
    tempo_final = time.time()
    tempo_execucao = tempo_final - tempo_inicial
    tempo_execucao = round(tempo_execucao, 4)

    print(f"Tempo de execução: {tempo_execucao} segundos")

    return page_faults

# Leitura do arquivo de entrada 1
with open('input_teste1.txt', 'r') as file:
    linhas = file.readlines()

blocos = int(linhas[0].strip())  # Primeira linha contém o número de blocos
paginas = [linha.strip() for linha in linhas[1:]]  # Restante das linhas são as páginas

#TESTE 1
print("=== TESTE 1.1 === ")
page_faults_total = fifo_page(blocos, paginas)
print("Total de page faults gerados:", page_faults_total)


# Leitura do arquivo de entrada 2
with open('input_teste2.txt', 'r') as file:
    linhas = file.readlines()

blocos = int(linhas[0].strip())  # Primeira linha contém o número de blocos
paginas = [linha.strip() for linha in linhas[1:]]  # Restante das linhas são as páginas

#TESTE 2
print("=== TESTE 1.2 === ")
page_faults_total = fifo_page(blocos, paginas)
print("Total de page faults gerados:", page_faults_total)


#Leitura arquivo de testes 1
with open('input2_teste1.txt', 'r') as file:
    linhas = file.readlines()

blocos = int(linhas[0].strip())  # Primeira linha contém o número de blocos
paginas = [linha.strip() for linha in linhas[1:]]  # Restante das linhas são as páginas


#TESTE 1
print("=== TESTE 2.1 === ")
page_faults_total = fifo_page(blocos, paginas)
print("Total de page faults gerados:", page_faults_total)


#Leitura arquivo de testes 2.2
with open('input2_teste2.txt', 'r') as file:
    linhas = file.readlines()

blocos = int(linhas[0].strip())  # Primeira linha contém o número de blocos
paginas = [linha.strip() for linha in linhas[1:]]  # Restante das linhas são as páginas


#TESTE 2
print("=== TESTE 2.2 === ")
page_faults_total = fifo_page(blocos, paginas)
print("Total de page faults gerados:", page_faults_total)