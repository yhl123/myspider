#!/usr/bin/env python
# -*- coding:utf-8 -*-

#需要用到抖音js文件

import re
import requests

url = 'https://www.douyin.com/share/user/6556303280/?share_type=link'  
# 75097696932/96488770253/6556303280/67561351000（作者ID）

# ###################### 1. 根据url获取用户ID #########################
user_id = re.findall('share/user/(.*)/\?', url)[0]

# ###################### 2. 根据用户ID获取签名 #########################
# 方式一：
import os

output = os.popen('node s1.js %s' % user_id)
# output = os.popen('node byted-acrawler.js %s' % user_id)
signature = output.readlines()[0].strip()
# 方式二：
"""
def exec_javascript(file_path, func, *args):
    pip3 install execjs
    import execjs

    with open(file_path, 'r', encoding='UTF-8') as f:
        content = f.read()
    ctx = execjs.compile(content)
    return ctx.call(func, *args)

signature = exec_javascript("encode.js", '_bytedAcrawler.sign', user_id)
"""

# ###################### 3. 获取抖音用户发送过的所有的视频 #########################
headers = {
    'accept': 'application/json',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
    'upgrade-insecure-requests': '1',
    'host':'www.douyin.com',
    'X-Requested-With':'XMLHttpRequest',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
}

user_video_list = []

user_video_params = {
    'user_id': str(user_id),
    'count': '21',
    'max_cursor': '0',
    'aid': '1128',
    '_signature': signature,
    'dytk': '114f1984d1917343ccfb14d94e7ce5f5'
}



def get_aweme_list(max_cursor=None):
    if max_cursor:
        user_video_params['max_cursor'] = str(max_cursor)
    res = requests.get(
        url="https://www.douyin.com/aweme/v1/aweme/post/",
        params=user_video_params,
        headers=headers
    )
    content_json = res.json()
    print(content_json)
    aweme_list = content_json.get('aweme_list', [])
    user_video_list.extend(aweme_list)
    if content_json.get('has_more') == 1:
        return get_aweme_list(content_json.get('max_cursor'))


get_aweme_list()

print("该用户发布过抖音", user_video_list)

# ###################### 4. 获取抖音赞过的所有视频 #########################
#
favor_video_list = []

favor_video_params = {
    'user_id': str(user_id),
    'count': '21',
    'max_cursor': '0',
    'aid': '1128',
    '_signature': signature
}


def get_favor_list(max_cursor=None):
    if max_cursor:
        favor_video_params['max_cursor'] = str(max_cursor)
    res = requests.get(
        url="https://www.douyin.com/aweme/v1/aweme/favorite/",
        params=favor_video_params,
        headers=headers
    )
    content_json = res.json()
    aweme_list = content_json.get('aweme_list', [])
    favor_video_list.extend(aweme_list)
    if content_json.get('has_more') == 1:
        return get_favor_list(content_json.get('max_cursor'))


get_favor_list()

print("该用户赞过抖音", favor_video_list)

# ###################### 5. 下载抖音 #########################

base_download_folder = os.path.join('download', user_id)
if not os.path.isdir(base_download_folder):
    os.mkdir(base_download_folder)

# 下载自己的视频
user_download_folder = os.path.join(base_download_folder, 'user')
if not os.path.isdir(user_download_folder):
    os.mkdir(user_download_folder)

for aweme in user_video_list:
    if aweme.get('video', None):
        video_id = aweme['video']['play_addr']['uri']

        file_name = video_id + ".mp4"
        file_path = os.path.join(user_download_folder, file_name)

        response_video = requests.get(
            url='https://aweme.snssdk.com/aweme/v1/play/',
            params={
                'video_id': video_id,
            },
            stream=True,
        )
        with open(file_path, 'wb') as fh:
            for chunk in response_video.iter_content(chunk_size=1024):
                fh.write(chunk)

# 下载赞过的视频

favor_download_folder = os.path.join(base_download_folder, 'favor')
if not os.path.isdir(favor_download_folder):
    os.mkdir(favor_download_folder)

for aweme in favor_video_list:
    if aweme.get('video', None):
        video_id = aweme['video']['play_addr']['uri']

        file_name = video_id + ".mp4"
        file_path = os.path.join(favor_download_folder, file_name)

        response_video = requests.get(
            url='https://aweme.snssdk.com/aweme/v1/play/',
            params={
                'video_id': video_id,
            },
            stream=True,
        )
        with open(file_path, 'wb') as fh:
            for chunk in response_video.iter_content(chunk_size=1024):
                fh.write(chunk)

