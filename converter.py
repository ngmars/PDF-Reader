import cv2
import numpy as np
import requests
import io
import json
from PIL import Image
from pdf2image import convert_from_path
pages = convert_from_path('file1.pdf', dpi=200, output_folder=None, first_page=3, last_page=91, fmt="ppm", jpegopt=None, thread_count=1, userpw=None, use_cropbox=False, strict=False, transparent=False, poppler_path=None, grayscale=False, size=None, paths_only=False, use_pdftocairo=False)
ite=0
for page in pages:
        ite=ite+1
        page.save('out.jpg', 'JPEG') 
        im = Image.open('out.jpg').convert('L')
        im = im.crop((130,130,1500,1900))
        im.save('out.jpg')
        img = cv2.imread("out.jpg")
        height, width, _ = img.shape

        # Cutting image
        # roi = img[0: height, 400: width]
        roi = img

        # Ocr
        url_api = "https://api.ocr.space/parse/image"
        _, compressedimage = cv2.imencode(".jpg", roi, [1, 90])
        file_bytes = io.BytesIO(compressedimage)

        result = requests.post(url_api,
                files = {"out.jpg": file_bytes},
                data = {"apikey": "73569e28f488957",
                        "language": "eng"})

        result = result.content.decode()
        result = json.loads(result)

        parsed_results = result.get("ParsedResults")[0]
        text_detected = parsed_results.get("ParsedText")
        print(text_detected)

        cv2.destroyAllWindows()
        file_object = open('Questions.txt', 'a')
        file_object.write(text_detected)
        file_object.close()
        print(ite)

       
