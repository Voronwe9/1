import os
import time

import requests

host = 'http://127.0.0.1:5000'
extensions_files = ('png', 'jpg', 'JPG')
path_dir = 'example'



def get_images(extensions_files: list|tuple, path_dir: str = 'example') -> list:
    examples_files = os.listdir(path_dir)
    filltered_files = list()
    for i in examples_files:
        instance_file = i.split('.')
        if instance_file[1] in extensions_files:
            filltered_files.append(i)
    return filltered_files

def open_images(name_image: str, path_dir: str = 'example'):
    with open(f'{path_dir}/{name_image}', "rb") as image:
        send_image = requests.post(
            url=f'{host}/upscale', files={
                'image': image
            }
        )
    return send_image


if __name__ == '__main__':
    images = get_images(extensions_files)
    tasks_id = list()

    for i in images:
        res = open_images(name_image=i).json()
        print(res)
        tasks_id.append(res.get('task_id'))

    while True:
        time.sleep(1)
        get_task = requests.get(url=f'{host}/upscale/{tasks_id[-1]}').json()
        print(get_task)
        if get_task['status'] in {'SUCCESS', 'FAILURE'}:
            break

    # image_response = requests.get(url=f'{host}/processed/0ae4b17d-0c44-428e-a144-b593a9486d54_up.png')
    # with open("res.png", 'wb') as f:
    #     f.write(image_response.content)
















