import requests
from core import myauallyze
def get_html(url1, uil_num):
    if uil_num == 3:
        url = url1
        get_html_text(url,uil_num)
    else:
        for i in range(1, 6):
            url = url1.format(i)
            get_html_text(url,uil_num)


def get_html_text(url,uil_num):
    # 伪装浏览器的信息
    headers = {
        'UserAgent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
    }
    # 使用get请求方式
    req = requests.get(url, headers=headers)
    # 网页编码问题,如果不处理,爬到的内容会乱码
    if req.encoding == 'ISO-8859-1':
        encodings = requests.utils.get_encodings_from_content(req.text)
        if encodings:
            encoding = encodings[0]
        else:
            encoding = req.apparent_encoding
        global encode_content
        encode_content = req.content.decode(encoding, 'replace')  # 如果设置为replace，则会用?取代非法字符；
        myauallyze.analyze_html(encode_content, uil_num)  # 获取网页的HTML
    else:
        myauallyze.analyze_html(req.text, uil_num)