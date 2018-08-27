import re
from core import create_tables
from core import mysysqlinfo
def analyze_html(res, num):
    # res, num = ret.result()
    if num == 0:
        Baidu(res, 'baiduinfo')
    elif num == 1:
        MIUI(res, 'xiaomiinfo')
    elif num == 2:
        PP_assistant(res,'ppinfo')
    elif num == 3:
        Apple(res,'appleinfo')



def Baidu(url, table_name):
    show_table_k(table_name)  # 查看数据空表是否存在,不存在就创建,有的话就不进行任何操作

    sql = 'insert into baiduinfo (name,count,date)  VALUES (%s,%s,%s)'
    res = re.findall('''  <p class="name">(.*?)</p>
                    <p class="down-size">
                        <span class="down">(.*?)</span>
                        <span class="size">(.*?)</span>
                    </p>''', url)
    conn = mysysqlinfo.mysql_info()
    cursor = conn.cursor()
    cursor.executemany(sql, res)
    conn.commit()
    cursor.close()
    conn.close()


def MIUI(url, table_name):
    show_table_k(table_name)
    sql = 'insert into xiaomiinfo (name,category)  VALUES (%s,%s)'
    res = re.findall('<h5><.+?>(.+?)</a></h5><p.+?><a.+?>(.+?)</a></p>', url)
    conn = mysysqlinfo.mysql_info()
    cursor = conn.cursor()
    cursor.executemany(sql, res)
    conn.commit()
    cursor.close()
    conn.close()


def PP_assistant(url, table_name):
    show_table_k(table_name)
    sql = 'insert into ppinfo (name,downloads)  VALUES (%s,%s)'
    res=re.findall('ellipsis" title=".*?">(.*?)</a><p class="app-downs ellipsis" title=".*?">(.*?)</p>',url)


    conn = mysysqlinfo.mysql_info()
    cursor = conn.cursor()
    cursor.executemany(sql, res)
    conn.commit()
    cursor.close()
    conn.close()



def Apple(url, table_name):
    show_table_k(table_name)
    sql = 'insert into appleinfo (name,downloads)  VALUES (%s,%s)'
    res=re.findall('<h3><a href=.*?">(.*?)</a></h3><h4><a .*?>(.*?)</a></h4>',url)
    conn = mysysqlinfo.mysql_info()
    cursor = conn.cursor()
    cursor.executemany(sql, res)
    conn.commit()
    cursor.close()
    conn.close()

def show_table_k(table_name):

    sql_show = 'select id from %s WHERE id=1' % table_name

    conn = mysysqlinfo.mysql_info()

    cursor = conn.cursor()
    try:
        cursor.execute(sql_show)
    except  Exception as e:
        if table_name == 'baiduinfo':
            create_tables.create_baiduinfo()
        elif table_name == 'xiaomiinfo':
            create_tables.create_xiaomiinfo()
        elif table_name == 'ppinfo':
            create_tables.create_ppinfo()
        elif table_name == 'appleinfo':
            create_tables.create_appleinfo()
    finally:
        cursor.close()
        conn.close()