'''
使用 Python 标准库 tk 编写 GUI 版本的猜数游戏。
每次猜数之前要启动游戏并设置猜数范围和最大猜测次数等参数，
退出游戏时显示战绩（共玩几次， 猜对几次） 信息。
'''
import tkinter as tk
import tkinter.messagebox
import random

#1. 创建主界面

window = tk.Tk()                    # 生成主窗口
window.title('猜数字游戏')           # 主窗口加标题
window.geometry('500x400')          # 设置主窗口的大小
canvas=tk.Canvas(window,height=400,width=500)
canvas.pack(side='top')

#2. 提示信息（游戏规则，用户输入）,建立文本框，输入框

# 游戏名称和规则文本
label_game = tk.Label(window,fg='black',text="猜数字小游戏",font=('Arial',35,'bold')).place(x=100,y=10)
label_rule = tk.Label(window,fg='red',text="游戏规则：",font=('Arial',15,'bold')).place(x=100,y=80)
label_rule1 = tk.Label(window,fg='blue',text="1.用户设定范围猜数字！！！",font=('Arial',10)).place(x=130,y=110)
label_rule2 = tk.Label(window,fg='blue',text="2.用户限定猜测次数！！！",font=('Arial',10)).place(x=130,y=130)
# 用户设定猜数范围输入框
var_range_min=tk.IntVar()
var_range_max=tk.IntVar()
label_range=tk.Label(window,fg='red',text="请设定猜数范围：",font=('Arial',14,'bold')).place(x=100,y=150)
label_range_min = tk.Label(window,fg='black',text="最小值：",font=('Arial',10)).place(x=120,y=180)
entry_range_min = tk.Entry(window,textvariable=var_range_min,width=5,font=('Arial', 10)).place(x=175,y=180)
label_range_max = tk.Label(window,fg='black',text="最大值：",font=('Arial',10)).place(x=220,y=180)
entry_range_max = tk.Entry(window,textvariable=var_range_max, width=5, font=('Arial', 10)).place(x=275,y=180)
# 用户设定猜数次数限制
var_guess_limitcount=tk.IntVar()
label_guess_limitcount = tk.Label(window,fg='red',text="请设定猜数限制次数：",font=('Arial',14,'bold')).place(x=100,y=210)
entry_guess_limitcount = tk.Entry(window,textvariable=var_guess_limitcount,width=8,font=('Arial', 10)).place(x=300,y=215)
# 用户猜数输入框
var_user_guessnumber=tk.IntVar()
label_user_guessnumber = tk.Label(window,fg='blue',text="请在下方输入你所猜测的数字：",font=('Arial',15,'bold')).place(x=100,y=240)
entry_user_guessnumber = tk.Entry(window,textvariable=var_user_guessnumber,width=15,font=('Arial',12)).place(x=160,y=270)

#3. 猜数字函数，进行游戏

FlagOver = True                # 是否允许进行游戏，用于用户达到猜数次数限制后判定
user_guess_count = 0           # 用户猜数次数
user_guess_count_right = 0     # 用户猜对次数

def GameStart():
    range_min = var_range_min.get()               # 获取猜数范围最小值
    range_max = var_range_max.get()               # 获取猜数范围最大值
    # 生成随机数number，然后获取用户输入的数字，比较大小，然后跳出不同的提示框。
    randnumber = random.randint(range_min,range_max)
    print("min:",range_min,"max:",range_max,"randnumber:",randnumber)
    global user_guess_count_right  # 声明全局变量用户猜对的次数
    # 获取用户猜的数字
    user_guessnumber = var_user_guessnumber.get()
    # 进行比较，并弹出结果
    if user_guessnumber == '':
        # 错误消息框【返回”ok”】 tkinter.messagebox.showerror(消息框标题,错误提示内容)
        tk.messagebox.showerror('警告', '输入不能为空！！！')
    elif user_guessnumber > randnumber:
        # 提示消息框:【返回”ok”】tkinter.messagebox.showinfo(消息框标题,提示内容)
        tk.messagebox.showinfo('不正确', '您输入的数据太大了，下次加油！')
    elif user_guessnumber < randnumber:
        tk.messagebox.showinfo('不正确', '您输入的数据太小了，再来一次！')
    elif user_guessnumber == randnumber:
        user_guess_count_right += 1       # 用户猜对次数加一
        tk.messagebox.showinfo('正确', '恭喜你猜对啦！！！\n你咋这么聪明的呢！赏你个摸摸哒！!')
    else:
        tk.messagebox.showerror('警告', '输入不正确！！！')
    global user_guess_count  # 声明全局变量用户猜测的次数
    global FlagOver
    user_guess_count += 1
    guess_limitcount = var_guess_limitcount.get() # 获取猜数限制次数
    if user_guess_count >= guess_limitcount:      #
        FlagOver =False
def GameOver():
    tk.messagebox.showinfo('本次战绩', '共玩{}次， 猜对{}次'.format(user_guess_count, user_guess_count_right))
    window.destroy()

#4. 用户选择确定猜数结果，或者退出游戏

def LoopClick():
    global FlagOver
    if  FlagOver:
        GameStart()
    else:
        tk.messagebox.showerror('警告', '本次游戏猜测次数已用完\n请点击退出游戏！')

# 建立一个按钮,command：通过按钮触发比较函数
button1 = tk.Button(window, text='确定',bg='skyblue', font=('Arial', 10))
button1.place(x=250,y=300)
button1['command'] = LoopClick
# 建立一个按钮,command：通过按钮触发界面退出，bg是背景颜色
button2 = tk.Button(window, text='退出游戏',font=('Arial', 10),command=GameOver)
button2.place(x=300,y=300)

#5. 主循环
window.mainloop()
