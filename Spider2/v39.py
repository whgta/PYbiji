import pytesseract as pt
from PIL import Image

#生成图片实例
image = Image.open('C:\\Users\\wh\\Desktop\\2.jpg')

# 调用pytesseract把图片转换成文字
# 返回结果是转换的结果
text = pt.image_to_string(image)
print(text)