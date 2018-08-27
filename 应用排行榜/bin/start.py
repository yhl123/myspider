import os
import sys
import time
from concurrent.futures import ThreadPoolExecutor
sys.path.insert(0,os.path.dirname(os.getcwd()))

from conf import settings
from core import core

if __name__ == '__main__':
    for i, j in enumerate(settings.l1, 1):
        print(i, j)
user_number = input('请输入序号,可多选(多选用逗号隔开):')
start_time = time.time()
msg='=================start====================='
print(msg)
user_number_count = 0
for number in user_number:
    if number in ['1', '2', '3', '4']:
        user_number_count += 1  # 为了查看有几个需要查看的网页,并在下面创相等个线程
        settings.l3.append(int(number))
p = ThreadPoolExecutor(user_number_count)
msg = '''URL个数{}个，启用{}个线程'''
if '4'in user_number and user_number_count==1:
    print(msg.format(1,user_number_count))
elif '4'in user_number and user_number_count!=1:
    print(msg.format((user_number_count-1)*5+1, user_number_count))
elif '4' not in user_number:
    print(msg.format((user_number_count)*5,user_number_count))
for uil_num in settings.l3:
    p.submit(core.get_html, settings.l2[uil_num - 1], uil_num - 1)
p.shutdown(wait=True)
msg='==================end======================'
end_time = time.time()
print(msg)
print('总耗时{}秒'.format(round(end_time-start_time)))
