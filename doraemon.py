from turtle import *


def gotos(x, y):
    penup()
    goto(x, y)
    pendown()


# 眼睛
def eyes():
    tracer(False)
    a = 2.5
    for i in range(120):
        if 0 <= i < 30 or 60 <= i < 90:
            a -= 0.05
            lt(3)
            fd(a)
        else:
            a += 0.05
            lt(3)
            fd(a)
    tracer(True)


# 胡须
def beard():
    gotos(-37, 135)
    seth(165)
    fd(60)
    gotos(-37, 125)
    seth(180)
    fd(60)
    gotos(-37, 115)
    seth(193)
    fd(60)
    gotos(37, 135)
    seth(15)
    fd(60)
    gotos(37, 125)
    seth(0)
    fd(60)
    gotos(37, 115)
    seth(-13)
    fd(60)


# 嘴巴
def mouth():
    gotos(5, 148)
    seth(270)
    fd(100)
    seth(0)
    circle(120, 50)
    seth(230)
    circle(-120, 100)


# 围巾
def scarf():
    fillcolor('#e70010')
    begin_fill()
    seth(0)
    fd(200)
    circle(-5, 90)
    fd(10)
    circle(-5, 90)
    fd(207)
    circle(-5, 90)
    fd(10)
    circle(-5, 90)
    end_fill()


# 鼻子
def nose():
    gotos(4, 148)
    fillcolor('#e70010')
    begin_fill()
    circle(20)
    end_fill()


# 黑眼睛
def black_eyes():
    seth(0)
    gotos(-20, 195)
    fillcolor('#000000')
    begin_fill()
    circle(13)
    end_fill()
    pensize(6)
    gotos(20, 205)
    seth(75)
    circle(-10, 150)
    pensize(3)
    gotos(-17, 200)
    seth(0)
    fillcolor('#ffffff')
    begin_fill()
    circle(5)
    end_fill()
    gotos(0, 0)


# 脸
def face():
    fd(183)
    fillcolor('#ffffff')
    begin_fill()
    lt(45)
    circle(120, 100)
    seth(90)
    eyes()
    seth(180)
    penup()
    fd(60)
    pendown()
    seth(90)
    eyes()
    penup()
    seth(180)
    fd(64)
    pendown()
    seth(215)
    circle(120, 100)
    end_fill()


# 头型
def head():
    penup()
    circle(150, 40)
    pendown()
    fillcolor('#00a0de')
    begin_fill()
    circle(150, 280)
    end_fill()


# 画哆啦A梦
def Doraemon():
    # 头部
    head()
    # 围脖
    scarf()
    # 脸
    face()
    # 眼睛
    black_eyes()
    # 红鼻子
    nose()
    # 嘴巴
    mouth()
    # 胡须
    beard()
    # 身体
    gotos(0, 0)
    seth(0)
    penup()
    circle(150, 50)
    pendown()
    seth(30)
    fd(40)
    seth(70)
    circle(-30, 270)
    fillcolor('#00a0de')
    begin_fill()
    seth(230)
    fd(80)
    seth(90)
    circle(1000, 1)
    seth(-89)
    circle(-1000, 10)
    # print(pos())
    seth(180)
    fd(70)
    seth(90)
    circle(30, 180)
    seth(180)
    fd(70)
    # print(pos())
    seth(100)
    circle(-1000, 9)
    seth(-86)
    circle(1000, 2)
    seth(230)
    fd(40)
    # print(pos())
    circle(-30, 230)
    seth(45)
    fd(81)
    seth(0)
    fd(203)
    circle(5, 90)
    fd(10)
    circle(5, 90)
    fd(7)
    seth(40)
    circle(150, 10)
    seth(30)
    fd(40)
    end_fill()
    # 左手
    seth(70)
    fillcolor('#ffffff')
    begin_fill()
    circle(-30)
    end_fill()
    # 脚
    gotos(103.74, -182.59)
    seth(0)
    fillcolor('#ffffff')
    begin_fill()
    fd(15)
    circle(-15, 180)
    fd(90)
    circle(-15, 180)
    fd(10)
    end_fill()
    gotos(-96.26, -182.59)
    seth(180)
    fillcolor('#ffffff')
    begin_fill()
    fd(15)
    circle(15, 180)
    fd(90)
    circle(15, 180)
    fd(10)
    end_fill()
    # 右手
    gotos(-133.97, -91.81)
    seth(50)
    fillcolor('#ffffff')
    begin_fill()
    circle(30)
    end_fill()
    # 口袋
    gotos(-103.42, 15.09)
    seth(0)
    fd(38)
    seth(230)
    begin_fill()
    circle(90, 260)
    end_fill()
    gotos(5, -40)
    seth(0)
    fd(70)
    seth(-90)
    circle(-70, 180)
    seth(0)
    fd(70)
    # 铃铛
    gotos(-103.42, 15.09)
    fd(90)
    seth(70)
    fillcolor('#ffd200')
    # print(pos())
    begin_fill()
    circle(-20)
    end_fill()
    seth(170)
    fillcolor('#ffd200')
    begin_fill()
    circle(-2, 180)
    seth(10)
    circle(-100, 22)
    circle(-2, 180)
    seth(180 - 10)
    circle(100, 22)
    end_fill()
    goto(-13.42, 15.09)
    seth(250)
    circle(20, 110)
    seth(90)
    fd(15)
    dot(10)
    gotos(0, -150)


if __name__ == '__main__':
    setup(1.0, 1.0)
    title("Doraemon")
    bgcolor('skyblue')
    speed(0)
    pensize(3)
    hideturtle()
    Doraemon()
    gotos(300, -200)
    color('pink')
    write('老\n婆\n，\n我\n永\n远\n爱\n你', font=("Bradley Hand ITC", 33, "bold"))
    mainloop()
