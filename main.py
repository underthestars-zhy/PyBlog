'''
Made by UTS
WebSite: https://uts.ski
License: MIT license
'''

def update_page():
    """Update Page"""
    import sqlite3
    conn_log = sqlite3.connect("log.db")
    cur_log = conn_log.cursor()
    cur_log.execute('select * from BackUp_Pages')
    lsts = []
    for back in cur_log.fetchall():
        lsts.append(back)
    conn_log.close()
    for lst in lsts:
        name = lst[0]
        path_ = lst[1]
        time_ = lst[2]
        txt = lst[3]
        pic_url = lst[5]
        import theme_write as Tr
        if Tr.page_write(name, path_, time_, txt, pic_url):
            pass
        else:
            return False
    return True

def date_celebrate():
    import datetime
    month_ = int(datetime.datetime.now().month)
    day_ = int(datetime.datetime.now().day)
    if month_ == 10 and day_ == 1:
        return "Happy National Day, the first version of PyBlog was released today!"
    elif month_ == 10 and day_ == 31:
        return "The Develop setting was added for the first time.\ntrick or treat!"
    elif month_ == 12 and day_ == 25:
        return "Merry Christmas!"

def data_cmd():
    import datetime
    month_ = int(datetime.datetime.now().month)
    day_ = int(datetime.datetime.now().day)
    if month_ == 10 and day_ == 1:
        return True
    elif month_ == 10 and day_ == 31:
        return True
    elif month_ == 12 and day_ == 25:
        return True
if __name__ == '__main__':
    import sqlite3
    import os
    import sys
    import time
    # Variable forward declaration
    develop_celebrate = False
    develop_theme_version = False
    # Main program
    os.system("rm -rf __pycache__")
    os.system("rm version.txt")
    os.system('wget https://github.com/underthestars-zhy/PyBlog/raw/master/version.txt')
    version_new_file = open('version.txt', 'rt')
    version_new = str(version_new_file.read())
    version_new_file.close()
    os.system("rm version.txt")
    os.system("clear")
    print("+++++This is PyBlog!+++++")
    print("+++++++Made By UTS+++++++")
    print("Github@underthestars-zhy/PyBlog")
    print('''当前版本: Beta-5 最新版本: {0}'''.format(version_new))
    print("==========================================")
    print("0: 注册, 1: 登录")
    log = int(input("输入:"))
    account = 0
    if log == 0:
        conn_log = sqlite3.connect("log.db")
        cur_log = conn_log.cursor()
        cur_log.execute('''Create table Account(id int,name text,password text)''')
        cur_log.execute('''Create table Themes(id int,name text)''')
        cur_log.execute('''Create table IndexD(id int,tf int)''')
        cur_log.execute('''Create table DevelopSet(id int,tf int)''')
        cur_log.execute('''Create table BackUp_Pages(tittle text, path text, time text, content text, html_content text, pic text)''')
        print("现在我们需要一些注册信息")
        user_name = str(input("User_Name:"))
        user_password = str(input("User_Password:"))
        cur_log.execute('''insert into Account Values(1,'{}','{}')'''.format(user_name, user_password))
        cur_log.execute('''insert into Themes Values(1,'no themes')''')
        cur_log.execute('''insert into IndexD Values(1,0)''')
        cur_log.execute('''insert into DevelopSet Values(1,0)''')  # celebrate
        cur_log.execute('''insert into DevelopSet Values(2,0)''')  # ThemeVersion
        conn_log.commit()
        cur_log.execute('select * from Themes')
        t_name = ""
        for t_name_out in cur_log.fetchall():
            t_name = str(t_name_out[1])
        conn_log.close()
        account = 1
        print("OK")
    elif log == 1:
        conn_log = sqlite3.connect("log.db")
        cur_log = conn_log.cursor()
        cur_log.execute('select * from Themes')
        t_name = ""
        for t_name_out in cur_log.fetchall():
            t_name = str(t_name_out[1])
        print("现在我们需要一些登录信息")
        user_name_in = str(input("User_Name:"))
        user_password_in = str(input("User_Password:"))
        user_in = (1, user_name_in, user_password_in)
        cur_log.execute('select * from Account')
        for user_out in cur_log.fetchall():
            user = user_out
        if user == user_in:
            account = 1
        else:
            print("NO")
        # Develop Select
        cur_log.execute('select * from DevelopSet')
        for developset_in in cur_log.fetchall():
            if developset_in[0] == 1 and developset_in[1] == 1:
                develop_celebrate = True
            elif developset_in[0] == 2 and developset_in[1] == 1:
                develop_theme_version= True
    else:
        os.system("clear")
        print("+++++Error#0-PyBlog!+++++")
        print("+++++++Made By UTS+++++++")
        print("Github@underthestars-zhy/PyBlog")
        print("==========================================")
        sys.exit()
    os.system("clear")
    if account != 1:
        print("+++++Error#1-PyBlog!+++++")
        print("+++++++Made By UTS+++++++")
        print("Github@underthestars-zhy/PyBlog")
        print("==========================================")
        sys.exit()
    if develop_theme_version:
        try:
            from theme_main import *
            os.system("rm version_theme.txt")
            os.system('wget ' + least_version_url())
            file = open('version_theme.txt', 'rt')
            version_theme = str(file.read())
            file.close()
            os.system("rm version_theme.txt")
            theme_version = "当前主题版本: " + version() + " 最新主题版本: " + version_theme
        except:
            theme_version = "当前主题不支持/你还未安装主题"
    while True:
        # Develop Select
        conn_log = sqlite3.connect("log.db")
        cur_log = conn_log.cursor()
        cur_log.execute('select * from DevelopSet')
        for developset_in in cur_log.fetchall():
            if developset_in[0] == 1 and developset_in[1] == 1:
                develop_celebrate = True
            elif developset_in[0] == 2 and developset_in[1] == 1:
                develop_theme_version = True
        conn_log.close()
        # Main Program
        os.system("clear")
        print("+++++Welcome-PyBlog!+++++")
        print("+++++++Made By UTS+++++++")
        print("Github@underthestars-zhy/PyBlog")
        if develop_celebrate and data_cmd():
            print("Celebrate: "+date_celebrate())
        if develop_theme_version:
            print(theme_version)
        print("==========================================")
        print("0: 退出, 1: 设置, 2: 主题, 3: 页面, 99: Develop Set")
        main_set = int(input("选择："))
        if main_set == 0:
            os.system("clear")
            print("++++++Bye-Bye " + user_name_in + "++++++")
            sys.exit()
        elif main_set == 1:
            os.system("clear")
            print("+++++AllSets-PyBlog!+++++")
            print("==========================================")
            print("0: Back, 1:更新账户")
            main_set_sets = int(input("选择: "))
            if main_set_sets == 0:
                continue
            elif main_set_sets == 1:
                os.system("clear")
                print("+++++AllSets-PyBlog!+++++")
                print("++++++++更新账户信息++++++++")
                print("==========================================")
                print("0:Back, 1:Name, 2:Password")
                ac_set_update = int(input("选择: "))
                if ac_set_update == 0:
                    continue
                elif ac_set_update == 1:
                    os.system("clear")
                    print("+++++AllSets-PyBlog!+++++")
                    print("++++++++更新账户名称++++++++")
                    print("==========================================")
                    user_name_new = str(input("New_Name: "))
                    conn_log = sqlite3.connect("log.db")
                    cur_log = conn_log.cursor()
                    cur_log.execute("delete from Account where id=1")
                    conn_log.commit()
                    cur_log.execute(
                        '''insert into Account Values(1,'{}','{}')'''.format(user_name_new, user_password_in))
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
                    cur_log.execute(
                        '''insert into Account Values(1,'{}','{}')'''.format(user_name_in, user_password_new))
                    conn_log.commit()
                    conn_log.close()
                    os.system("clear")
                    print("+++++AllSets-PyBlog!+++++")
                    print("++++++账户密码已经更新++++++")
                    print("==========================================")
                    print("请重新登录!")
                    sys.exit()
                else:
                    os.system("clear")
                    print("+++++Error#0-PyBlog!+++++")
                    print("+++++++Made By UTS+++++++")
                    print("Github@underthestars-zhy/PyBlog")
                    print("==========================================")
                    sys.exit()
            else:
                os.system("clear")
                print("+++++Error#0-PyBlog!+++++")
                print("+++++++Made By UTS+++++++")
                print("Github@underthestars-zhy/PyBlog")
                print("==========================================")
                sys.exit()
        elif main_set == 2:
            os.system("clear")
            print("+++++Themes-PyBlog!+++++")
            print("==========================================")
            print("0: Back, 1: 修改主题, 2: 主题设置, 3: About Pages")
            set_mian_theme = int(input("选择: "))
            if set_mian_theme == 0:
                continue
            elif set_mian_theme == 1:
                os.system("clear")
                print("+++++当前主题" + t_name + "+++++")
                print("==========================================")
                print("0: Back 1: 修改")
                theme_set = int(input("选择: "))
                if theme_set == 0:
                    continue
                elif theme_set == 1:
                    os.system("clear")
                    print("+++++请选择你的主题名称,注意大小写+++++")
                    print("==========================================")
                    theme_name_set = str(input("输入名称: "))
                    conn_log = sqlite3.connect("log.db")
                    cur_log = conn_log.cursor()
                    cur_log.execute("delete from Themes where id=1")
                    conn_log.commit()
                    cur_log.execute('''insert into Themes Values(1,'{}')'''.format(theme_name_set))
                    conn_log.commit()
                    conn_log.close()
                    os.system("clear")
                    print("切换完毕")
                    print("==========================================")
                    print("请重新登录")
                    sys.exit()
            elif set_mian_theme == 2:
                os.system("clear")
                from theme_main import *

                theme_tf_in = theme_tf()
                if t_name == 'no themes':
                    os.system("clear")
                    print("+++++Error#4-PyBlog!+++++")
                    print("+++++++Made By UTS+++++++")
                    print("Github@underthestars-zhy/PyBlog")
                    print("==========================================")
                    sys.exit()
                if t_name != theme_tf_in:
                    os.system("clear")
                    print("+++++Error#3-PyBlog!+++++")
                    print("+++++++Made By UTS+++++++")
                    print("Github@underthestars-zhy/PyBlog")
                    print("==========================================")
                    sys.exit()
                if theme_main():
                    from main_txt import *

                    com = main_txt()
                    print("+++++" + t_name + "设置+++++")
                    print("==========================================")
                    print("0: Back, 1: 创建主题主文件" + com)
                    theme_main_set = int(input("选择: "))
                    if theme_main_set == 0:
                        continue
                    elif theme_main_set == 1:
                        from index import *

                        if main_index():
                            os.system("clear")
                            conn_log = sqlite3.connect("log.db")
                            cur_log = conn_log.cursor()
                            cur_log.execute("delete from IndexD where id=1")
                            conn_log.commit()
                            cur_log.execute('''insert into IndexD Values(1,1)''')
                            conn_log.commit()
                            cur_log.execute('select * from IndexD')
                            main_int = 0
                            for main_int_out in cur_log.fetchall():
                                main_int = main_int_out[1]
                            conn_log.close()
                            if main_int == 1:
                                print("+++++OKOKOKOK-PyBlog!+++++")
                                print("+++++++Made By UTS+++++++")
                                print("Github@underthestars-zhy/PyBlog")
                                print("==========================================")
                                time.sleep(3)
                                continue
                            else:
                                os.system("clear")
                                print("+++++Error#8-PyBlog!+++++")
                                print("+++++++Made By UTS+++++++")
                                print("Github@underthestars-zhy/PyBlog")
                                print("==========================================")
                                sys.exit()
                        else:
                            os.system("clear")
                            print("+++++Error#7-PyBlog!+++++")
                            print("+++++++Made By UTS+++++++")
                            print("Github@underthestars-zhy/PyBlog")
                            print("==========================================")
                            conn_log.close()
                            sys.exit()
                    else:
                        conn_log = sqlite3.connect("log.db")
                        cur_log = conn_log.cursor()
                        cur_log.execute('select * from IndexD')
                        index_in = (1, 0)
                        index_out = 0
                        for index in cur_log.fetchall():
                            index_out = index[1]
                        conn_log.close()
                        if index_out == 0:
                            os.system("clear")
                            print("+++++Error#6-PyBlog!+++++")
                            print("+++++++Made By UTS+++++++")
                            print("Github@underthestars-zhy/PyBlog")
                            print("==========================================")
                            sys.exit()
                    os.system("clear")
                    from main_com import *
                    print(theme_main_com(theme_main_set))
                    main_com_set = int(input("选择: "))
                    if main_com_set == 0:
                        continue
                    else:
                        os.system("clear")
                        com_type = [theme_main_set, main_com_set]
                        if com_input(com_type) == "str":
                            os.system("clear")
                            print(int_com([theme_main_set, main_com_set]))
                            str_input = str(input("输入: "))
                            main_input = [theme_main_set, main_com_set, str_input]
                            if com_str(main_input):
                                os.system("clear")
                                print("OK!")
                                print("==========================================")
                                time.sleep(3)
                                continue
                            else:
                                os.system("clear")
                                print("+++++Error#5-PyBlog!+++++")
                                print("+++++++Made By UTS+++++++")
                                print("Github@underthestars-zhy/PyBlog")
                                print("==========================================")
                                sys.exit()
                        else:
                            os.system("clear")
                            print("+++++Error#5-PyBlog!+++++")
                            print("+++++++Made By UTS+++++++")
                            print("Github@underthestars-zhy/PyBlog")
                            print("==========================================")
                            sys.exit()
                else:
                    os.system("clear")
                    print("+++++Error#2-PyBlog!+++++")
                    print("+++++++Made By UTS+++++++")
                    print("Github@underthestars-zhy/PyBlog")
                    print("==========================================")
                    sys.exit()
            elif set_mian_theme == 3:
                try:
                    import markdown
                except:
                    os.system("clear")
                    print("+++++Error#9-PyBlog!+++++")
                    print("+++++++Made By UTS+++++++")
                    print("Github@underthestars-zhy/PyBlog")
                    print("==========================================")
                    print(">>> pip install markdown")
                    sys.exit()
                os.system("clear")
                print("+++++Write-PyBlog!+++++")
                print("==========================================")
                print("0: Back, 1: Upset, 2: Write online")
                about_set = int(input('Choose: '))
                if about_set == 0:
                    continue
                elif about_set == 1:
                    os.system("clear")
                    print("+++++Upset About Page-PyBlog!+++++")
                    print("==========================================")
                    print("Upload your files to the current directory")
                    about_page_name = input('File Nmae: ')
                    about_page_pic = input('Pic URL: ')
                    try:
                        file = open(about_page_name + '.md', 'r')
                        about_txt = str(file.read())
                        file.close()
                    except:
                        os.system("clear")
                        print("+++++Warning#1-PyBlog!+++++")
                        print("+++++++Made By UTS+++++++")
                        print("Github@underthestars-zhy/PyBlog")
                        print("==========================================")
                        print("Please Retry")
                        import time
                        time.sleep(2)
                        continue
                    from theme_write import *
                    from datetime import *
                    today = datetime.now()
                    if page_write('about', 'about.html', datetime.date(today), about_txt, about_page_pic):
                        os.system('clear')
                        sql_1 = str(datetime.date(today))
                        sql_2 = str(markdown.markdown(about_txt))
                        conn_log = sqlite3.connect("log.db")
                        cur_log = conn_log.cursor()
                        cur_log.execute(
                            '''insert into BackUp_Pages Values('About','about.html','{0}','{1}','{2}','{3}')'''.format(
                                sql_1, sql_2, about_txt, about_page_pic
                            )
                        )
                        conn_log.commit()
                        conn_log.close()
                        print("+++++Upload About Page-PyBlog!+++++")
                        print("==========================================")
                        print("Success!")
                        import time
                        time.sleep(2)
                        continue
                    else:
                        os.system("clear")
                        print("+++++Warning#0-PyBlog!+++++")
                        print("+++++++Made By UTS+++++++")
                        print("Github@underthestars-zhy/PyBlog")
                        print("==========================================")
                        print("Please Retry")
                        import time
                        time.sleep(2)
                        continue
                elif about_set == 2:
                    os.system("clear")
                    print("+++++Write About Page-PyBlog!+++++")
                    print("==========================================")
                    print("Please write below, if the writing is completed, please enter: WriteOK")
                    i = True
                    import random
                    file_name = str(int(random.uniform(0,10)))+str(int(random.uniform(0,10)))+str(int(random.uniform(0,10)))+".md"
                    file = open(file_name, 'a')
                    while i:
                        input_txt = str(input())
                        if input_txt != "WriteOK":
                            file.write(input_txt + "\r")
                        else:
                            i = False
                    file.close()
                    print("输入成功!")
                    time.sleep(1)
                    os.system('clear')
                    about_page_pic = input('Pic URL: ')
                    try:
                        file = open(file_name, 'r')
                        about_txt = str(file.read())
                        file.close()
                    except:
                        os.system("clear")
                        print("+++++Warning#1-PyBlog!+++++")
                        print("+++++++Made By UTS+++++++")
                        print("Github@underthestars-zhy/PyBlog")
                        print("==========================================")
                        print("Please Retry")
                        import time
                        time.sleep(2)
                        continue
                    os.system('''rm {0}'''.format(file_name))
                    from theme_write import *
                    from datetime import *
                    today = datetime.now()
                    if page_write('about', datetime.date(today), about_txt, about_page_pic):
                        os.system('clear')
                        sql_1 = str(datetime.date(today))
                        sql_2 = str(markdown.markdown(about_txt))
                        conn_log = sqlite3.connect("log.db")
                        cur_log = conn_log.cursor()
                        cur_log.execute(
                            '''insert into BackUp_Pages Values('About','about.html','{0}','{1}','{2}','{3}')'''.format(
                                sql_1, sql_2, about_txt, about_page_pic
                            )
                        )
                        conn_log.commit()
                        conn_log.close()
                        print("+++++Up About Page-PyBlog!+++++")
                        print("==========================================")
                        print("Success!")
                        import time
                        time.sleep(2)
                        continue
                    else:
                        os.system("clear")
                        print("+++++Warning#0-PyBlog!+++++")
                        print("+++++++Made By UTS+++++++")
                        print("Github@underthestars-zhy/PyBlog")
                        print("==========================================")
                        print("Please Retry")
                        import time
                        time.sleep(2)
                        continue
                else:
                    os.system("clear")
                    print("+++++Error#0-PyBlog!+++++")
                    print("+++++++Made By UTS+++++++")
                    print("Github@underthestars-zhy/PyBlog")
                    print("==========================================")
                    sys.exit()
            else:
                os.system("clear")
                print("+++++Error#0-PyBlog!+++++")
                print("+++++++Made By UTS+++++++")
                print("Github@underthestars-zhy/PyBlog")
                print("==========================================")
                sys.exit()
        elif main_set == 3:
            os.system("clear")
            print("+++++Pages-PyBlog!+++++")
            print("==========================================")
            print("0: Back, 1: New, 2: Look")
            article_set = int(input("Choose: "))
            if article_set == 0:
                continue
            elif article_set == 1:
                try:
                    import markdown
                except:
                    os.system("clear")
                    print("+++++Error#9-PyBlog!+++++")
                    print("+++++++Made By UTS+++++++")
                    print("Github@underthestars-zhy/PyBlog")
                    print("==========================================")
                    print(">>> pip install markdown")
                    sys.exit()
                os.system('clear')
                print("+++++Write Pages-PyBlog!+++++")
                print("==========================================")
                print("0: Back, 1: Up, 2: Write online")
                write_set = int(input())
                if write_set == 0:
                    continue
                elif write_set == 1:
                    os.system('clear')
                    print("+++++Upload Page-PyBlog!+++++")
                    print("==========================================")
                    print("Upload your files to the current directory")
                    page_name = input('File Nmae: ')
                    page_url = input('File Path: ')
                    page_Main = input('Page Name: ')
                    file = open(page_name, 'r')
                    page_txt = str(file.read())
                    file.close()
                    from theme_write import *
                else:
                    os.system("clear")
                    print("+++++Error#0-PyBlog!+++++")
                    print("+++++++Made By UTS+++++++")
                    print("Github@underthestars-zhy/PyBlog")
                    print("==========================================")
                    sys.exit()
            else:
                os.system("clear")
                print("+++++Error#0-PyBlog!+++++")
                print("+++++++Made By UTS+++++++")
                print("Github@underthestars-zhy/PyBlog")
                print("==========================================")
                sys.exit()
        elif main_set == 99:
            os.system("clear")
            print("+++++Develop Set-PyBlog!+++++")
            print("+++++++Made By UTS+++++++")
            print("Github@underthestars-zhy/PyBlog")
            print("==========================================")
            print("0: Back")
            print("1: Special date celebration (will take up a small amount of resources): " + str(develop_celebrate))
            print("2: View the current theme version and the latest theme version on the homepage (requires theme support): " + str(develop_theme_version))
            develop_set_input = int(input())
            if develop_set_input == 0:
                continue
            elif develop_set_input == 1 and develop_celebrate == False:
                conn_log = sqlite3.connect("log.db")
                cur_log = conn_log.cursor()
                cur_log.execute('''update DevelopSet set tf = 1 where id=1''')
                conn_log.commit()
                conn_log.close()
                os.system("clear")
                print("Develop Set SUCCESS")
                print("==========================================")
                print(
                    "The experimental feature is currently being used. This feature has not been fully tested and may cause unpredictable consequences.")
                time.sleep(3)
                continue
            elif develop_set_input == 2 and develop_theme_version == False:
                conn_log = sqlite3.connect("log.db")
                cur_log = conn_log.cursor()
                cur_log.execute('''update DevelopSet set tf = 1 where id=2''')
                conn_log.commit()
                conn_log.close()
                try:
                    from theme_main import *

                    os.system("rm version_theme.txt")
                    os.system('wget ' + least_version_url())
                    file = open('version_theme.txt', 'rt')
                    version_theme = str(file.read())
                    file.close()
                    os.system("rm version_theme.txt")
                    theme_version = "当前主题版本: " + version() + " 最新主题版本: " + version_theme
                except:
                    theme_version = "当前主题不支持/你还未安装主题"
                os.system("clear")
                print("Develop Set SUCCESS")
                print("==========================================")
                print(
                    "The experimental feature is currently being used. This feature has not been fully tested and may cause unpredictable consequences.")
                time.sleep(3)
                continue
            elif develop_set_input == 1 and develop_celebrate == True:
                conn_log = sqlite3.connect("log.db")
                cur_log = conn_log.cursor()
                cur_log.execute('''update DevelopSet set tf = 0 where id=1''')
                conn_log.commit()
                conn_log.close()
                develop_web = False
                os.system("clear")
                print("Develop Set SUCCESS")
                print("==========================================")
                print(
                    "The experimental feature is currently being used. This feature has not been fully tested and may cause unpredictable consequences.")
                time.sleep(3)
                continue
            elif develop_set_input == 2 and develop_theme_version == True:
                conn_log = sqlite3.connect("log.db")
                cur_log = conn_log.cursor()
                cur_log.execute('''update DevelopSet set tf = 0 where id=2''')
                conn_log.commit()
                conn_log.close()
                develop_celebrate = False
                os.system("clear")
                print("Develop Set SUCCESS")
                print("==========================================")
                print(
                    "The experimental feature is currently being used. This feature has not been fully tested and may cause unpredictable consequences.")
                time.sleep(3)
                continue
            else:
                os.system("clear")
                print("+++++Error#0-PyBlog!+++++")
                print("+++++++Made By UTS+++++++")
                print("Github@underthestars-zhy/PyBlog")
                print("==========================================")
                sys.exit()
        else:
            os.system("clear")
            print("+++++Error#0-PyBlog!+++++")
            print("+++++++Made By UTS+++++++")
            print("Github@underthestars-zhy/PyBlog")
            print("==========================================")
            sys.exit()