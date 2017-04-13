
# Desafio Nama_Team

def nama_team(dim):
    i = 1
    while i < dim:
        out = ''
        if i % 5 == 0:
            out += 'Nama '
        if i % 7 == 0:
            out += 'Team'
        if out == '':
            out = i

        print(out)
        i += 1

if __name__ == '__main__':
    nama_team(int(input('Digite um numero: ')))
        
        
