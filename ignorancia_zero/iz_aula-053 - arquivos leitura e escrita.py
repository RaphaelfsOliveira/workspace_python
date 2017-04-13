#  V*u **r***** c** *g*****c*a **ro

def gera_dicionario():
    arq = open('PALAVRAS.txt', 'r')

    dic = []

    print('carregando palavras para o dicionario...')
    for p in arq:
        sep = p.split('\n')
        print(sep)
        dic.append(sep)

    # dic.sort() # coloca em ordem alfabetica

    return dic


def receba_frase():

    while True:
        frase = input('digite a frase usando * para caracteres desconhecidos\n')
        ok = True
        for c in frase:
            if not 'a' <= c <= 'z' and not'A' <= c <= 'Z' and c != '*' and c != ' ':
                ok = False
                break
        if ok:
            return frase
        else:
            print('Digite letras sem acento e nenhum ç!')


def procura_palavra(dic, pa):

    pa = pa.upper()

    if pa[0] != '*':
        for i in range(len(dic)):
            if i % 100 == 0:
                print('procurando letra no dicionario...')
            if dic[i][0] == pa[0]:
                break

        for j in range(i, len(dic)):
            if j % 100:
                print('procurando letra no dicionario...')
            if dic[j][0] != pa[0]:
                break

        return separa_por_tamanho(dic[i:j], pa)
    else:
        return separa_por_tamanho(dic, pa)
    


def separa_por_tamanho(dic, pa):

    dim = len(pa)

    candidatos = []

    for word in dic:
        if dim == len(word):
            e_candidata = True
            for i in range(dim):
                if pa[i] != '*' and pa[i] != word[i]:
                    e_candidata = False
                    break

            if e_candidata:
                print('adicionando palavra candidata..')
                candidatos.append(word)

    return candidatos


def gera_frases_possiveis(candidatas_totais):

    aux = open('auxiliar.py', 'w')
    aux.write('def funcao_auxiliar(pa_totais):\n')
    aux.write('\tarquivo = open("FRASE.txt", "w")\n')
 
    aux.write('\tfrase = []\n')
    aux.write('\tfor i in range(len(pa_totais)):\n')
    aux.write('\t\tfrase.append("")\n')
 
    for i in range(len(candidatas_totais)):
        linha = '\t'*(i+1)
        linha += 'for a%i in range(len(pa_totais[%i])):\n'%(i,i)
        aux.write(linha)
        linha = '\t'*(i+2) + 'frase[%i]= pa_totais[%i][a%i]\n'%(i,i,i)
        aux.write(linha)
 
    aux.write('\t'*(i+2) + 'frase_s = ""\n')
    aux.write('\t'*(i+2) + 'for palavra in frase:\n')
    aux.write('\t'*(i+3)+ 'frase_s += palavra\n')
    aux.write('\t'*(i+3)+ 'frase_s += " "\n')
    aux.write('\t'*(i+2) + 'arquivo.write(frase_s + "\\n")\n')
 
    aux.write('\tarquivo.close()')
 
    aux.close()
 
    print("Gerando Lista de Palavras Candidatas...")
     
    from auxiliar import funcao_auxiliar
 
    funcao_auxiliar(candidatas_totais)     




if __name__ == '__main__':

    dic = gera_dicionario()
    frase = receba_frase().split()

    candidatas_totais = []

    for pa in frase:
        candidatas_totais.append(procura_palavra(dic, pa))

    gera_frases_possiveis(candidatas_totais)

    print('operações encerradas')


        
    

