# I. troca
# seja uma string s
# se s tiver tamanho <= 1 retorna ela mesma
# caso contrário troca a primeira e última letra
# troca('code') -> 'eodc'
# troca('a') -> 'a'
# troca('ab') -> 'ba'
def troca(s):
  word = str()
  if len(s) <= 1:
      return s
  else:
      for l in range(len(s)):
          if l == 0:
              word += s[len(s) - 1]
          elif l == len(s) - 1:
              word += s[0]
          else:
              word += s[l]
  return word
              
  





