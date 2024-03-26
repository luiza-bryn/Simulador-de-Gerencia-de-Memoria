import time
import random
import pprint


def nru(num_quadros, lista_referencias):
    # ref/mod
    classes = {
        (0, 0): 0,
        (0, 1): 1,
        (1, 0): 2,
        (1, 1): 3,
    }

    tempo_inicial = time.time()

    page_faults = 0

    # chave = numero pagina, valor = lista com valor de referenciada/modifica, nessa ordem
    quadros = {}

    # chave = numero classe, valor = lista com as páginas com respectivo valor de classe
    class_dict = {
        0: [],
        1: [],
        2: [],
        3: [],
    }

    for ref in lista_referencias:
        if ref not in quadros.keys():
            page_faults += 1

            # testa numero maximo de quadros
            if len(quadros) == num_quadros:
                class_number = None
                if len(class_dict[0]) > 0:
                    class_number = 0
                elif len(class_dict[1]) > 0:
                    class_number = 1
                elif len(class_dict[2]) > 0:
                    class_number = 2
                else:
                    class_number = 3

                # pprint.pprint(class_dict)
                # pprint.pprint(quadros)

                random_page = random.choice(class_dict[class_number])
                # print(len(quadros), random_page, random_page in quadros.keys())
                class_dict[class_number].remove(random_page)
                quadros.pop(random_page)
            quadros[ref] = [0, 0]
            class_dict[0].append(ref)

        else:
            referenced = random.choice([True, False])
            modified = random.choice([True, False])

            new_class = classes[(int(referenced), int(modified))]
            old_class = classes[(quadros[ref][0], quadros[ref][1])]

            quadros[ref] = [int(referenced), int(modified)]
            class_dict[old_class].remove(ref)
            class_dict[new_class].append(ref)

    tempo_final = time.time()
    tempo_execucao = tempo_final - tempo_inicial
    tempo_execucao = round(tempo_execucao, 4)

    print(f"Tempo de execução: {tempo_execucao} segundos")

    return page_faults

# =====


# Leitura arquivo de testes 1
with open('input_teste1.txt', 'r') as file:
    linhas = file.readlines()

lista_referencias = [linha.strip() for linha in linhas[1:]]
num_quadros = int(linhas[0].strip())

# TESTE 1
print("=== TESTE 1.1 === ")
page_faults = nru(num_quadros, lista_referencias)
print(f"Houve {page_faults} page faults!")

# Leitura arquivo de testes 2
with open('input_teste2.txt', 'r') as file:
    linhas = file.readlines()

lista_referencias = [linha.strip() for linha in linhas[1:]]
num_quadros = int(linhas[0].strip())

# TESTE 2
print("=== TESTE 1.2 === ")
page_faults = nru(num_quadros, lista_referencias)
print(f"Houve {page_faults} page faults!")

# Leitura arquivo de testes 2.1
with open('input2_teste1.txt', 'r') as file:
    linhas = file.readlines()

lista_referencias = [linha.strip() for linha in linhas[1:]]
num_quadros = int(linhas[0].strip())

# TESTE 1
print("=== TESTE 2.1 === ")
faults = nru(num_quadros, lista_referencias)
print(f"Houve {faults} page faults!")


# Leitura arquivo de testes 2.2
with open('input2_teste2.txt', 'r') as file:
    linhas = file.readlines()

lista_referencias = [linha.strip() for linha in linhas[1:]]
num_quadros = int(linhas[0].strip())

# TESTE 2
print("=== TESTE 2.2 === ")
faults = nru(num_quadros, lista_referencias)
print(f"Houve {faults} page faults!")
