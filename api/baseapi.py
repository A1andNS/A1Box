import base64
import time
import os


def base64_decode(text):
    try:
        text = bytes(text, 'utf-8')
        result = base64.b64decode(text)
        return result.decode()
    except:
        return "解码错误"


def base64_encode(text):
    text = bytes(text, 'utf-8')
    result = base64.b64encode(text)
    return result.decode()


def base85_encode(text):
    text = bytes(text, 'utf-8')
    result = base64.b85encode(text)
    return result.decode()


def base85_decode(text):
    try:
        text = bytes(text, 'utf-8')
        result = base64.b85decode(text)
        return result.decode()
    except:
        return "解码错误"


def base32_encode(text):
    text = text.encode()
    result = base64.b32encode(text)
    return result.decode()


def base32_decode(text):
    try:
        text = text.encode()
        result = base64.b32decode(text)
        return result.decode()
    except:
        return "解码错误"


def base16_encode(text):
    text = text.encode()
    result = base64.b16encode(text)
    return result.decode()


def base16_decode(text):
    try:
        text = text.encode()
        result = base64.b16decode(text)
        return result.decode()
    except:
        return "解码失败"


def img_base64_encode(file):
    with open(file, "rb") as f:
        img_data = f.read()
        base64_data = base64.b64encode(img_data)
        txt_path = file + "_encode.txt"
        txt = open(txt_path, "w")
        txt.write(base64_data.decode())
        txt.close()
        txt_path = '/' + txt_path
        return txt_path


def img_base64_decode(base64_data):
    now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
    if not os.path.exists('static/base64/'):  # upload目录初始化
        os.makedirs('static/base64/')
    img_path = "static/base64/" + now + ".png"
    img = open(img_path, "wb")
    img_data = base64.b64decode(base64_data)
    img.write(img_data)
    img_path = '/' + img_path
    img.close()
    return img_path
