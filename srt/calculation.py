import math
import graphics
import time

#define "×" "*"

# one = 1 #存表达式的第一个数
# def number(s):#s代表一个操作数组
#     global one#one为全局变量
#     if one == 1:
#         one = one + 1
#         if jzh == 10:
#             return float(s)
#
#         return int(s.split('.')[0])
#     else:
#         return float(s)
# def multiply_n(s):
#     s = s.split("F")
#
#     t = shuzi(s[0])
#     for i in range(1,len(s)):
#         t *=shuzi(s[i])
#     return t
# def pingfang_n(s):
#     s = s.split("G")
#     t = shuzi(s[0])
#     for i in range(1,len(s)):
#         t **= multiply_n(s[i])#用于连续计算，下面同理
#     return t
# def div(s):
#     s = s.split("E")
#     t = chen(s[0])
#     for i in range(1, len(s)):
#         t /= pingfang_ns[i])
# def jian_n(s):#减法
#     s = s.split("B")
#     t=yu(s[0])
#     for i in range(1,len(s)):
#         t-=div(s[i])
#     return t
# def plus_n(s):#加法
#     s=s.split("A")
#     t=0
#     for i in s:
#         t+=jian_n(i)
#     return t
# def sqrt_n(s):
#     t = plus_n(s)
#     if t%1 == 0:
#         t = int(t)
#     sq = math.sqrt(t)
#     if sq%1==0:
#         return int(sq)
#     return sq

def jisuan(t):

    middle = ''
    i = 0
    while i < len(t):
        wd_2 = t[i:i + 2]
        wd_3 = t[i:i + 3]
        wd_4 = t[i:i + 4]
        if (wd_2 == 'ln' or wd_3 == 'sin' or wd_3 == 'cos' or wd_3 == 'tan' or wd_3 == 'log' or wd_4 == 'asin' or wd_4 == 'acos' or wd_4 == 'atan' or wd_4 == 'sqrt'):
            level = 1
            if (wd_2 == 'ln'):
                level = 2
            elif (wd_3 == 'sin' or wd_3 == 'cos' or wd_3 == 'tan' or wd_3 == 'log'):
                level = 3
            elif (wd_4 == 'asin' or wd_4 == 'acos' or wd_4 == 'atan' or wd_4 == 'sqrt'):
                level = 4
            if (level == 3):
                if (wd_3 == 'log'):
                    middle = middle + 'math.log'
                if (wd_3 == 'sin'):
                    middle = middle + 'math.sin'
                if (wd_3 == 'cos'):
                    middle = middle + 'math.cos'
                if (wd_3 == 'tan'):
                    middle = middle + 'math.tan'
            if (level == 4):
                if (wd_4 == 'sqrt'):
                    middle = middle + 'math.sqrt'
                if (wd_4 == 'asin'):
                    middle = middle + 'math.asin'
                if (wd_4 == 'acos'):
                    middle = middle + 'math.acos'
                if (wd_4 == 'atan'):
                    middle = middle + 'math.tan'
            i += level
        else:
            middle += t[i]
            i = i + 1

    result = eval(middle)
    list(t).clear()
    list(middle).clear()
    list(t).append(str(result))
    return result


class Button:
    def __init__(self,width = None,height = None, x = None, y = None, text = None,color1 = None,color2 = None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.text = text

        self.color1 = color1#按键颜色
        self.color2 = color2#窗口颜色

        self.st = graphics.Point(x,y) #基础坐标点

        p1 = self.st.clone()
        p2 = self.st.clone() #按钮的对角线点

        p1.move(-self.width / 2, -self.height / 2)
        p2.move(self.width / 2, self.height / 2)#p1p2左下右上位移形成对角线
        #这种设置的优点为st为中心点 可以把文本放在st点上
        self.sq = graphics.Rectangle(p1, p2)#形成矩形 graphics的具体操作请参考
                # https://blog.csdn.net/qq_45940395/article/details/111704989的具体内容
        self.sq.setFill(color1)#填充色
        self.sq.setOutline(color2)#边框色
        self.square_text = graphics.Text(self.st,self.text)
    def show(self,win):
        self.sq.draw(win)
        self.square_text.draw(win)

    def change(self,color):#按键反馈
        self.sq.setFill(color)
        time.sleep(0.20)
        self.sq.setFill(self.color1)

    def click_co(self,p,color):#点击
        s1 = self.sq.getP1()
        s2 = self.sq.getP2()#返回矩形对角点
        if p.getX() >= s1.getX() and p.getX() <= s2.getX():
            if p.getY() >= s1.getY() and p.getY() <= s2.getY():
                return self.text
class text:
    def __init__(self,x=None, y=None, text=None, size=None, pianyi=None):
        self.x = x
        self.y = y
        self.text = text#数据
        self.txt = text#数据计算
        self.size = size #字体大小
        self.pianyi = pianyi
        self.pianyi_size = 0#偏移数
        self.st = graphics.Point(x, y)
        self.cr = graphics.Text(self.st, text)
        self.cr.setSize(size)

    def show(self,win):
        self.cr.draw(win)

    #靠右站
    def gx(self, g, s):  # 更改偏移量
        if g == True:
            self.pianyi_size += s
            self.cr.move(-(self.pianyi) * s, 0)
        else:
            self.pianyi_size -= s
            if self.pianyi_size < 0:
                self.pianyi = 0
            self.cr.move((self.pianyi) * s, 0)
        self.cr.setText(self.text)

def calculation(kuan,gao):
    win = graphics.GraphWin("calculation_102101221_zyf",kuan,gao)

    color1 = graphics.color_rgb(0,191,225)#窗口颜色(浅蓝
    color2 = graphics.color_rgb(165,42,42)#按键边框颜色（深红
    color3 = graphics.color_rgb(255,240,245)#按键颜色（浅肉色
    color4 = graphics.color_rgb(51,0,0)#背景颜色（浅黑色

    win.setBackground(color1)

    #结果框
    end_p = graphics.Point(2,gao / 7)
    end_p2 = graphics.Point(kuan,gao / 7 * 2 + gao / 14)
    square = graphics.Rectangle(end_p,end_p2)
    square.setFill(color3)
    square.setOutline(color4)
    square.draw(win)

    list_button = []

    list_button_text = ("sqrt","(",")","<<",
                   "sin","cos","tan","/",
                   "7","8","9","×",
                   "4","5","6","-",
                   "1","2","3","+",
                   "AC","0",".","=")

    button_wide = (kuan - 20) / 4
    button_high = (gao - 90) / 9

    white = (kuan - button_wide * 4) / 5

    #输出结果
    t1 = text(kuan - 5, gao / 7 + (gao / 7 + gao / 14) / 3 * 2, "", 30, 11)  # 坐标点
    t1.show(win)

    for i in range(0, 6):
        for j in range(0, 4):
            b = Button(button_wide, button_high,
                       button_wide / 2 + white + (white + button_wide) * j + 2,
                       (gao - button_high * 6 - white * 7) + button_high / 2 + (white + button_high) * i,
                       list_button_text[i * 4 + j], color3, color2)  # 退出按键
            list_button.append(b)
            b.show(win)

    while(1):
        i = win.getMouse()
        for j in list_button:
            t = j.click_co(i,color1)
            if t != None:
                if t == "<<":
                    t1.text = t1.text[0:-1]
                    t1.gx(False,1)
                elif t == "=":
                    t1.text = jisuan(t1.text)
                    t1.txt = t1.text
                    t1.gx(True,len(str(t1.txt)))
                elif t == "AC":
                    while(t1.text != None):
                        t1.text = t1.text[0:-1]
                        t1.gx(False,1)
                elif t == "×":
                    t1.text += "*"
                    t1.txt = t1.text
                else:
                    if t == "cos":
                        t1.text += t
                        t1.txt += t
                        t1.gx(True, 3)
                    elif t == "sin":
                        t1.text += t
                        t1.txt += t
                        t1.gx(True, 3)
                    elif t == "tan":
                        t1.text += t
                        t1.txt += t
                        t1.gx(True, 3)
                    else:
                        t1.text += t
                        t1.txt += t
                        t1.gx(True, 1)
                j.change(color1)
                break

if __name__ == '__main__':
    kuan,gao = 1000,580
    calculation(kuan,gao)