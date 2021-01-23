from tkinter import *
import tkinter as tk        # 使用Tkinter前需要先导入
import tkinter.messagebox   # 要使用messagebox先要导入模块

username = ""
password = ""

window = tk.Tk()  # 第1步，实例化object,建立窗口window
window.title('Login to TKinter')  # 第2步，给窗口的可视化起名字
window.geometry('500x300')  # 第3步，设定窗口的大小(长×宽)#这里的乘是小x
tk.Label(window, text='Welcome to TK', bg='skyblue', font=('Arial', 13), width=300, height=2).pack()


user_name = tk.Label(window, text="UserName: ", bg='white', font=('Arial', 13)).place(x=80, y=50)
user_pwd = tk.Label(window, text="Password: ", bg='white', font=('Arial', 13)).place(x=80, y=90)

user = tk.StringVar()
pwd=tk.StringVar()

userInput = tk.Entry(window, textvariable=user,show=None, font=('Arial', 13))  # 显示成明文形式
userInput.place(x=180, y=50)
pwdInput = tk.Entry(window, textvariable=pwd,show='*', font=('Arial', 13))  # 显示成密文形式
pwdInput.place(x=180, y=90)


def login():
    inputUser = user.get()
    inputPwd = pwd.get()
    if inputPwd == password and inputUser == username and username != "" and password !="":
        tkinter.messagebox.showinfo(title='登录成功',message='欢迎进入TK系统!')           #提示信息对话窗
    else:
        tkinter.messagebox.showinfo(title='提示', message='用户名/密码不正确')

def register():
    def checkInfo():
     if user.get() != "" and pwd.get() != "":
        global username
        global password
        username = user.get()
        password = pwd.get()
        tkinter.messagebox.showinfo(title='成功', message='注册成功！欢迎加入TK！')
        wnd.destroy()

    wnd = tk.Toplevel()   # 第1步，实例化object,建立窗口window
    wnd.title('Register')  # 第2步，给窗口的可视化起名字
    wnd.geometry('500x300')  # 第3步，设定窗口的大小(长×宽)#这里的乘是小x
    tk.Label(wnd, text='Join to TK', bg='skyblue', font=('Arial', 13), width=300, height=2).pack()

    user_name = tk.Label(wnd, text="UserName: ", bg='white', font=('Arial', 13)).place(x=80, y=50)
    user_pwd = tk.Label(wnd, text="Password: ", bg='white', font=('Arial', 13)).place(x=80, y=90)

    user = tk.StringVar()
    pwd = tk.StringVar()

    userInput = tk.Entry(wnd,textvariable=user, show=None, font=('Arial', 13))  # 显示成明文形式
    userInput.place(x=180, y=50)
    pwdInput = tk.Entry(wnd, textvariable=pwd, show=None, font=('Arial', 13))
    pwdInput.place(x=180, y=90)

    RegisterBtn = tk.Button(wnd, text='Register', bg='green', font=('Arial', 10), width=10, height=1, command=checkInfo)
    RegisterBtn.place(x=200, y=170)



loginBtn = tk.Button(window, text='Login', bg='skyblue', font=('Arial', 10), width=10, height=1,command=login)
loginBtn.place(x=200, y=130)
RegisterBtn = tk.Button(window, text='Register', bg='green', font=('Arial', 10), width=10, height=1,command=register)
RegisterBtn.place(x=200, y=170)

window.mainloop()











