import re
import requests
from bs4 import BeautifulSoup


def get_ip_addr(ipadds=None):
    headers = {
        'Host': 'www.ipip.net',
        'Referer': 'https://www.ipip.net/ip.html',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding': 'gzip,deflate,br'
    }
    url = "https://www.ipip.net/ip.html"
    if ipadds:
        response = requests.post(url=url, data={
            'ip': ipadds
        })
    else:
        response = requests.get(url)
    bs = BeautifulSoup(response.text, 'html.parser')
    inner = bs.find(name='div',attrs={'class':'outer tableNormal ipSearch'})
    td_list = inner.find_all(name='td',attrs={'colspan':'6'})
    ip_list = []
    for td in td_list:
        ip_list.append(td.find(name = 'span').text)
        # ip_list.append(ip_type)
        # ip_list.append(time_zone)
        # ip_list.append(address)
    print('当前IP：',ip_list[0])
    print('地理位置：',ip_list[1])
    print('相关信息：',ip_list[2])
    if '购买此数据' in ip_list[3]:
        ip_list[3] = ip_list[3].rsplit('。')[0]
    print('IDC：',ip_list[3])
    return ip_list


ip_addr = input('输入要查询的IP，自动默认本地外网:')
ipaddr = re.findall(
    '(25[0-5]|2[0-4]\d|[0-1]\d{2}|[1-9]?\d)\.(25[0-5]|2[0-4]\d|[0-1]\d{2}|[1-9]?\d)\.(25[0-5]|2[0-4]\d|[0-1]\d{2}|[1-9]?\d)\.(25[0-5]|2[0-4]\d|[0-1]\d{2}|[1-9]?\d)',
    ip_addr)
if ipaddr:
    get_ip_addr(ip_addr)
else:
    get_ip_addr()
