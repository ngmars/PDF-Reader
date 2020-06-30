from PIL import Image
from pdf2image import convert_from_path
header_offset = 200
footer_offset = 1200 
pages = convert_from_path('file1.pdf', dpi=200, output_folder=None, first_page=3, last_page=4, fmt="ppm", jpegopt=None, thread_count=1, userpw=None, use_cropbox=False, strict=False, transparent=False, poppler_path=None, grayscale=False, size=None, paths_only=False, use_pdftocairo=False)

for page in pages:
    page.save('out.jpg', 'JPEG') 
    im = Image.open('out.jpg').convert('L')
    im = im.crop((130,130,1500,1900))
    im.save('out.jpg') 
    