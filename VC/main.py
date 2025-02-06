from ya_api import *
from VK_parser import *
from progress.bar import Bar
import logging
import configparser
config = configparser.ConfigParser()
config.read('config.ini')
logging.basicConfig(
    level = logging.DEBUG,
    filename = config['logging']['filename'],
    format = config['logging']['format'],
    datefmt = config['logging']['datefmt']
    )

logging.info(config['logging']['logging.info'])


if __name__ == '__main__':
    vk_id = int(input('Введите ID:'))
    ya = YandexDisk(input('Введите токен от яндекс диска:'))
    dir = 'Vk_photo'
    token = configparser.ConfigParser()
    token.read('private/token.ini')
    # ya = YandexDisk(token['ya']['key'])
    vk = Vk_Avatar(token['vk']['key'])
    dict = vk.get_dict_img(vk_id, 5)
    vk.write_img_json(vk_id)
    if dir not in ya.get_list_dir():
        ya.create_dir(dir)
        ya.publish_dir(dir)
    photo_dir = ya.get_list_dir(dir)
    bar = Bar('Processing', max=len(dict))
    for j in range(len(dict)):
        bar.next()
        if dict[j]['file_name'] not in photo_dir:
            ya.upload_link_to_disk(dict[j]['file_name'], dict[j]['url'], directory=dir)
        else:
            print('Photo passed')
    bar.finish()















