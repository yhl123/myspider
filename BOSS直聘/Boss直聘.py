import os
import re
import time
import requests
from bs4 import BeautifulSoup

addr = {

    '北京': 'c101010100',
    '上海': 'c101020100',
    '广州': 'c101280100',
    '太原': 'c101100100',
    '杭州': 'c101210100',
}
PAGINATINO = 2


def BossDirecruit():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36'
    }
    for i in range(1, PAGINATINO + 1):
        time.sleep(2)
        url = 'https://www.zhipin.com/{1}-p100109/?ka=sel-city-101020100?page={0}&ka=page-{0}'.format(i, addr['杭州'])
        s = requests.session()
        res = s.get(
            url=url,
            headers=headers
        )
        bp = BeautifulSoup(res.text, 'html.parser')
        count = bp.find(name='div', attrs={'class': 'job-list'})
        li = count.find_all(name='li')
        for message in li:
            time.sleep(2)
            job_title = message.find(name='div', attrs={'class': 'job-title'}).text
            job_red = message.find(name='span', attrs={'class': 'red'}).text
            job_addr, _, job_ex = message.find(name='p').text.split(' ')
            company_text = message.find(name='div', attrs={'class': 'company-text'})
            company_cote = message.find(name='a').get('href')
            company_name = company_text.find(name='h3').text
            company_category = str(company_text.find(name='p'))
            info_publiss = message.find(name='div', attrs={'class': 'info-publis'})
            info_publis = str(info_publiss.find(name='h3'))
            info = re.findall('<h.*?/>(.*?)<e.*?m>(.*?)</h3>', info_publis, )
            info_name = info[0][0]
            info_post = info[0][1]
            info_time = info_publiss.find(name='p').text
            company_content = re.findall('<p>(.*?)<e.*?m>(.*?)<e.*?m>(.*?)<', company_category, )
            company_url = 'https://www.zhipin.com/' + company_cote
            if company_content:
                sort = company_content[0][0]
                state = company_content[0][1]
                scale = company_content[0][2]
            else:
                sort = '无'
                state = '无'
                scale = '无'
            print('工作名称:', job_title)
            print('工资:', job_red)
            print('公式名称:', company_name)
            print('工作地点:', job_addr)
            print('工作经验:', job_ex)
            print('工作类型:', sort)
            print('工作类型:', state)
            print('公式规模:', scale)
            print('Boss公式网址:', company_url)
            job_box = s.get(url=company_url, headers=headers)
            bp1 = BeautifulSoup(job_box.text, 'html.parser')
            job_boxs = bp1.find(name='div', attrs={'class': 'job-box'})
            job_sec = job_boxs.find(name='div', attrs={'class': 'job-sec'})
            job_description = job_sec.find(name='div', attrs={'class': 'text'}).text.strip()
            print(job_description)
            print('-' * 120)
    return


BossDirecruit()
