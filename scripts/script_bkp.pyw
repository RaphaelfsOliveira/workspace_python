import os, subprocess, pyodbc, shutil
from datetime import date
#time.sleep(60)

#### backup file

def compress_rename_file(path, dst_path, src_arq):
    dst_arq = src_arq[:src_arq.find('.')] + date.today().strftime('%d-%m-%y') + src_arq[src_arq.find('.'):]
    
    if src_arq in os.listdir(path):
        os.rename( path + src_arq, path + dst_arq)
        if dst_arq in os.listdir(path):
            arq = dst_arq[:dst_arq.find('.')]
            cmd = '"C:\Program Files\WinRAR\Rar.exe" a ' + arq + ' ' + dst_arq
            #subprocess.Popen(cmd, cwd=path) #mantem o processo e continua a função
            subprocess.run(cmd, cwd=path)
            if arq + '.rar' in os.listdir(path):
                return arq + '.rar'
    else:
        return '[ ERRO ]: Arquivo ' + src_arq + ' não está no diretório!'
        

### make dirs and move file
    
def make_dir_bkp(path, dst_path, dst_arq):
    mes = ('janeiro','fevereiro','março','abril','maio','junho',
           'julho','agosto','setembro','outubro','novembro','dezembro')

    if date.today().strftime('%Y') not in os.listdir(dst_path):
        os.mkdir(dst_path + date.today().strftime('%Y') + dst_path[dst_path.find('\\')])
    dst_path = dst_path + date.today().strftime('%Y') + dst_path[dst_path.find('\\')]

    if mes[int(date.today().strftime('%m')) - 1].capitalize() not in os.listdir(dst_path):
        os.mkdir(dst_path + mes[int(date.today().strftime('%m')) - 1].capitalize() + dst_path[dst_path.find('\\')])
    dst_path = dst_path + mes[int(date.today().strftime('%m')) - 1].capitalize() + dst_path[dst_path.find('\\')]

    shutil.move(path + dst_arq, dst_path + dst_arq)


#### backup Database

def bkp_database(srv, db_bkp, path_bkp_db):
    conn = pyodbc.connect(driver='{ODBC Driver 13 for SQL Server}',
                          server=srv,
                          database=db_bkp,
                          trusted_connection='yes',
                          autocommit=True)
    
    sql_query = "BACKUP DATABASE " + db_bkp + " TO DISK ='" + path_bkp_db + "' WITH FORMAT"
    cursor = conn.cursor().execute(sql_query)
    while cursor.nextset():
        pass
    conn.close()




if __name__ == "__main__":

    # database bkp Refeitorio    
    db_bkp = 'XXXX_XX' #database for backup
    path_bkp_db = 'C:/Program Files/Microsoft SQL Server/MSSQL10_50.SQLEXPRESS/MSSQL/Backup/backup/XXX.bak' # backup stay here
    srv = 'XXXXX\SQLEXPRESS' #database server
    bkp_database(srv, db_bkp, path_bkp_db)


    #armazenar backup Refeitorio
    path = 'Y:\\backup\\'
    dst_path = 'D:\\backup\\'
    src_arq = 'XX.bak'
    make_dir_bkp(path, dst_path, compress_rename_file(path, dst_path, src_arq))


    #armazenar backup CMnet
    path = 'D:\\Backup Full\\'
    dst_path = 'D:\\Backup Compact\\'
    src_arq = 'XX.bak'
    make_dir_bkp(path, dst_path, compress_rename_file(path, dst_path, src_arq))
    



