import os.path
import uuid

from flask import Flask, jsonify, request, send_file
from flask.views import MethodView
from celery import Celery
from celery.result import AsyncResult
import cv2
from cv2 import dnn_superres

files_path = 'files'

app_name = 'app'
app = Flask(app_name)
app.config['UPLOAD_FOLDER'] = files_path
celery = Celery(app_name, broker='redis://127.0.0.1:6379/1', backend='redis://127.0.0.1:6379/2')
# celery.conf.update(app.config)

# class ContextTask(celery.Task):
#     def __call__(self, *args, **kwargs):
#         with app.app_context():
#             return self.run(*args, **kwargs)
#
# celery.Task = ContextTask

@celery.task()
def fix_photos(input_path: str, output_path: str, model_path: str = 'EDSR_x2.pb') -> None:
    """
    :param input_path: путь к изображению для апскейла
    :param output_path:  путь к выходному файлу
    :param model_path: путь к ИИ модели
    :return:
    """

    scaler = dnn_superres.DnnSuperResImpl_create()
    scaler.readModel(model_path)
    scaler.setModel("edsr", 2)
    image = cv2.imread(input_path)
    result = scaler.upsample(image)
    cv2.imwrite(output_path, result)

# scaler = dnn_superres.DnnSuperResImpl_create()
# scaler.readModel('EDSR_x2.pb')
#
# @celery.task()
# def fix_photos(input_path: str, output_path: str, scaler) -> None:
#     """
#     :param input_path: путь к изображению для апскейла
#     :param output_path:  путь к выходному файлу
#     :param model_path: путь к ИИ модели
#     :return:
#     """
#
#     scaler.setModel("edsr", 2)
#     image = cv2.imread(input_path)
#     result = scaler.upsample(image)
#     cv2.imwrite(output_path, result)


class UpsclePhoto(MethodView):
    def get(self, task_id):
        task = AsyncResult(task_id, app=celery)
        return jsonify({'status': task.status})

    def post(self):
        image_name = self.save_image("image")
        image_pathes = files_path + '/' + image_name
        task = fix_photos.delay(input_path=image_pathes, output_path=image_pathes.replace('.', '_up.'))
        return jsonify(
            {
                'task_id': task.id,
                'file': image_name.replace('.', '_up.')
            }
        )

    def save_image(self, field):
        image = request.files.get(field)
        extension = image.filename.split('.')[-1]
        name = f'{uuid.uuid4()}.{extension}'
        path = os.path.join(files_path, name)
        image.save(path)
        return name
class UploadPhoto(MethodView):

    def get(self, file):
        return send_file(f"{files_path}/{file}")

upscale = UpsclePhoto.as_view('upscale')
upload = UploadPhoto.as_view('upload')

app.add_url_rule('/upscale', view_func=upscale, methods=['POST'])
app.add_url_rule('/upscale/<string:task_id>', view_func=upscale, methods=['GET'])
app.add_url_rule('/processed/<string:file>', view_func=upload, methods=['GET'])

if __name__ == '__main__':
    app.run(debug=True)
