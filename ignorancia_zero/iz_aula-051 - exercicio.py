"""
A ACME Inc., uma empresa de 500 funcionários, está tendo problemas de espaço em
disco no seu servidor de arquivos. Para tentar resolver este problema, o
Administrador de Rede precisa saber qual o espaço ocupado pelos usuários, e
identificar os usuários com maior espaço ocupado. Através de um programa,
baixado da Internet, ele conseguiu gerar o seguinte arquivo, chamado
"usuarios.txt":

alexandre       456123789
anderson        1245698456
antonio         123456456
carlos          91257581
cesar           987458
rosemary        789456125

Neste arquivo, o nome do usuário possui 15 caracteres. A partir deste arquivo,
você deve criar um programa que gere um relatório, chamado "relatório.txt", no
seguinte formato:

ACME Inc.               Uso do espaço em disco pelos usuários
------------------------------------------------------------------------
Nr.  Usuário        Espaço utilizado     % do uso

1    alexandre       434,99 MB             16,85%
2    anderson       1187,99 MB             46,02%
3    antonio         117,73 MB              4,56%
4    carlos           87,03 MB              3,37%
5    cesar             0,94 MB              0,04%
6    rosemary        752,88 MB             29,16%

Espaço total ocupado: 2581,57 MB
Espaço médio ocupado: 430,26 MB

O arquivo de entrada deve ser lido uma única vez, e os dados armazenados em
memória, caso sejam necessários, de forma a agilizar a execução do programa.
A conversão da espaço ocupado em disco, de bytes para megabytes deverá ser feita
através de uma função separada, que será chamada pelo programa principal.
O cálculo do percentual de uso também deverá ser feito através de uma função,
que será chamada pelo programa principal.
"""

def armazenar_dados():
    arq = open('usuarios.txt', 'r')

    for text in arq.readlines():
        dados[text[:15].rstrip()] = text[15:].rstrip('\n').lstrip()

    arq.close()

def converter_mb():
    byte = 1048576

    for key in dados:
        dados[key] = int(dados[key]) / byte

def total_media():
    total = 0
    
    for key in dados:
        total += dados[key]

    media = total / len(dados)
    return total, media
        
def porcentagem_uso(dado):

    return (dado * 100) / total_media()[0]


def relatorio():
    i = 1
    arq = open('relatorio.txt', 'w')
    
    arq.writelines(['ACME Inc.               Uso do espaço em disco pelos usuários\n',
                    '------------------------------------------------------------------------\n',
                    'Nr.  Usuário        Espaço utilizado     % do uso\n\n'                    
                    ])
    
    for key in dados:
        arq.write('{i}    {k}  {d:>30} MB    {p:>.2%}\n'.format(i=i,k=key,d=dados[key],p=dados[key]/total_media()[0]))
        i+=1

    arq.writelines(['\nEspaço total ocupado: %0.2f MB\n' %(total_media()[0]),
                    'Espaço medio ocupado: %0.2f MB\n' %(total_media()[1]),                    
                    ])
    arq.close()

if __name__ == "__main__":

    dados = {}
    armazenar_dados()
    converter_mb()

    '''    
    for key in dados:
        print(key, dados[key], porcentagem_uso(dados[key]))
    '''
    relatorio()

    print('Executado')    
    
    

    
