def mergesort(vetor,inicio,fim):
    if (fim - inicio > 1):
        meio = (inicio + fim)//2
        mergesort(vetor,inicio,meio)
        mergesort(vetor,meio,fim)
        merge(vetor,inicio,meio,fim)
    else:
        return vetor

def merge(vetor,inicio,meio,fim):
    esquerda = vetor[inicio:meio]
    direita = vetor[meio:fim]
    L,R = 0,0
    for contador in range(inicio,fim):
        if(L >= len(esquerda) ):
            vetor[contador] = direita[R]
            R += 1
        elif (R >= len(direita)):
            vetor[contador] = esquerda[L]
            L += 1
        elif(esquerda[L] < direita[R] ):
            vetor[contador] = esquerda[L]
            L += 1
        else:
            vetor[contador] = direita[R]
            R += 1


vetor1 = [34,31,2,13,27,8,67]
print(vetor1)
mergesort(vetor1,0,len(vetor1)-1)
print(vetor1)
