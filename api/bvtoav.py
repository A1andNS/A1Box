import requests
import json


def change(bv):
    if bv[0:2] != "BV":
        result = {"AV": "", "url": "", "msg": "你输入的BV号有误"}
        return result
    bv = bv[2:]
    headers = {
        "User-Agent": "Mozilla / 5.0(Windows NT 6.1;Win64;x64) AppleWebKit / 537.36(KHTML, like Gecko) \
Chrome / 80.0.3987.163 Safari / 537.36"
    }
    url = 'http://api.bilibili.com/x/web-interface/archive/stat?bvid={}'.format(bv)
    r = requests.get(url, headers=headers)
    data = json.loads(r.text)
    try:
        av = data["data"]["aid"]
        result_url = "https://www.bilibili.com/video/av{}".format(av)
        result = {"AV": av, "url": result_url, "msg": ""}
        return result
    except:
        result = {"AV": "", "url": "", "msg": "你输入的BV号有误"}
        return result


if __name__ == "__main__":
    result = change("BV1ny4y137Nf")
    if result['msg']:
        print(result["msg"])
    else:
        print(result['AV'], result['url'])
