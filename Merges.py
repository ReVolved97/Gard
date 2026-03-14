# ==========================================================
# MERGESORT — Estratégia Dividir e Conquistar
# ==========================================================
# O MergeSort é um algoritmo de ordenação baseado na estratégia
# "Dividir e Conquistar".
#
# A ideia é:
# 1) Dividir a lista em partes menores
# 2) Ordenar cada parte recursivamente
# 3) Combinar as partes ordenadas
#
# Complexidade:
# Tempo -> O(n log n)
# Espaço -> O(n)
# ==========================================================


def merge_sort(lista):

    # ------------------------------------------------------
    # CASO BASE DA RECURSÃO
    # ------------------------------------------------------
    # Se a lista tiver 0 ou 1 elemento, ela já está ordenada.
    # Portanto retornamos a própria lista.
    if len(lista) <= 1:
        return lista


    # ------------------------------------------------------
    # DIVISÃO DA LISTA
    # ------------------------------------------------------
    # Encontramos o índice do meio da lista
    meio = len(lista) // 2


    # ------------------------------------------------------
    # CONQUISTAR (RESOLVER SUBPROBLEMAS)
    # ------------------------------------------------------
    # Chamamos a função recursivamente para ordenar
    # a metade esquerda e a metade direita.

    esq = merge_sort(lista[:meio])     # metade esquerda
    dir = merge_sort(lista[meio:])     # metade direita


    # ------------------------------------------------------
    # COMBINAR (MERGE)
    # ------------------------------------------------------
    # Depois que as duas metades estão ordenadas,
    # precisamos juntá-las em uma única lista ordenada.

    return merge(esq, dir)



def merge(esq, dir):

    # ------------------------------------------------------
    # LISTA QUE GUARDARÁ O RESULTADO FINAL
    # ------------------------------------------------------
    resultado = []


    # ------------------------------------------------------
    # DOIS PONTEIROS PARA PERCORRER AS LISTAS
    # ------------------------------------------------------
    # i percorre a lista esquerda
    # j percorre a lista direita
    i = 0
    j = 0


    # ------------------------------------------------------
    # COMPARAÇÃO DOS ELEMENTOS
    # ------------------------------------------------------
    # Enquanto houver elementos nas duas listas,
    # comparamos os valores atuais.

    while i < len(esq) and j < len(dir):

        # Se o elemento da esquerda for menor
        if esq[i] <= dir[j]:

            # adicionamos ele no resultado
            resultado.append(esq[i])

            # avançamos o ponteiro da esquerda
            i += 1

        else:

            # caso contrário adicionamos o da direita
            resultado.append(dir[j])

            # avançamos o ponteiro da direita
            j += 1


    # ------------------------------------------------------
    # ELEMENTOS RESTANTES
    # ------------------------------------------------------
    # Quando uma das listas termina,
    # os elementos restantes da outra já estão ordenados.

    return resultado + esq[i:] + dir[j:]



# ==========================================================
# EXEMPLO DE EXECUÇÃO
# ==========================================================

nums = [38, 27, 43, 3, 9, 82, 10]

print("Lista original:", nums)

ordenada = merge_sort(nums)

print("Lista ordenada:", ordenada)

# Saída esperada:
# [3, 9, 10, 27, 38, 43, 82]