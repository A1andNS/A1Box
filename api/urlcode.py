import urllib.parse


def url_encode(text):
    # text = text.encode('utf-8')
    result = urllib.parse.quote(text)
    return result


def url_decode(text):
    # text = text.encode('utf-8')
    result = urllib.parse.unquote(text)
    return result


if __name__ == "__main__":
    results = url_encode("%23%23")
    print(results)
