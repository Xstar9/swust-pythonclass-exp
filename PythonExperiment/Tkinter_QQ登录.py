'''用户登陆界面程序
编写一个用户登录界面，用户可以登录账户信息，如果账户已经存在，可以直接登录，
登录名或者登录密码输入错误会提示，如果账户不存在，提示用户注册，点击注册进去注册页面，
输入注册信息，确定后便可以返回登录界面进行登录。
'''
import tkinter as tk
import tkinter.messagebox
import pickle

#1. 窗口
window = tk.Tk()               # 第1步，实例化object，建立窗口window
window.title('用户登录界面')    # 第2步，给窗口的可视化起名字
window.geometry('400x600')     # 第3步，设定窗口的大小(长 * 宽)

#画布放置图片
canvas=tk.Canvas(window,height=600,width=400)
imagefile=tk.PhotoImage(file='QQ.png')
image=canvas.create_image(0,0,anchor='nw',image=imagefile)
canvas.pack(side='top')

#标签 用户名密码
tk.Label(window,text='用户名:',bg='blue', fg='white',font=('Arial', 12)).place(x=60,y=321)
tk.Label(window,text='密码:',bg='blue', fg='white',font=('Arial',12)).place(x=60,y=362)

#用户名输入框
var_usr_name=tk.StringVar()
entry_usr_name=tk.Entry(window,textvariable=var_usr_name,font=('Arial', 14))
entry_usr_name.place(x=130,y=320)
#密码输入框
var_usr_pwd=tk.StringVar()
entry_usr_pwd=tk.Entry(window,textvariable=var_usr_pwd,show='*',font=('Arial', 14))
entry_usr_pwd.place(x=130,y=360)

#1.登录函数
def usr_log_in():
    #输入框获取用户名及密码
    usr_name=var_usr_name.get();
    usr_pwd = var_usr_pwd.get()
    # 从本地字典获取用户信息，如果没有则新建本地数据库
    try:
        with open('usr_info.pickle', 'rb') as usr_file:
            usrs_info = pickle.load(usr_file)
    except FileNotFoundError:  #异常处理
        with open('usr_info.pickle', 'wb') as usr_file:
            usrs_info = {'admin': 'admin'}
            pickle.dump(usrs_info, usr_file)
    # 判断用户名和密码是否匹配
    if usr_name in usrs_info:
        if usr_pwd == usrs_info[usr_name]:
            # 提示消息框:【返回”ok”】 tkinter.messagebox.showinfo(消息框标题,提示内容)
            tk.messagebox.showinfo(title='welcome',message='欢迎您：' + usr_name)
        else:
            # 错误消息框【返回”ok”】 tkinter.messagebox.showerror(消息框标题, 错误提示内容)
            tk.messagebox.showerror(message='密码错误')
    # 用户名密码不能为空
    elif usr_name == '' or usr_pwd == '':
        tk.messagebox.showerror(message='用户名或密码为空')
    # 不在数据库中弹出是否注册的框
    else:
        # 是/否对话框【返回True False】：tkinter.messagebox.askyesno(消息框标题,提示内容)
        is_signup = tk.messagebox.askyesno('欢迎', '您还没有注册，是否现在注册')
        if is_signup:
            usr_sign_up()

#2.注册函数
def usr_sign_up():
    # 确认注册时的相应函数
    def signtowcg():
        # 获取输入框内的内容
        nn = new_name.get()
        np = new_pwd.get()
        npf = new_pwd_confirm.get()

        # 本地加载已有用户信息,如果没有则已有用户信息为空
        try:
            with open('usr_info.pickle', 'rb') as usr_file:
                exist_usr_info = pickle.load(usr_file)
        except FileNotFoundError:
            exist_usr_info = {}

        # 检查用户名存在、密码为空、密码前后不一致
        if nn in exist_usr_info:
            tk.messagebox.showerror('错误', '用户名已存在')   #错误消息框【返回”ok”】
        elif np == '' or nn == '':
            tk.messagebox.showerror('错误', '用户名或密码为空')
        elif np != npf:
            tk.messagebox.showerror('错误', '密码前后不一致')
        # 注册信息没有问题则将用户名密码写入数据库
        else:
            exist_usr_info[nn] = np
            with open('usr_info.pickle', 'wb') as usr_file:
                pickle.dump(exist_usr_info, usr_file)

            tk.messagebox.showinfo('欢迎', '注册成功')  # 提示消息框:【返回”ok”】
            # 注册成功关闭注册框
            window_sign_up.destroy()

    # 新建注册界面
    window_sign_up = tk.Toplevel(window)
    window_sign_up.geometry('350x200')
    window_sign_up.title('注册')
    # 用户名变量及标签、输入框
    new_name = tk.StringVar()
    tk.Label(window_sign_up, text='用户名：').place(x=10, y=10)
    tk.Entry(window_sign_up, textvariable=new_name).place(x=150, y=10)
    # 密码变量及标签、输入框
    new_pwd = tk.StringVar()
    tk.Label(window_sign_up, text='请输入密码：').place(x=10, y=50)
    tk.Entry(window_sign_up, textvariable=new_pwd, show='*').place(x=150, y=50)
    # 重复密码变量及标签、输入框
    new_pwd_confirm = tk.StringVar()
    tk.Label(window_sign_up, text='请再次输入密码：').place(x=10, y=90)
    tk.Entry(window_sign_up, textvariable=new_pwd_confirm, show='*').place(x=150, y=90)
    # 确认注册按钮及位置
    bt_confirm_sign_up = tk.Button(window_sign_up, text='确认注册',command=signtowcg)
    bt_confirm_sign_up.place(x=150, y=130)

#3.退出的函数
def usr_sign_quit():
    window.destroy()

#登录 注册按钮
bt_login=tk.Button(window,text='登录',bg='#1BACEB',cursor='',command=usr_log_in)
bt_login.place(x=260,y=400)
bt_logup=tk.Button(window,text='注册',bg='#1BACEB',cursor='',command=usr_sign_up)
bt_logup.place(x=310,y=400)
bt_logquit=tk.Button(window,text='退出',bg='#1BACEB',cursor='',command=usr_sign_quit)
bt_logquit.place(x=360,y=400)

#主循环
window.mainloop()
