
from core import mysysqlinfo
# 创建表
def create_baiduinfo():
    mas = '''CREATE table baiduinfo (
id INT auto_increment PRIMARY KEY,
name varchar(100) not NULL,
count VARCHAR(100) not null,
date VARCHAR (100) not NULL
);'''
    conn = mysysqlinfo.mysql_info()
    cursor = conn.cursor()
    cursor.execute(mas)
    cursor.close()
    conn.close()


def create_xiaomiinfo():
    mas = '''CREATE table xiaomiinfo (
id INT auto_increment PRIMARY KEY,
name varchar(100) not NULL,
category VARCHAR(100) not null
);'''

    conn = mysysqlinfo.mysql_info()
    cursor = conn.cursor()
    cursor.execute(mas)
    cursor.close()
    conn.close()

def create_ppinfo():
    mas = '''CREATE table ppinfo (
    id INT auto_increment PRIMARY KEY,
    name varchar(100) not NULL,
    downloads VARCHAR(100) not null
    );'''
    conn = mysysqlinfo.mysql_info()
    cursor = conn.cursor()
    cursor.execute(mas)
    cursor.close()
    conn.close()

def create_appleinfo():
    mas = '''CREATE table appleinfo (
       id INT auto_increment PRIMARY KEY,
       name varchar(100) not NULL,
       downloads VARCHAR(100) not null
       );'''
    conn = mysysqlinfo.mysql_info()
    cursor = conn.cursor()
    cursor.execute(mas)
    cursor.close()
    conn.close()
