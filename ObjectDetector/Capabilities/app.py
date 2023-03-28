from chalice import Chalice
from chalicelib import storage_service
from chalicelib import recognition_service

import random

app = Chalice(app_name='Capabilities')
app.debug = True

storage_location = 'contents.stubborngastropod.ai'
storage_service = storage_service.StorageService(storage_location)
recognition_service = recognition_service.RecognitionService(storage_service)

@app.route('/demo-object-detection', cors = True)

def demo_object_detection():
    files = storage_service.list_files()
    images = [file for file in files if file['file_name'].endswith(".jpg")]
    image = random.choice(images)

    objects = recognition_service.detect_objects(image['file_name'])

    return {
        "imageName": image['file_name'],
        "imageUrl": image['url'],
        "objects": objects
    }

# The view function above will return {"hello": "world"}
# whenever you make an HTTP GET request to '/'.
#
# Here are a few more examples:
#
# @app.route('/hello/{name}')
# def hello_name(name):
#    # '/hello/james' -> {"hello": "james"}
#    return {'hello': name}
#
# @app.route('/users', methods=['POST'])
# def create_user():
#     # This is the JSON body the user sent in their POST request.
#     user_as_json = app.current_request.json_body
#     # We'll echo the json body back to the user in a 'user' key.
#     return {'user': user_as_json}
#
# See the README documentation for more examples.
#
