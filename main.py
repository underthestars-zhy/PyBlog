import sqlite3
import os
import sys
os.system("rm version.txt")
os.system('wget https://cdn.jsdelivr.net/gh/underthestars-zhy/pyblog@master/version.txt')
version_new_file=open('version.txt','r')
version_new=str(version_new_file.read())
version_new_file.close()
os.system("rm version.txt")
os.system("clear")
print("+++++This is PyBlog!+++++")
print("+++++++Made By UTS+++++++")
print("Github@underthestars-zhy/PyBlog")
print("当前版本: Beta-1-1021337 最新版本: "+version_new)
print("0: 注册, 1: 登录")
log=int(input("输入:"))
account=0
if log==0:
    conn_log=sqlite3.connect("log.db")
    cur_log=conn_log.cursor()
    cur_log.execute('''Create table Account(id int,name text,password text)''')
    print("现在我们需要一些注册信息")
    user_name=str(input("User_Name:"))
    user_password=str(input("User_Password:"))
    cur_log.execute('''insert into Account Values(1,'{}','{}')'''.format(user_name,user_password))
    conn_log.commit()
    conn_log.close()
    account=1
    print("OK")
elif log==1:
    conn_log = sqlite3.connect("log.db")
    cur_log = conn_log.cursor()
    print("现在我们需要一些登录信息")
    user_name_in = str(input("User_Name:"))
    user_password_in = str(input("User_Password:"))
    user_in=(1,user_name_in,user_password_in)
    cur_log.execute('select * from Account')
    for user_out in cur_log.fetchall():
        user=user_out
    if user == user_in:
        account = 1
    else:
        print("NO")
    conn_log.close()
else:
    os.system("clear")
    print("+++++Error#0-PyBlog!+++++")
    print("+++++++Made By UTS+++++++")
    print("Github@underthestars-zhy/PyBlog")
    print("==========================================")
    sys.exit()
os.system("clear")
if account!=1:
    print("+++++Error#1-PyBlog!+++++")
    print("+++++++Made By UTS+++++++")
    print("Github@underthestars-zhy/PyBlog")
    print("==========================================")
    sys.exit()
os.system("clear")
print("+++++Welcome-PyBlog!+++++")
print("+++++++Made By UTS+++++++")
print("Github@underthestars-zhy/PyBlog")
print("==========================================")
print("选择数据库 0：SQLite，1：MySQL")
sql_set=int(input("选择："))
print("0: 设置， 1:写文章")
main_set=int(input("选择："))
