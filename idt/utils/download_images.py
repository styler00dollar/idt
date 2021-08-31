import uuid
import requests;
import os;
from PIL import Image
from io import BytesIO
from idt.resizers.get_resizer import get_resizer

__name__ = "download_images"

def download(link, size, root_folder, class_name, resize_method):
    IMG_SIZE = size, size
    response = requests.get(link, timeout=3.000)
    file = BytesIO(response.content)
    raw_img = Image.open(file)

    # resize or crop image according to provided resize method
    img = get_resizer(raw_img, size, resize_method)

    # Split last part of url to get image name and its extension
    img_name = link.rsplit('/', 1)[1]
    img_type = img_name.split('.')[1]

    if img_type.lower() != "jpg":
        raise Exception("Cannot download these type of file")
    else:
        #Check if another file of the same name already exists
        id = uuid.uuid1()
        img.save(f"./{root_folder}/{class_name}/{img_name}.jpg", "JPEG")
