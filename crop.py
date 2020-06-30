import cv2
from PIL import Image
im = Image.open('out.jpg').convert('L')
im = im.crop((130,130,1500,1900))
im.save('_out.jpg')