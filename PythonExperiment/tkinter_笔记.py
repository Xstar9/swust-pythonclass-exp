import tkinter as tk        # 使用Tkinter前需要先导入
import tkinter.messagebox   # 要使用messagebox先要导入模块
window = tk.Tk()            #第1步，实例化object,建立窗口window
window.title('My Window')   #第2步，给窗口的可视化起名字
window.geometry('500x300')  #第3步，设定窗口的大小(长×宽)#这里的乘是小x

str1 = "(1). 创建主窗口及Label部件（标签）创建使用"
# 第4步，在图形界面上设定标签
i = tk.Label(window, text='Hello! this is Tkinter',bg='green', font=('Arial',12),width=30, height=2)
# 说明: bg 为背景,font为字体, width 为长,height为高，这里的长和高是字符的长和高，比如height=2,就是标签有2个字符这么高
# 第5步，放置标签 Label内容content区域放置位置，自动调节尺寸 #放置lable 的方法有∶1) l.pack(); 2)l.place();
i.pack()
str2 = "(2). Button窗口部件"
var = tk.StringVar()#将label标签的内容设置为字符类型，用var来接收hit_me函数的传出内容用以显示在标签上
b = tk.Label(window, textvariable=var, bg='green', fg='white', font=('Arial',12), width=30, height=2)
b.pack()
# #定义一个函数功能(内容自己自由编写)，供点击Button按键时调用，调用命令参数command=函数名
on_hit = False
def hit_me():
    global on_hit
    if on_hit == False:
        on_hit = True
        var.set('you hit me')
    else:
        on_hit = False
        var.set("")
# #第5步，在窗口界面设置放置Button按键
b = tk.Button(window, text='hit me', font=('Arial',12), width=10, height=1,command=hit_me)
b.pack()
str3 = "(3). Entry窗口部件"
# #第4步，在图形界面上设定输入框控件entry并放置控件
e1 = tk.Entry(window,show='*', font=('Arial', 14))
# #显示成密文形式
e2 = tk.Entry(window, show=None, font=('Arial', 14))#显示成明文形式
e1.pack(),e2.pack()
str4 = "(4). Text窗口部件"
# #第4步，在图形界面上设定输入框控件entry框并放置
e = tk.Entry(window, show = None)#显示成明文形式
e.pack()
# #第5步，定义两个触发事件时的函数insert_point和 insert_end
# # (注意:因为Python 的执行顺序是从上往下,所以函数一定要放在按钮的上面)
def insert_point(): #在鼠标焦点处插入输入内容
    var = e.get()
    tk.insert('insert', var)
def insert_end():#在文本框内容最后接着插入输入内容
    var = e.get()
    tk.insert('end', var)
# #第6步，创建并放置两个按钮分别触发两种情况
b1 = tk.Button(window,text='insert point', width=10,height=2, command=insert_point)
b1.pack()
b2 = tk.Button(window,text='insert end', width=10,height=2, command=insert_end)
b2.pack()
# #第7步，创建并放置一个多行文本框text 用以显示，指定height=3为文本框是三个字符高度
# t = tk.Text(window, height=3)
# t.pack()
# str5 = "(5). Canvas窗口部件"
# #第4步，在图形界面上创建500 * 200大小的画布并放置各种元素
# canvas = tk.Canvas(window, bg='green', height=200, width=500)#说明图片位置，并导入图片到画布上
# #图片位置（相对路径，与.py 文件同一文件夹下，也可以用绝对路径，需要给定图片具体绝对路径)
# image_file = tk.PhotoImage(file='test.png')
# #图片锚定点(n图片顶端的中间点位置)放在画布(250,0)坐标处
# image = canvas.create_image(250,0, anchor='n', image=image_file)
# #定义多边形参数,然后在画布上画出指定图形
# x0, y0,x1,y1 = 100,100,150,150
# line = canvas.create_line(x0-50,y0-50, x1-50, y1-50)                #画直线
# oval = canvas.create_oval(x0+120,y0+50,x1+120, y1+50,fill='red')    #画圆用红色填充
# arc  = canvas.create_arc(x0,y0+50,x1,y1+50,start=0,extent=180)      #画扇形从О度打开收到180度结束
# rect = canvas.create_rectangle(330,30,330+20,30+20)                 #画矩形正方形
# canvas.pack()
# #第6步，触发函数,用来一定指定图形
# def moveit():
#     canvas.move(oval,5,0)
#     #移动圆形oval (也可以改成其他图形名字用以移动—起图形、元素)，按每次(x=5,y=0)步长进行移动
# #第5步，定义一个按钮用来移动指定图形的在画布上的位置
# b = tk.Button(window, text='move item',command=moveit).pack()
str6 = "(6). messageBox窗口部件"
# #第4步，定义触发函数功能
def hit_me():
    tkinter.messagebox.showinfo(title='Hi',message='你好!')           #提示信息对话窗
    # tkinter.messagebox.showwarning(title='Hi', message='有警告!')   #提出警告对话窗
    # tkinter.messagebox.showerror(title='Hi',message='出错了! ')     #提出错误对话窗
    # print(tkinter.messagebox.askquestion(title='Hi', message='你好!'))   #询问选择对话窗return 'yes', 'no'
    # print(tkinter.messagebox.askyesno(title='Hi', message='你好! '))     # return 'True', 'False'
    # print(tkinter.messagebox.askokcancel(title='Hi', message='你好!'))   # return 'True', 'False'
# #第4步，在图形界面上创建一个标签用以显示内容并放置
tk.Button(window, text='hit me', bg='green', font=('Arial', 14),command=hit_me).pack()
str7 = "(7). 窗口部件三种放置方式pack/grid/place"
'''第4步, grid放置方法，grid是方格,所以所有的内容会被放在这些规律的方格中'''
# for i in range(3):
#     for j in range(3):
#         tk.Label(window,text=1).grid(row=i, column=j, padx=10, pady=10,ipadx=20,ipady=10)
# # 以上的代码就是创建一个三行三列的表格,其实grid 就是用表格的形式定位的。
# # 这里的参数row 为行, colum为列, padx就是单元格左右间距, pady 就是单元格上下间距,
# # ipadx是单元格内部元素与单元格的左右间距， ipady是单元格内部元素与单元格的上下间距。
'''第4步, pack放置方法，我们常用的pack()，他会按照上下左右的方式排列.例如︰'''
# tk.Label(window, text='上', fg='red').pack(side='top')       # 上
# tk.Label(window, text='下', fg='blue').pack(side='bottom')   # 下
# tk.Label(window, text='左', fg='black').pack(side='left')    # 左
# tk.Label(window, text='右', fg='green').pack(side='right')   # 右
'''第4步, place放置方法（精准的放置到指定坐标点的位置上)'''
# tk.Label(window, text='PLACE', font=('Arial' , 20), ).place(x=50, y=100, anchor='nw')
# 比较容易理解，就是给精确的坐标来定位，如此处给的(50，100)，就是将这个部件放在坐标为(x=50, y=100)的这个位置
# 后面的参数anchor='nw '就是前面所讲的锚定点是西北角,可以不写。

window.mainloop()  # 最后一步，主窗口循环显示
# 注意，loop因为是循环的意思, window.mainloop就会让window不断的刷新，
# 如果没有mainloop,就是一个静态的 window,传入进去的值就不会有循环，
# mainloop 就相当于一个很大的while循环，有个while，每点击一次就会更新一次,所以我们必须要有循环
#所有的窗口文件都必须有类似的mainloop函数, mainloop是窗口文件的关


