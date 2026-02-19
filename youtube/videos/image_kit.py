import os
from imagekitio import ImageKit
from dotenv import load_dotenv

load_dotenv()

def get_imagekit():
    return ImageKit(
        private_key=os.environ.get("IMAGEKIT_PRIVATE_KEY")
    )

def upload_video(file_data: bytes, file_name: str, folder: str= "videos") -> dict:
    client = get_imagekit()

    response = client.files.upload(
        file = file_data,
        file_name = file_name,
        folder = folder
    )

    return {
        "file_id" : response.file_id,
        "url" : response.url
    }

def upload_thumbnail(file_data: str, file_name: str, folder: str= "thumbnail") -> dict:
    import base64

    if file_data.startswith("data:"):
        base64_data = file_data.split("," ,1)[1]
        image_bytes = base64.b64decode(base64_data)
    else:
        image_bytes = base64.b64decode(file_data)

    client = get_imagekit()

    response = client.files.upload(
        file = image_bytes,
        file_name = file_name,
        folder = folder
    )

    return {
        "file_id" : response.file_id,
        "url" : response.url
    }