from PIL import Image
from pillow_heif import register_heif_opener
import os

register_heif_opener()

input_folder = 'C:/Users/XXX/XXX/HEIC' # โฟลเดอร์ที่มีไฟล์ HEIC
output_folder = 'C:/Users/xxx/xxx/converted' # โฟลเดอร์ที่ต้องการบันทึกไฟล์ PNG

# ค้นหาไฟล์ HEIC ในโฟลเดอร์ที่ระบุ
heic_files = [photo for photo in os.listdir(input_folder) if '.HEIC' in photo]

# แปลงไฟล์ HEIC เป็น PNG และบันทึกในโฟลเดอร์ที่ระบุ
for photo in heic_files:
  temp_img = Image.open(os.path.join(input_folder, photo))
  png_photo = photo.replace('.HEIC','.png')
  temp_img.save(os.path.join(output_folder, png_photo))
