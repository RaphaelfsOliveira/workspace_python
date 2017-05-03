import telebot
import configparser
import urllib.request
import requests

#config Jarvis
config = configparser.ConfigParser()
config.read_file(open('jarvis_config.ini'))
TOKEN = config['DEFAULT']['token']

#start Jarvis
bot = telebot.TeleBot(TOKEN)

#file_info = bot.get_file(file_id=)
#file = requests.get('https://api.telegram.org/file/bot{0}/{1}'.format(TOKEN, file_info.file_path))

event_title, event_text = '', ''

@bot.message_handler(commands=['start', 'help'])
def send_welcome(msg):
    username = msg.from_user.first_name
    print(msg)
    bot.reply_to(msg, 'Olá, '+ username +' seja bem vindo!!')
    bot.send_location(msg.chat.id, latitude=13.7, longitude=12.3)

    markup = telebot.types.ReplyKeyboardMarkup()
    itembtna = telebot.types.KeyboardButton('1')
    itembtnb = telebot.types.KeyboardButton('2')
    itembtnc = telebot.types.KeyboardButton('3')
    itembtnd = telebot.types.KeyboardButton('4')
    itembtne = telebot.types.KeyboardButton('5')
    itembtnf = telebot.types.KeyboardButton('6')
    markup.row(itembtna, itembtnb, itembtnc)
    markup.row(itembtnd, itembtne, itembtnf)
    bot.send_message(msg.chat.id, "Choose one letter:", reply_markup=markup)


@bot.message_handler(commands=['dominar_mundo'])
def dominar_mundo(msg):
    bot.send_message(msg.chat.id, 'Como gostaria de dominar o mundo senhor ?')


@bot.message_handler(commands=['add'])
def add_post(msg):
    print('\nFunc = /add: ', msg.text, '\n')
    try:
        markup = telebot.types.ForceReply(selective=True)
        bot.send_message(msg.chat.id, "Titulo do Evento:", reply_markup=markup)
        bot.register_next_step_handler(msg, post_title)
    except Exception as error:
        print(error)

def post_title(msg): #recebe o titulo do evento na msg
    print('\nFunc = Post Title: ', msg.text, '\n', msg)
    try:
        msg.reply_to_message.text == "Titulo do Evento:"
        global event_title
        event_title = msg.text
        markup = telebot.types.ForceReply(selective=True)
        bot.send_message(msg.chat.id, "Sobre o Evento:", reply_markup=markup)
        bot.register_next_step_handler(msg, post_text)
    except Exception as error:
        print('\nFatal Error: ooops rs... post sem titulo\n')

def post_text(msg): #recebe o texto do evento na msg
    print('\nFunc = Post Text: ', msg.text, '\n', msg)
    try:
        msg.reply_to_message.text == "Sobre o Evento:"
        global event_text
        event_text = msg.text
        markup = telebot.types.ForceReply(selective=True)
        bot.send_message(msg.chat.id, "Receber Fotos:", reply_markup=markup)
        bot.register_next_step_handler(msg, post_photo)
    except Exception as error:
        print('\nTextal Error: hehe foi mal ...post sem texto\n')

def post_photo(msg):  #recebe as fotos do evento
    try:
        msg.reply_to_message.text == "Receber Fotos:"
        global event_title, event_text
        print('\nFunc = Post Photo: ', msg.text, '\n', msg)
        bot.send_message(msg.chat.id, 'Titulo do Post: %s \nTexto do Post: %s' %(event_title, event_text))
        print()
    except Exception as error:
        print('\nPhotal Error: esqueceram de tirar as fotos ... \n')

'''
@bot.message_handler(func=lambda msg: 'grupo' in msg.text.lower() or\
                                      'canal' in msg.text.lower())
def echo_keyword(msg):
    # msg.text.lower() == 'grupo' or msg.text.lower() == 'canal'
    print()
    print('Func = Grupo ou Canal')
    print(msg.text)

    bot.send_message(msg.chat.id, '#Test_ForceReply')
    markup = telebot.types.ForceReply(selective=True)
    msg_canalgrupo = "Talvez seja esse Canal/Grupo de TI que você está procurando\
    fique a vontade para entrar e explorar"
    bot.send_message(msg.chat.id, msg_canalgrupo, reply_markup=markup)


@bot.message_handler(func=lambda msg: 'oi' in msg.text.lower() or\
                                      'jarvis' in msg.text.lower() or\
                                      'olá' in msg.text.lower())
def echo_test(msg):
    bot.send_message(msg.chat.id, 'Olá como é seu nome ??')
    print(msg)
    bot.register_next_step_handler(msg, reply_name)

def reply_name(msg):
    bot.send_message(msg.chat.id, 'Olá '+ msg.text +' meu nome é Jarvis seja bem vindo!!..')
'''


@bot.message_handler(content_types=['document'], func=lambda msg: True)
def echo_document(msg):
    try:
        print()
        print('Func = Todas as Mensagens: ', msg.text)
        print('JSON full: ', msg)
        print('KEY Document: ', msg.document)
        print('KEY Document.fileID: ', msg.document.file_id)
        #ID = msg.message_id
        #photo = bot.get_file(document.file_id)
        file_info = bot.get_file(msg.document.file_id)
        i = file_info.file_path.find('/')
        file_name = file_info.file_path[i+1::]
        #file = requests.get('https://api.telegram.org/file/bot{0}/{1}'.format(TOKEN, file_info.file_path))
        file_test = urllib.request.urlopen('https://api.telegram.org/file/bot{0}/{1}'.format(TOKEN, file_info.file_path)).read()
        file_save = open(file_name, 'wb')
        file_save.write(file_test)
        file_save.close()
        print('INFO: ', file_info)
        print('FILE PATH: ', file_info.file_path)
        #print(file)
        #arq = open(file, 'w')
        #arq.close()

    except Exception as e:
        print(e)


@bot.message_handler(func=lambda msg: True)
def echo_text(msg):
    print('\nFunc = ALL Msgs: ', msg.text, '\n\n', msg)


@bot.message_handler(content_types=['photo'], func=lambda msg: True)
def echo_photo(msg):
    print('\nFunc = PHOTO: ', msg.text, '\n\n', msg)
    print()
    print('MSG Photo: \n', msg.photo)

    #save = open('test.txt', 'a')
    i = 0
    for file_id in msg.photo:
        print('MSG Photo [%i]: %s' %(i, file_id))
        i += 1
        #save.write(file_id)
    #save.close()
    print(msg.photo[0].file_id)
    print(msg.photo[1].file_id)

    #print(msg.photo.file_id)
    file_info = bot.get_file(msg.photo[3].file_id)
    #file = requests.get('https://api.telegram.org/file/bot{0}/{1}'.format(TOKEN, file_info.file_path))
    #print('Return FILE: ', file)
    print('File INFO: ', file_info)
    i = file_info.file_path.find('/')
    file_name = file_info.file_path[i+1::]
    #file = requests.get('https://api.telegram.org/file/bot{0}/{1}'.format(TOKEN, file_info.file_path))
    file_test = urllib.request.urlopen('https://api.telegram.org/file/bot{0}/{1}'.format(TOKEN, file_info.file_path)).read()
    file_save = open(file_name, 'wb')
    file_save.write(file_test)
    file_save.close()



    '''
        file_info = bot.get_photo(file_id)
        i = file_info.file_path.find('/')
        file_name = file_info.file_path[i+1::]
        file_test = urllib.request.urlopen('https://api.telegram.org/file/bot{0}/{1}'.format(TOKEN, file_info.file_path)).read()
        file_save = open(file_name, 'wb')
        file_save.write(file_test)
        file_save.close()
    '''





bot.polling(none_stop=False, interval=0)
