import pymysql
from conf import settings


def mysql_info():
    ret = pymysql.connect(host=settings.host, database=settings.database, user=settings.user,
                          port=settings.port, password=settings.password,charset=settings.charset)
    return ret
