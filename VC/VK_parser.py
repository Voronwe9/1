import requests
import json
import os.path
import time
from datetime import datetime
import configparser
config = configparser.ConfigParser()
config.read('config.ini')
def write_json(dict, dir = os.getcwd(), json_name = 'photo_vk.json'):
    with open(f'{dir}/{json_name}', 'w', encoding='utf-8') as f:
        json.dump(dict, f, indent=4, sort_keys=True, ensure_ascii=False)
class Vk_Photo:
    url = config['vk']['url']
    def __init__(self, token):
        self.token = token

    def get_photo_link(self, vk_id):
        url_get_photo = self.url + 'photos.getAll'
        res_total = list()
        offset = int()
        swicher = True
        while swicher:
            param = {
                'owner_id' : vk_id,
                'access_token':self.token,
                'offset':offset,
                'extended':'1',
                'v':'5.131'
            }
            res = requests.get(url_get_photo, params=param).json()
            if res.status_code == 200:
                print("VK Success")
            res = requests.get(url_get_photo, params=param)
            if len(res['response']['items']) < 20:
                swicher = False
            res_total += res['response']['items']
            offset += 20
            time.sleep(0.33)

        return res_total
    def get_photo_link_lim(self, vk_id, lim = 5):
        url_get_photo = self.url + 'photos.getAll'
        res_total = list()
        offset = int()
        cut_list = (lim+20)%20
        while offset <= lim:
            param = {
                'owner_id' : vk_id,
                'access_token':self.token,
                'offset':offset,
                'extended': '1',
                'v':'5.131'
            }
            res = requests.get(url_get_photo, params=param).json()
            if res.status_code == 200:
                print("VK Success")
            if offset <= lim - 20:
                res_total += res['response']['items']
            elif offset > lim - 20:
                res_total += res['response']['items'][0 : cut_list]
            offset += 20
            time.sleep(0.33)

        return res_total



    def get_dict_img(self, vk_id, lim = 5):
        vk_dic = self.get_photo_link_lim(vk_id, lim)
        j_list = list()
        size_dict = {'s': 1, 'm': 2, 'o': 3, 'p': 4, 'q': 5, 'r': 6, 'x': 7, 'y': 8, 'z': 9, 'w': 10}
        for i in vk_dic:
            file_url = max(i['sizes'], key=lambda x: size_dict[x["type"]])
            j_dic = {
                'file_name': f"{i['likes']['count']}_{datetime.fromtimestamp(i['date']).strftime('%Y-%m-%d_%H-%M-%S')}",
                'url': file_url['url'],
                'size': file_url['type']
            }
            j_list.append(j_dic)
        return j_list


    def write_img_json(self, vk_id,  dir = os.getcwd() ,json_name = 'photo_vk.json'):
        dict_img = self.get_dict_img(vk_id)
        [x.pop('url') for x in dict_img]
        write_json(dict_img, dir, json_name)

    def write_photo_img(self, vk_id, dir = os.getcwd()+'/photo'):
        dict_img = self.get_dict_img(vk_id)
        if os.path.exists(f'{dir}/'):
            for i in dict_img:
                response = requests.get(i['url'])
                with open(f'{dir}/{i["file_name"]}.jpg', 'wb') as f:
                    f.write(response.content)
        else:
            return 'Укажите имя папки для сохранения фото'

class Vk_Avatar(Vk_Photo):
    def __init__(self, token):
        self.token = token
    def get_photo_link_lim(self, vk_id, lim = 5):
        url_get_av = self.url + 'photos.get'
        param = {
            'access_token': self.token,
            'owner_id': vk_id,
            'album_id': 'profile',
            'count': lim,
            'rev': '1',
            'extended': '1',
            'photo_sizes': '1',
            'v': '5.131'
        }
        respond = requests.get(url_get_av, params=param)
        res = respond.json()['response']['items']
        if respond.status_code == 200:
            print("VK Success")
        return res








