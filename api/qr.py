import qrcode
import time
import os


def make_qr(text, size):
    now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
    data = text
    size = size
    qr = qrcode.QRCode(
        version=size,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    '''version1:12x12,version2:330x330'''
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image()
    if not os.path.exists('static/qr/'):  # upload目录初始化
        os.makedirs('static/qr/')
    img_path = "static/qr/" + now + ".png"
    img.save(img_path)
    path = '/'+img_path
    return path


if __name__ == "__main__":
    make_qr("text", 1)
