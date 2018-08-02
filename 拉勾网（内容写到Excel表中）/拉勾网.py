import requests
import json
import time
from lxml import etree
import pandas as pd

s = requests.session()
url = 'https://www.lagou.com/jobs/positionAjax.json?city=%E5%8C%97%E4%BA%AC&needAddtionalResult=false'
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9,und;q=0.8,en;q=0.7',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Host': 'www.lagou.com',
    'Referer': 'https://www.lagou.com/jobs/list_Python?px=default&gx=%E5%85%A8%E8%81%8C&gj=&isSchoolJob=1&city=%E5%85%A8%E5%9B%BD',
    'Upgrade-Insecure-Requests': '1',
}
data = {
    'first': 'true',
    'pn': '',
    'kd': '教育'
}


id = 1000
id_list = []
district_list = []
salary_list = []
positionName_list = []
detail_url_list=[]
education_list=[]
workYear_list=[]
createTime_list=[]
positionLables_list=[]
try:
    for x in range(1, 5):
        time.sleep(5)
        data['pn'] = x
        r1 = s.post(
            url=url,
            headers=headers,
            data=data
        )
        result = r1.json()
        jobs = result['content']['positionResult']['result']

        for job in jobs:
            # print(job)
            companyShortName = job['companyShortName']
            positionId = job['positionId']  # 主页ID
            companyFullName = job['companyFullName']  # 公司全名
            companyLabelList = job['companyLabelList']  # 福利待遇
            companySize = job['companySize']  # 公司规模
            industryField = job['industryField']
            createTime = job['createTime']  # 发布时间
            district = job['district']  # 地区
            education = job['education']  # 学历要求
            financeStage = job['financeStage']  # 上市否
            firstType = job['firstType']  # 类型
            secondType = job['secondType']  # 类型
            formatCreateTime = job['formatCreateTime']  # 发布时间
            publisherId = job['publisherId']  # 发布人ID
            salary = job['salary']  # 薪资
            workYear = job['workYear']  # 工作年限
            positionName = job['positionName']  #
            jobNature = job['jobNature']  # 全职
            positionAdvantage = job['positionAdvantage']  # 工作福利
            positionLables = job['positionLables']  # 工种
        #
            detail_url = 'https://www.lagou.com/jobs/{}.html'.format(positionId)
            response = s.get(url=detail_url, headers=headers)
            response.encoding = 'utf-8'
            tree = etree.HTML(response.text)
            desc = tree.xpath('//*[@id="job_detail"]/dd[2]/div/p/text()')

            # print(companyFullName)
            # print('%s 拉勾网链接:-> %s' % (companyShortName, detail_url))
            detail_url_list.append(detail_url)
            # print('职位：%s' % positionName)
            positionName_list.append(positionName)
            # print('职位类型：%s' % firstType)
            # print('薪资待遇：%s' % salary)
            salary_list.append(salary)
            # print('职位诱惑：%s' % positionAdvantage)
            # print('地区：%s' % district)
            district_list.append(district)
            id+=1
            id_list.append(id)
            # print('类型：%s' % jobNature)
            # print('工作经验：%s' % workYear)
            workYear_list.append(workYear)
            # print('学历要求：%s' % education)
            education_list.append(education)
            # print('发布时间：%s' % createTime)
            createTime_list.append(createTime)
            x = ''
            # for label in positionLables:
            #     x += label + ','
            # print('技能标签：%s' % x)
            # print('公司类型：%s' % industryField)
            positionLables_list.append(positionLables)
            # for des in desc:
                # print(des)
except KeyError :
    pass
df = pd.DataFrame({"id": id_list,
                   "地区": district_list,
                   "工资": salary_list,
                   '职位':positionName_list,
                   '网址':detail_url_list,
                   '学历要求':education_list,
                   '工作经验':workYear_list,
                   '发布时间':createTime_list,
                   '技能':positionLables_list},
                  columns=['id','职位' ,'地区', '工资','网址','学历要求','工作经验','发布时间','技能'])

df = df.fillna(value=0)
df.to_excel('北京教育职位表.xlsx', sheet_name='bluewhale_cc')
print(df)