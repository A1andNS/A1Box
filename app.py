# -*-utf-8-*-
# author:A1andNS
from flask import Flask, redirect, render_template, request, url_for
from api import baseapi
from api import scanshell
from api import qr
from api import urlcode
from api import random_num
from api import bvtoav
import os

app = Flask(__name__)
version = "V0.2beta"
app.debug = True


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/log')
def log():
    return render_template("log.html")


@app.route('/app/<func>', methods=['GET', 'POST'])
def work(func):
    if func == "base64":
        source = '原文：I am A1andNS'
        chiper = '编码后：SSBhbSBBMWFuZE5T'
        content1 = 'Base64是一种基于64个可打印字符来表示二进制数据的表示方法。'
        content2 = 'Base64常用于在通常处理文本数据的场合，表示、传输、存储一些二进制数据，包括MIME的电子邮件及XML的一些复杂数据。'
        text = request.args.get("text")
        ty = request.args.get("type")
        name = func + "编解码"
        if ty == "Encode":
            result = baseapi.base64_encode(text)
            return render_template("basex.html", result=result, name=name, func=func, source=source, chiper=chiper,
                                   content1=content1, content2=content2)
        elif ty == "Decode":
            result = baseapi.base64_decode(text)
            return render_template("basex.html", result=result, name=name, func=func, source=source, chiper=chiper,
                                   content1=content1, content2=content2)
        else:
            return render_template("basex.html", result="请于此处输入.....", name=name, func=func, source=source,
                                   chiper=chiper, content1=content1, content2=content2)
    elif func == "base85":
        source = '原文：I am A1andNS'
        chiper = '编码后：Ng!cuAVD!<Ze&hV'
        content1 = 'base85 也称为Ascii85，是Paul E. Rutter为btoa实用程序开发的一种二进制文本编码形式。'
        content2 = '用途是Adobe的PostScript和Portable Document Format文件格式，以及Git使用的二进制文件的补丁编码。'
        text = request.args.get("text")
        ty = request.args.get("type")
        name = func + "编解码"
        if ty == "Encode":
            result = baseapi.base85_encode(text)
            return render_template("basex.html", result=result, name=name, func=func, source=source, chiper=chiper,
                                   content1=content1, content2=content2)
        elif ty == "Decode":
            result = baseapi.base85_decode(text)
            return render_template("basex.html", result=result, name=name, func=func, source=source, chiper=chiper,
                                   content1=content1, content2=content2)
        else:
            return render_template("basex.html", result="请于此处输入.....", name=name, func=func, source=source,
                                   chiper=chiper, content1=content1, content2=content2)
    elif func == "base32":
        source = '原文：I am A1andNS'
        chiper = '编码后：JEQGC3JAIEYWC3TEJZJQ===='
        content1 = 'Base32编码是使用32个可打印字符（字母A-Z和数字2-7）对任意字节数据进行编码的方案。'
        content2 = '编码后的字符串不用区分大小写并排除了容易混淆的字符，可以方便地由人类使用并由计算机处理。'
        text = request.args.get("text")
        ty = request.args.get("type")
        name = func + "编解码"
        if ty == "Encode":
            result = baseapi.base32_encode(text)
            return render_template("basex.html", result=result, name=name, func=func, source=source, chiper=chiper,
                                   content1=content1, content2=content2)
        elif ty == "Decode":
            result = baseapi.base32_decode(text)
            return render_template("basex.html", result=result, name=name, func=func, source=source, chiper=chiper,
                                   content1=content1, content2=content2)
        else:
            return render_template("basex.html", result="请于此处输入.....", name=name, func=func, source=source,
                                   chiper=chiper, content1=content1, content2=content2)
    elif func == "base16":
        source = '原文：I am A1andNS'
        chiper = '编码后：4920616D204131616E644E53'
        content1 = '使用16个ASCII可打印字符（数字0-9和字母A-F），对任意字节数据进行编码。'
        content2 = ' Base16编码后的数据量是原数据的两倍：1000比特数据需要250个字符（即 250*8=2000 比特）。。'
        text = request.args.get("text")
        ty = request.args.get("type")
        name = func + "编解码"
        if ty == "Encode":
            result = baseapi.base16_encode(text)
            return render_template("basex.html", result=result, name=name, func=func, source=source, chiper=chiper,
                                   content1=content1, content2=content2)
        elif ty == "Decode":
            result = baseapi.base16_decode(text)
            return render_template("basex.html", result=result, name=name, func=func, source=source, chiper=chiper,
                                   content1=content1, content2=content2)
        else:
            return render_template("basex.html", result="请于此处输入.....", name=name, func=func, source=source,
                                   chiper=chiper, content1=content1, content2=content2)
    elif func == "shell":
        if request.method == 'POST':
            if request.form.get('Source') == "WEBDIR+":
                if request.files['file']:
                    if not os.path.exists('static/upload/'):  # upload目录初始化
                        os.makedirs('static/upload/')
                    file = request.files['file']
                    filename = file.filename
                    root_path = "static/upload/"
                    file_path = root_path + filename
                    file.save(file_path)
                    dc, data = scanshell.scan(file_path)
                    os.remove(file_path)  # 检测完即清除upload文件
                    if "type" in dc:
                        return "<h1 align='center'>" + dc['type'] + "</h1>"
                    else:
                        return render_template("shellresult.html", dc=dc, data=data)
                else:
                    tips = "请选择你的文件后再点击转换按钮"
                    tips_en = "Please choose your file after clicking the button!"
                    url = "/app/shell"
                    return render_template("error.html", tips=tips, url=url, tips_en=tips_en)
            else:
                return "<h1 align='center'>开发中。。。。。。</h1>"
        else:
            return render_template("shell.html")
    elif func == "qrcode":
        path = "/static/img/init.png"
        if request.method == "POST":
            if request.form.get("text"):
                text = request.form.get("text")
                path = qr.make_qr(text, 1)
                return render_template("qrcode.html", result=text, path=path)
            else:
                return render_template("qrcode.html", result="请在此处输入....", path=path)
        else:
            return render_template("qrcode.html", result="请在此处输入....", path=path)
    elif func == "url":
        name = "URL编解码"
        text = request.args.get("text")
        ty = request.args.get("type")
        if ty == "Encode":
            result = urlcode.url_encode(text)
            print(result)
            return render_template("urlcode.html", name=name, func=func, result=result)
        elif ty == "Decode":
            result = urlcode.url_decode(text)
            print(result)
            return render_template("urlcode.html", result=result, name=name, func=func)
        else:
            return render_template("urlcode.html", name=name, func=func)
    elif func == "imgtobase64":
        path = "/static/img/init.png"
        if request.method == 'POST':
            if request.form.get('type') == "图片转文本":
                if request.files['file']:
                    if not os.path.exists('static/upload/'):  # upload目录初始化
                        os.makedirs('static/upload/')
                    file = request.files['file']
                    filename = file.filename
                    root_path = "static/upload/"
                    file_path = root_path + filename
                    file.save(file_path)
                    txt_path = baseapi.img_base64_encode(file_path)
                    os.remove(file_path)  # 装完就结束
                    return render_template("302.html", url=txt_path)
                else:
                    tips = "请选择你的文件后再点击转换按钮"
                    tips_en = "Please choose your file after clicking the button!"
                    url = "/app/imgtobase64"
                    return render_template("error.html", tips=tips, url=url, tips_en=tips_en)
            elif request.form.get('type') == "文本转图片":
                text = request.form.get('text')
                img_path = baseapi.img_base64_decode(text)
                return render_template("imgtobase64.html", path=img_path)
        else:
            return render_template("imgtobase64.html", path=path)
    elif func == "covid-19":
        return render_template("covid-19.html")
    elif func == "random":
        if request.method == "POST":
            if request.form.get('start') and request.form.get('end') and request.form.get('num'):
                start = request.form.get('start')
                end = request.form.get('end')
                num = request.form.get('num')
                result = random_num.random_num(start, end, num)
                return render_template("random_num.html", result=result, start=start, end=end, num=num)
            else:
                result = "请正确输入参数！！！"
                return render_template("random_num.html", result=result, start=1, end=100, num=10)
        else:
            return render_template("random_num.html", start=1, end=100, num=10)
    elif func == "bvtoav":
        BV_default = 'BV1ny4y137Nf'
        if request.method == "POST":
            if request.form.get('bv'):
                bv = request.form.get('bv')
                result = bvtoav.change(bv)
                if result['msg']:
                    return render_template("bvtoav.html", msg=result['msg'], BV=bv)
                else:
                    return render_template("bvtoav.html", url=result['url'], av="av"+str(result['AV']), BV=bv)
            else:
                return render_template("bvtoav.html", BV=BV_default)
        else:
            return render_template("bvtoav.html", BV=BV_default)


@app.route('/game/<gamename>', methods=['GET', 'POST'])
def game(gamename):
    if gamename == "2048":
        return render_template("2048.html")


@app.route('/about')
def about():
    return render_template("about.html", version=version)


if __name__ == "__main__":
    port = 5000
    host = "0.0.0.0"
    app.run(host=host, port=port)
