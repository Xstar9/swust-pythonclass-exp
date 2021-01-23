import  turtle as tt
'''
    一些常用的函数：
1）turtle.pensize()：设置线条的粗细；
2）turtle.speed()：设置绘制的速度，1-10，1最慢，10最快；
3）turtle.begin_fill()：准备开始填充图形；
4）turtle.circle(50,angle,steps=3)：circle函数在之前用到过，是画一个半径为radius的圆，这里是扩展，steps表示在半径为50的圆内的内置steps多边形；
5）turtle.end_fill()：填充完成；
6）turtle.write(s,font=(“font-name”,font_size,”font_type”))：写文本，s为文本内容，font是字体的参数，里面分别为字体名称，大小和类型；
7）turtle.hideturtle()：隐藏箭头显示；
8）turtle.backward(d)：与forward()函数对应，这里是从尾部绘制线条和箭头到头部；
9）turtle.left(angle)：逆时针转动箭头方向；
10）turtle.undo()：撤销上一个turtle动作；
11）turtle.screensize(w,h)：设置turtle窗口的长和宽；
12）turtle.clear()：清空turtle窗口，但是turtle的位置和状态不会改变；
13）turtle.reset()：清空窗口，重置turtle状态为起始状态；
14）turtle.showturtle()：与hideturtle()函数对应；
15）turtle.filling()：返回当前是否在填充状态；true为filling，false为not filling；
16）turtle.isvisible()：返回当前turtle是否可见。
17）turtle.pos() :
'''
pen = tt.Turtle()  # 定义画笔实例
pen.up()
pen.goto(0,-100)
pen.down()
pen.begin_fill()
pen.fillcolor('#FDCF1F')
pen.circle(200)
pen.end_fill()

pen.begin_fill()
pen.fillcolor('white')
pen.up()
pen.goto(70,110)
pen.down()
pen.circle(50)
pen.end_fill()

pen.begin_fill()
pen.fillcolor('white')
pen.up()
pen.goto(-70,110)
pen.down()
pen.circle(50)
pen.end_fill()

pen.begin_fill()
pen.fillcolor('brown')
pen.up()
pen.goto(-70,150)
pen.down()
pen.circle(10)
pen.end_fill()

pen.begin_fill()
pen.fillcolor('brown')
pen.up()
pen.goto(70,150)
pen.down()
pen.circle(10)
pen.end_fill()

pen.begin_fill()
pen.fillcolor('red')
pen.up()
pen.goto(80,80)
pen.down()
pen.goto(-80,80)
pen.seth(270)
a=0
for i in range(60):
    if 0<=i<15 or  30<=i<45:
        a+=0.53
        pen.lt(3)
        pen.fd(a)
    else:
        a-= 0.53
        pen.lt(3)
        pen.fd(a)
pen.end_fill()


pen.begin_fill()
pen.fillcolor('white')
pen.seth(270)
pen.up()
pen.goto(55,80)
pen.down()
pen.goto(50,70)
pen.goto(-50,70)
pen.goto(-55,80)
pen.end_fill()

pen.up()
pen.goto(-37,20)
pen.seth(60)

pen.begin_fill()
pen.fillcolor('#B22222')
pen.circle(-44,60)
pen.circle(-44,60)
pen.seth(240)
pen.circle(-44.5,60)
pen.circle(-44.5,60)
pen.hideturtle()
pen.end_fill()

tt.hideturtle()
tt.done()




