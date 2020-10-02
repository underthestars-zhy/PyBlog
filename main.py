'''
Made by UTS
'''
import sqlite3
import os
import sys
os.system("rm version.txt")
os.system('wget https://cdn.jsdelivr.net/gh/underthestars-zhy/PyBlog@master/version.txt')
version_new_file=open('version.txt','r')
version_new=str(version_new_file.read())
version_new_file.close()
os.system("rm version.txt")
os.system("clear")
print("+++++This is PyBlog!+++++")
print("+++++++Made By UTS+++++++")
print("Github@underthestars-zhy/PyBlog")
print("当前版本: Beta-2-1002145 最新版本: "+version_new)
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
exit=False
while exit==False:
    os.system("clear")
    print("+++++Welcome-PyBlog!+++++")
    print("+++++++Made By UTS+++++++")
    print("Github@underthestars-zhy/PyBlog")
    print("==========================================")
    print("0: 退出, 1: 设置, 2:主题")
    main_set=int(input("选择："))
    if main_set==0:
        os.system("clear")
        print("++++++Bye-Bye "+user_name_in+" ++++++")
        sys.exit()
    elif main_set==1:
        os.system("clear")
        print("+++++AllSets-PyBlog!+++++")
        print("==========================================")
        print("0: Back, 1:更新账户")
        main_set_sets = int(input("选择："))
        if main_set_sets==0:
            continue
        elif main_set_sets==1:
            os.system("clear")
            print("+++++AllSets-PyBlog!+++++")
            print("++++++++更新账户信息++++++++")
            print("==========================================")
            print("0:Back, 1:Nema, 2:Password")
            ac_set_update=int(input("选择: "))
            if ac_set_update==0:
                continue
            elif ac_set_update==1:
                os.system("clear")
                print("+++++AllSets-PyBlog!+++++")
                print("++++++++更新账户名称++++++++")
                print("==========================================")
                user_name_new=str(input("New_Name: "))
                conn_log = sqlite3.connect("log.db")
                cur_log = conn_log.cursor()
                cur_log.execute("delete from Account where id=1")
                conn_log.commit()
                cur_log.execute('''insert into Account Values(1,'{}','{}')'''.format(user_name_new,user_password_in))
                conn_log.commit()
                conn_log.close()
                os.system("clear")
                print("+++++AllSets-PyBlog!+++++")
                print("++++++账户名称已经更新++++++")
                print("==========================================")
                print("请重新登录!")
                sys.exit()
            elif ac_set_update == 2:
                os.system("clear")
                print("+++++AllSets-PyBlog!+++++")
                print("++++++++更新账户密码++++++++")
                print("==========================================")
                print("==========================================")
                user_password_new = str(input("New_Password: "))
                conn_log = sqlite3.connect("log.db")
                cur_log = conn_log.cursor()
                cur_log.execute("delete from Account where id=1")
                conn_log.commit()
                cur_log.execute('''insert into Account Values(1,'{}','{}')'''.format(user_name_in, user_password_new))
                conn_log.commit()
                conn_log.close()
                os.system("clear")
                print("+++++AllSets-PyBlog!+++++")
                print("++++++账户密码已经更新++++++")
                print("==========================================")
                print("请重新登录!")
                sys.exit()
            else:
                print("+++++Error#2-PyBlog!+++++")
                print("+++++++Made By UTS+++++++")
                print("Github@underthestars-zhy/PyBlog")
                print("==========================================")
                sys.exit()
        else:
            print("+++++Error#3-PyBlog!+++++")
            print("+++++++Made By UTS+++++++")
            print("Github@underthestars-zhy/PyBlog")
            print("==========================================")
            sys.exit()