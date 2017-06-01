import os
from datetime import datetime

# Global
def logs_path(path_log, log_file):
    if not os.path.isdir(str(path_log)):
        os.mkdir(path_log)
    log = open(os.path.join(path_log, str(log_file) + '.txt'), 'a')
    log.write(datetime.now().strftime('%Y-%m-%d - %H:%M:%S ') + str(e) + '\n')
    log.close()


try:
    log = open('/tmp/log.txt', 'a')
    log.write('test\n')
    log.close()

except Exception as e:
    logs_path('Logs', 'log')
    '''
    path_log = 'Logs'
    if not os.path.isdir(path_log):
        os.mkdir(path_log)

    log_file = 'log.txt'
    log = open(os.path.join(path_log, log_file), 'a')
    log.write(datetime.now().strftime('%Y-%m-%d - %H:%M:%S ') + str(e) + '\n')
    log.close()
    '''






print(datetime.now().isoformat(timespec='seconds'))
print(datetime.now().strftime('%Y-%m-%d - %H:%M:%S'))
print(os.listdir())


'''
if not os.path.isdir(path_log):
    os.mkdir(path_log)
'''
#os.path.join(path_log)
