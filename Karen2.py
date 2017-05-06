import requests
from time import sleep

url = "https://api.telegram.org/bot359371106:AAHhSQ_1b2hw0F3zmIimFA_BBAtJN7Mg-BM/"


def get_updates_json(request):
    params = {'timeout': 100, 'offset': None}
    response = requests.get(request + 'getUpdates')
    return response.json()

def last_update(data):
    results = data['result']
    total_updates = len(results) - 1
    return results[total_updates]

def in_text(update):
    text = update['message']['text']
    return text

def get_chat_id(update):
    chat_id = update['message']['chat']['id']
    return chat_id

def send_mess(chat, text):
    params = {'chat_id': chat, 'text': text}
    response = requests.post(url + 'sendMessage', data=params)
    return response

chat_id = get_chat_id(last_update(get_updates_json(url)))
text = in_text(last_update(get_updates_json(url)))

def out_text():
    chat_id = get_chat_id(last_update(get_updates_json(url)))
    text = in_text(last_update(get_updates_json(url)))

    if text == "hello" or text == "hi":
        send_mess(chat_id, "hello to you as well, stranger.")
    else:
        send_mess(chat_id, "I echo to you: %s." % text)

    #send_mess(chat_id, text)

def main():
    update_id = last_update(get_updates_json(url))['update_id']
    while True:
        if update_id == last_update(get_updates_json(url))['update_id']:
            out_text()
            update_id += 1
    sleep(1)

if __name__ == '__main__':
    main()
