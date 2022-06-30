
import socket
import sys
import tkinter
import webbrowser as web

from ctypes import WinDLL


from pickletools import read_int4

from time import *
from tkinter import *
from tkinter import PhotoImage, Radiobutton, messagebox, simpledialog,PhotoImage


import wmi
from psutil import cpu_count

root= tkinter.Tk()
root.resizable(width=False, height=False)
import os
from tkinter.ttk import *

from pynotifier import Notification

#变量初始化

j=0
wi=""

a=1
ip=socket.gethostbyname(socket.gethostname())
pc=wmi.WMI()
os_info=pc.win32_OperatingSystem()[0]
processor=pc.win32_Processor()[0]
gpu=pc.win32_VideoController()[0]

CPu="\nCpu:"+processor.Name
ram=str(float(os_info.TotalVisibleMemorySize)/1048576)
neicun="\nRam:"+ram+"GB"
xianka="\nGpu:"+gpu.Name
cpu=processor.Name
if "i3" in cpu:
    im="D:\\i3.gif"
elif "i5" in cpu:
    im="D:\\i5.gif"
elif "i7" in cpu:
    im="D:\\i7.gif"
elif "i9" in cpu:
    im="D:\\i9.gif"
elif "r3" in cpu:
    im="D:\\r3.gif"
elif "r5" in cpu:
    im="D:\\r5.gif"
elif "r7" in cpu:
    im="D:\\r7.gif"
elif "r9" in cpu:
    im="D:\\r9.gif"
else:
    im="D:\\not.gif"
#函数封装


def rad():
    root.configure(background="red")
def green():
    root.configure(background="green")
def blue():
    root.configure(background="blue")
def white():
    root.configure(background="white")
def yellow():
    root.configure(background="yellow")
def pink():
    root.configure(background="pink")
def black():
    root.configure(background="black")

def chw():
    roott = Toplevel()
    roott.title("程序坞")
    phaho = PhotoImage(file="D:\\ps.gif")
    btnn4 = tkinter.Button(roott, text='ps',image=phaho, width=60, height=45,activebackground="blue",activeforeground="white"  ,font=(None, 15), command=lambda:no())


    btnn4.grid(row=1)
    phoho = PhotoImage(file="D:\\sm.gif")
    btnn4 = tkinter.Button(roott, text='ps',image=phoho, width=60, height=45,activebackground="blue",activeforeground="white"  ,font=(None, 15), command=lambda:no())


    btnn4.grid(row=1,column=4)
    roott.mainloop()
def html():
    root4 = tkinter.Tk()
    root4.title("html编辑器")
    root4.geometry("650x450")
    def bianxie():
        html1=simpledialog.askstring('wendang',"输入文件名")
        html1="D:\\"+html1+".html"
        with open(html1,'w') as f:
            message = ent.get("1.0","end")
            f.write(message)
        web.open(html1,new = 1)
    def chru():
        nome=simpledialog.askstring('文档',"输入你要插入的文档的名称")
        try:
            nome='D:\\'+nome
        except TypeError:
            messagebox.showerror('错误提示', '请输入有效名字')
        else:
            try:
                with open (nome,"r")  as fle:
                    print(" ")
                    

                    wi=fle.read()
                    print(wi)
                    fle.close
            except FileNotFoundError:
                messagebox.showerror('错误提示', '请输入有效地址')
            else:
                ent.insert("1.0",wi)
    scr1=tkinter.Scrollbar(root4) 
    scr1.pack(side='right')
    btnn = tkinter.Button(root4, text='运行', font=(None, 12), command=lambda: bianxie())
    btnn.pack()
    btnw = tkinter.Button(root4, text='插入', font=(None, 12), command=lambda: chru())
    btnw.pack()
    ent =tkinter.Text(root4, height=400,bd=10,font=(None, 15))
    ent.pack(side='left',expand=True)
    ent.config(yscrollcommand = scr1.set)
    scr1.config(command = ent.yview)


    root4.mainloop()
def liulan():

    wenti=simpledialog.askstring('浏览器',"输入你要搜索的网页")
    try:
        url =wenti
        web.open(url)
    except TypeError:
        messagebox.showerror('错误提示', '404\n未找到,请输入有效网址')
    else:
        url =wenti
        web.open(url)
def shijian():
    time=strftime(":%d:%H:%M")
    messagebox.showinfo(title = "时间", message=f"本地时间是{time}")
def no():
    messagebox.showwarning(title = "404 not found", message = "程序未开发")
def shezhi():
    print(im)
    wind= Toplevel()
    wind.title("配置")
    phto = PhotoImage(file=im)
    peizhi=(CPu+xianka+neicun+"\nip地址"+ip+'\nOS:ABCos py-tk2.0')
    lbl =Label(wind, text=peizhi)
    lbl.grid(column=0, row=0)
    #file：t图⽚路径
    imw =Label(wind,image=phto)#把图⽚整合到标签类中
    imw.grid()
    
    wind.mainloop()
    
def wendang():
    print(" ")
    def bianxie():
        global mingzi
        mingzi=simpledialog.askstring('文档',"输入你要文档的名称")
        try:
            ming="D:\\"+mingzi
        except TypeError:
            messagebox.showerror('错误提示', '请输入有效名字')
        else:
            with open (ming,"a+")  as file:
                print(" ")
                file.write(w)
                file.closed
    def charu():
        
        
        nome=simpledialog.askstring('文档',"输入你要插入的文档的名称")
        try:
            nome='D:\\'+nome
        except TypeError:
            messagebox.showerror('错误提示', '未找到')
       
        try:
            global wi
            with open (nome,"r")  as fle:
                print(" ")
                
                try:
                    wi=fle.read()
                except UnicodeDecodeError:
                    messagebox.showerror('错误提示', '路径有误')
                else:
                    wi=fle.read()
                
                fle.close
        except FileNotFoundError:
            messagebox.showerror('错误提示', '无法识别此文档\n请插入纯文本文件')
        else:
            
            entc.insert("1.0",wi)
            
    def qingkong():

        entc.delete("1.0",END)
    root5=Tk()
    
    entc =tkinter.Text(root5, height=40,bd=10,font=(None, 15))
    entc.pack(side='left',expand=True)
    w=entc.get("1.0","end")
    btnnm = tkinter.Button(root5, text='保存', font=(None, 12), command=lambda: bianxie())
    btnnm.pack()
    btnnm = tkinter.Button(root5, text='插入', font=(None, 12), command=lambda: charu())
    btnnm.pack()
    btnnm = tkinter.Button(root5, text='清空所有', font=(None, 12), command=lambda:qingkong())
    btnnm.pack()
    root5.mainloop() 
def yanse ():
    root2= tkinter.Tk()
    rad1 = Radiobutton(root2, text="红", value=1, command=lambda: rad())
    rad2 = Radiobutton(root2, text="绿", value=2, command=lambda: green())
    rad3 = Radiobutton(root2, text="蓝", value=3, command=lambda: blue())
    rad4= Radiobutton(root2, text="白", value=4, command=lambda: white())
    rad5 = Radiobutton(root2, text="黄", value=5, command=lambda: yellow())
    rad6 = Radiobutton(root2, text="粉", value=6, command=lambda: pink())
    rad7 = Radiobutton(root2, text="黑", value=1, command=lambda: black())
    rad1.grid(column=0, row=0)
    rad2.grid(column=1, row=0)
    rad3.grid(column=2, row=0)
    rad4.grid(column=3, row=0)
    rad5.grid(column=4, row=0)
    rad6.grid(column=5, row=0)
    rad7.grid(column=6, row=0)
    root2.mainloop()
def quit1():
    
    root.destroy()
    sys.exit(0)
def jisuan():
    import glob
    import tkinter
    from tkinter import font
    from turtle import end_fill
    x=""

    wi=""   
    roont= tkinter.Tk()
    roont.title("计算器")
    roont.geometry("300x250")
    roont.resizable(0,0)
    entnc = tkinter.Entry(roont ,width=35,bd=5,font=(None,10))
    entnc.grid(columnspan=70,padx=10)
    def tianjia(y):
        global wi
        global x

        wi=wi+y
        entnc.delete("0","end")
        entnc.insert("0",wi)
        return wi,x
    def clear():
        global x
        global wi
        global y
        entnc.delete("0","end")
        wi=""
        x=1
        y=""
        return x,wi,y
    def jisuan():
        global wi
        global j
        try:
            try:

                j=eval(wi)

            except ZeroDivisionError :
                messagebox.showerror('错误提示', '请勿将x/0')
        except SyntaxError or  ZeroDivisionError:
            messagebox.showerror('错误提示', '请输入有效算式')
        else:
            try:

                j=eval(wi)

            except ZeroDivisionError :
                messagebox.showerror('错误提示', '请输入有效算式')
            else:
                
                j=eval(wi)
                entnc.delete("0","end")
                entnc.insert("0",j)

                return j
        
    nbtn= tkinter.Button(roont, text='c',background="red",width=2, height=1,activebackground="red",activeforeground="white"  ,font=(None, 15), command=lambda: clear())

    nbtn.grid(row=0,column=0)
    nbtn1= tkinter.Button(roont, text='7',background="gray",width=6, height=2,activebackground="gray",activeforeground="white"  ,font=(None, 15), command=lambda: tianjia("7"))

    nbtn1.grid(row=3,column=2)
    nbtn2= tkinter.Button(roont, text='8', background="gray",width=6, height=2,activebackground="gray",activeforeground="white"  ,font=(None, 15), command=lambda:  tianjia("8"))

    nbtn2.grid(row=3,column=4)
    nbtn3 = tkinter.Button(roont, text='9', background="gray",width=6, height=2,activebackground="gray",activeforeground="white"  ,font=(None, 15), command=lambda:  tianjia("9"))

    nbtn3.grid(row=3,column=6)
    nbtn4= tkinter.Button(roont, text='+', background="gray",width=6, height=2,activebackground="gray",activeforeground="white"  ,font=(None, 15), command=lambda: tianjia("+"))

    nbtn4.grid(row=3,column=8)
    nbtn5 = tkinter.Button(roont, text='4', background="gray",width=6, height=2,activebackground="gray",activeforeground="white"  ,font=(None, 15), command=lambda: tianjia("4"))

    nbtn5.grid(row=5,column=2)
    nbtn6 = tkinter.Button(roont, text='5',background="gray", width=6, height=2,activebackground="gray",activeforeground="white"  ,font=(None, 15), command=lambda:tianjia("5"))

    nbtn6.grid(row=5,column=4)
    nbtn7= tkinter.Button(roont, text='6',background="gray", width=6, height=2,activebackground="gray",activeforeground="white"  ,font=(None, 15), command=lambda: tianjia("6"))

    nbtn7.grid(row=5,column=6)
    nbtn8 = tkinter.Button(roont, text='-',background="gray", width=6, height=2,activebackground="gray",activeforeground="white"  ,font=(None, 15), command=lambda:tianjia("-"))

    nbtn8.grid(row=5,column=8)
    nbtn9= tkinter.Button(roont, text='1',background="gray", width=6, height=2,activebackground="gray",activeforeground="white"  ,font=(None, 15), command=lambda: tianjia("1"))

    nbtn9.grid(row=7,column=2)
    nbtn10 = tkinter.Button(roont, text='2', background="gray",width=6, height=2,activebackground="gray",activeforeground="white"  ,font=(None, 15), command=lambda: tianjia("2"))

    nbtn10.grid(row=7,column=4)
    nbtn11 = tkinter.Button(roont, text='3',background="gray", width=6, height=2,activeforeground="white" ,activebackground="gray" ,font=(None, 15), command=lambda: tianjia("3"))

    nbtn11.grid(row=7,column=6)
    nbtn12= tkinter.Button(roont, text='*',background="gray", width=6, height=2,activeforeground="white" ,activebackground="gray" ,font=(None, 15), command=lambda: tianjia("*"))

    nbtn12.grid(row=7,column=8)
    nbtn13= tkinter.Button(roont, text='.',background="gray", width=6, height=2,activeforeground="white"  ,activebackground="gray",font=(None, 15), command=lambda: tianjia("."))

    nbtn13.grid(row=9,column=2)
    nbtn14= tkinter.Button(roont, text='0',background="gray", width=6, height=2,activeforeground="white" ,activebackground="gray" ,font=(None, 15), command=lambda: tianjia("0"))

    nbtn14.grid(row=9,column=4)
    nbtn15 = tkinter.Button(roont, text='=',background="gray", width=6, height=2,activeforeground="white"  ,activebackground="gray",font=(None, 15), command=lambda: jisuan())

    nbtn15.grid(row=9,column=6)
    nbtn16 = tkinter.Button(roont, text='/', width=6, height=2,background="gray",activebackground="gray",activeforeground="white"  ,font=(None, 15), command=lambda:tianjia("/"))

    nbtn16.grid(row=9,column=8)
    roont.mainloop()
#主体结构

Notification(
	title='hello',
	description='welcome to ABCos',
	
	duration=5,                                   
).send()
sleep(1)
root.title("abc系统")
root.geometry("700x500")
root.configure(background="black")
phato = PhotoImage(file="D:\\sss.gif")
btn = tkinter.Button(root, text='浏览器',image=phato,width=60, height=45,activebackground="blue",activeforeground="white"  ,font=(None, 15), command=lambda: liulan())

btn.grid(row=1,column=3)
phata = PhotoImage(file="D:\\asd.gif")
btn1 = tkinter.Button(root, text='时间',image=phata,width=60, height=45,activebackground="blue",activeforeground="white"  ,font=(None, 15), command=lambda:shijian())

btn1.grid(row=1,column=6)
phatu = PhotoImage(file="D:\\sz.gif")
btn2 = tkinter.Button(root, text='设置',image=phatu, width=60, height=45,activebackground="blue",activeforeground="white"  ,font=(None, 15), command=lambda:shezhi())

btn2.grid(row=1,column=9)
phuto = PhotoImage(file="D:\\tp.gif")   
btn3 = tkinter.Button(root, text='背景',image=phuto,width=60, height=40,activebackground="blue",activeforeground="white"  ,font=(None, 15), command=lambda:yanse())
btn3.grid(row=1,column=12)
phauo = PhotoImage(file="D:\\wd.gif")
btn4 = tkinter.Button(root, text='文档',image=phauo, width=60, height=45,activebackground="blue",activeforeground="white"  ,font=(None, 15), command=lambda:wendang())


btn4.grid(row=1,column=15)
phaoo = PhotoImage(file="D:\\hm.gif")
btn5 = tkinter.Button(root, text='html', width=60,image=phaoo, height=45,activebackground="blue",activeforeground="white"  ,font=(None, 15), command=lambda:html())


btn5.grid(row=1,column=18)
pheto = PhotoImage(file="D:\\jsq.gif")
btn6= tkinter.Button(root, text='计算器',image=pheto, width=60, height=45,activebackground="blue",activeforeground="white"  ,font=(None, 15), command=lambda:jisuan())


btn6.grid(row=1,column=21)
phaeo = PhotoImage(file="D:\\gj.gif")
btn7 = tkinter.Button(root, text='退出',image=phaeo, width=60, height=45,activebackground="red",activeforeground="white"  ,font=(None, 15), command=lambda:quit1())


btn7.grid(row=1,column=24)
phaet = PhotoImage(file="D:\\chw.gif")
btn8= tkinter.Button(root, text='退出',image=phaet, width=60, height=45,activebackground="blue",activeforeground="white"  ,font=(None, 15), command=lambda:chw())
btn8.grid(row=1,column=27)
ph0to = PhotoImage(file="D:\\111.gif")
imw =Label(root,image=ph0to)
imw.grid(row=2,column=2,columnspan=70)
root.mainloop()
