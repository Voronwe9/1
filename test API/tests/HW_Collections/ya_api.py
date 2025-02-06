import requests
import configparser
config = configparser.ConfigParser()
config.read('config.ini')
class YandexDisk:

    def __init__(self, token):
        self.token = token

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token)
        }

    def get_files_list(self):
        files_url = config['ya']['files']
        headers = self.get_headers()
        response = requests.get(files_url, headers=headers)
        if response.status_code == 200:
            print("Yandex Success")
        return response.json()

    def _get_upload_link(self, disk_file_path):
        upload_url = config['ya']['upload']
        headers = self.get_headers()
        params = {"path": disk_file_path, "overwrite": "true"}
        response = requests.get(upload_url, headers=headers, params=params)
        if response.status_code == 200:
            print("Yandex Success")
        return response.json()

    def upload_file_to_disk(self, disk_file_path, filename):
        href = self._get_upload_link(disk_file_path=disk_file_path).get("href", "")
        response = requests.put(href, data=open(filename, 'rb'))
        response.raise_for_status()
        if response.status_code == 201:
            print("Success")
    def get_list_dir(self, dir = '/'):
        upload_url = config['ya']['resources']
        headers = self.get_headers()
        params = {
            'path': f'{dir}',
            }
        response = requests.get(url=upload_url, headers=headers, params=params)
        res = [i['name'] for i in response.json()['_embedded']['items']]
        if response.status_code == 200:
            print("Yandex Success")
        else:
            print("Error")
        return res
    def create_dir(self, dir : str):
        upload_url = config['ya']['resources']
        headers = self.get_headers()
        params = {
            'path': f'/{dir}'
            }
        response = requests.put(url=upload_url, headers=headers, params=params)
        return response.status_code
        # if response.status_code == 201:
        #     print("Yandex Success")
        # else:
        #     print("Error")
    def publish_dir(self, dir : str):
        upload_url = config['ya']['publish']
        headers = self.get_headers()
        params = {
            'path': f'/{dir}'
            }
        response = requests.put(url=upload_url, headers=headers, params=params)
        if response.status_code == 200:
            print("Yandex Success")
        else:
            print("Error")

    def upload_link_to_disk(self, file_name, link, directory = 'VK_photo'):
        upload_url = config['ya']['upload']
        headers = self.get_headers()
        params = {
            'path':f'/{directory}/{file_name}',
            'url':link
        }
        response = requests.post(url = upload_url,headers = headers, params = params)
        if response.status_code == 202:
            print(" Yandex Success")
        else:
            print("Error")


if __name__ == '__main__':
    token = configparser.ConfigParser()
    token.read('token.ini')
    ya = YandexDisk(token['ya']['key'])
    # result = ya.create_dir('for_unittest')
    result = ya.get_list_dir()
    print(result)






