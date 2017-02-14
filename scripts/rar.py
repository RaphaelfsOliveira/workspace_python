import os, subprocess
from datetime import date

def compress_file(path, src_arq):
        
    if src_arq in os.listdir(path):
        arq = src_arq[:src_arq.find('.')]
        cmd = '"C:\Program Files\WinRAR\Rar.exe" a ' + arq + ' ' + src_arq
        #subprocess.Popen(cmd, cwd=path) #mantem o processo e continua a função
        subprocess.run(cmd, cwd=path)
        if arq + '.rar' in os.listdir(path):
            return arq + '.rar'
    else:
        return '[ ERRO ]: Arquivo ' + src_arq + ' não está no diretório!'
        


if __name__ == "__main__":

    path = 'Z:\\backup\\'
    src_arq = 'Z:\\backup\\'

    # compress all files in dir
    # compress_file(path, file)
    for dit in os.listdir(path):
        print(dit)
        compress_file(path, dit)
        '''
        for files in os.listdir(path + dit + '\\'):
            #print(files)
            compress_file(path + dit + '\\', files)
      '''
            
            
        
        
        
        
    
