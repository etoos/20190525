import turtle as t

s7seg_img = ["7s0.gif", "7s1.gif", "7s2.gif",
             "7s3.gif", "7s4.gif", "7s5.gif",
             "7s6.gif", "7s7.gif", "7s8.gif", "7s9.gif", "7s10.gif"]
def disp_num(k):
    t.shape(s7seg_img[k])
    t.stamp()


def Key_0():
    disp_num(0)
def Key_1():
    disp_num(1)
def Key_2():
    disp_num(2)
def Key_3():
    disp_num(3)
def Key_4():
    disp_num(4)
def Key_5():
    disp_num(5)
def Key_6():
    disp_num(6)
def Key_7():
    disp_num(7)
def Key_8():
    disp_num(8)
def Key_9():
    disp_num(9)
def Key_10():
    disp_num(10)

t.setup(400,400)
s=t.Screen()
t.hideturtle()
t.speed(0)

for i in range(11):
    s.addshape(s7seg_img[i])

disp_num(10)


s.onkeypress(Key_0,"0")
s.onkeypress(Key_1,"1")
s.onkeypress(Key_2,"2")
s.onkeypress(Key_3,"3")
s.onkeypress(Key_4,"4")
s.onkeypress(Key_5,"5")
s.onkeypress(Key_6,"6")
s.onkeypress(Key_7,"7")
s.onkeypress(Key_8,"8")
s.onkeypress(Key_9,"9")
#s.onKeypress(Key_10,"r")


s.onkeyrelease(Key_10,"0")
s.onkeyrelease(Key_10,"1")
s.onkeyrelease(Key_10,"2")
s.onkeyrelease(Key_10,"3")
s.onkeyrelease(Key_10,"4")
s.onkeyrelease(Key_10,"5")
s.onkeyrelease(Key_10,"6")
s.onkeyrelease(Key_10,"7")
s.onkeyrelease(Key_10,"8")
s.onkeyrelease(Key_10,"9")


s.listen()




