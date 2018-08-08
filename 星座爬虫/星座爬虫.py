import requests
from bs4 import BeautifulSoup
def get_xingzuo(xingzuonao_name):
    word = []
    xingzuo_dict = {}
    url = 'https://www.meiguoshenpo.com/%s'
    res = requests.get(url % (xingzuonao_name))
    bs = BeautifulSoup(res.text, 'html.parser')
    wrapper = bs.find(name='div', attrs={'class': 'wrapper mt_40'})
    astro_logo = wrapper.find(name='div', attrs={'class': 'astro_logo'})
    xingzuo_name = astro_logo.find(name='span').text
    xingzuo_time = astro_logo.find(name='em').text
    word.append('星座名：' + xingzuo_name)
    word.append('星座时间：' + xingzuo_time)
    astro_info = wrapper.find(name='div', attrs={'class': 'astro_info'})
    an_overview_of_the = astro_info.find(name='h5').text
    keyword__list = astro_info.find_all(name='li')
    for keyword in keyword__list:
        word.append(keyword.text)
    detailed = astro_info.find(name='h6').text
    content = astro_info.find(name='p').text
    detailed_content = detailed + '：' + content
    word.append(detailed_content)
    for i in word:
        xingzuo_dict[i.split('：')[0]] = i.split('：')[1]
    return xingzuo_dict