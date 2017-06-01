import socket
import configparser

#config project
config = configparser.ConfigParser()
config.read_file(open('cli_config.ini'))
HOST = config['DEFAULT']['host']
PORT = int(config['DEFAULT']['port'])

#log_file
def logs_path(path_log, log_file):
    if not os.path.isdir(str(path_log)):
        os.mkdir(path_log)
    log = open(os.path.join(path_log, str(log_file) + '.txt'), 'a')
    log.write(datetime.now().strftime('%Y-%m-%d - %H:%M:%S ') + str(e) + '\n')
    log.close()



#start project
cli_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cli_socket.connect((HOST, PORT))

while True:
    try:
        data = cli_socket.recv(256).decode('ascii')
        print(data)
    except Exception as e:
        logs_path('Logs', 'log_cli_socket')

cli_socket.close()
