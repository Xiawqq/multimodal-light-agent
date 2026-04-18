"""

图像属性处理

"""


import cv2


def get_image_size(image_path: str):
    image = cv2.imread(image_path)

    if image is None:
        return "图片打开失败或无法读取图片信息"

    height, width = image.shape[:2]
    return f"图片尺寸为：宽 {width} 像素，高 {height} 像素"