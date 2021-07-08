from time import sleep

import requests


def scan(path):
    global temp_dc
    url = "https://scanner.baidu.com/enqueue"
    file_path = path
    files = {'archive': open(file_path, 'rb')}
    try:
        r = requests.post(url, files=files)
        res = r.json()
        if "unsupported" in res['descr']:
            file_type = file_path.split('.')[-1]
            result = file_type + "不是受支持的文件类型"
            temp_dc = {"type": result}
            return temp_dc, temp_dc
        else:
            result_url = res['url']
            result = requests.get(result_url)
            ls = result.json()
            while ls[0]['status'] == "pending":
                sleep(2)
                result = requests.get(result_url)
                ls = result.json()
                temp_dc = ls[0]
            return temp_dc, temp_dc['data'][0]
    except:
        temp_dc = {'type': "网络错误，请检查网络状态！"}
        return temp_dc, temp_dc


if __name__ == "__main__":
    scan("index.php")
