from re import X
import tkinter
import pymongo
from tkinter import messagebox,Toplevel
client = pymongo.MongoClient(host= '127.0.0.1', port=27017)
db = client.testdb
coll = db.get_collection("namedb")
result=""




def zhuce():
    global ans3,ans2
    def zhucebox(x,y):
        global ans2,ans3
        ans2= x
        ans3= y
        find_post = coll.find_one({'name' : ans2})
        try:
            upk=len(find_post["name"] )
        except TypeError:
            
            if len(ans2)>1 and len(ans2)<10 and len(ans3)>1 and len(ans3)<10:
                longo={"name":ans2,"password":ans3}
                result = coll.insert_one(longo)
                root.destroy()

                messagebox.showinfo('成功', '注册成功') 

            else:
                messagebox.showerror('错误提示', '命名或密码错误')
                root.destroy()
        else:
            messagebox.showerror('错误提示', '该账户已被占用')
            root.destroy()
    root=Toplevel()
    root.title("注册")
    label=tkinter.Label(root,text="请输入名字和密码1--10")
    label.grid(row=0,column=0)

    ent = tkinter.Entry(root, font=(None, 15))
    ent.grid(row=3,column=0)

    ent2 = tkinter.Entry(root, font=(None, 15))
    ent2.grid(row=6,column=0)

    nbt= tkinter.Button(root, text='提交' ,font=(None, 15), command=lambda:zhucebox(ent.get(),ent2.get()))

    nbt.grid(row=8,column=0)

    
    root.mainloop()
def denglu():
    def denglubox(x)  :
        find_post = coll.find_one({'password' : x})
        try:
            passw=find_post["password"]
        except TypeError:
            roo3.destroy()
            messagebox.showerror('错误提示', '密码不正确')
        else:
            passw=find_post["password"]
            print(passw)
            if passw==x:
                roo3.destroy()

                messagebox.showinfo('欢迎', '你好'+find_post["name"]+"登陆成功")
            else:
                roo3.destroy()
                messagebox.showerror('错误提示', '密码错误')
    roo3=Toplevel()
    root2.title("登录")
    label=tkinter.Label(roo3,text="请输入密码")
    label.grid(row=0,column=0)
    enn = tkinter.Entry(roo3, font=(None, 15))
    enn.grid(row=3,column=0)
    nbt= tkinter.Button(roo3, text='登录' ,font=(None, 15), command=lambda:denglubox(enn.get()))

    nbt.grid(row=8,column=0)
    
    roo3.mainloop()
def zhuxiao():
    def zhuxiaobox(x,y):
        find_post = coll.find_one({'name' : x})
        print(find_post)
        try:
            passw=find_post["password"]
        except TypeError or KeyError :
            roo4.destroy()
            messagebox.showerror('错误提示', '账户错误或不存在')
        else:
            print(find_post)
            passw=find_post["password"]
            if passw==y:
                an=messagebox.askyesno('确认操作', '确定执行？')
                
                if an==True:
                    result = coll.delete_many({'name' : x})
                    roo4.destroy()
                    messagebox.showinfo('成功', "注销成功")
                else:
                    roo4.destroy()
                    messagebox.showinfo('成功', "取消成功")
                
            else:
                roo4.destroy()
                messagebox.showerror('错误提示', '密码错误')
    roo4=Toplevel()
    roo4.title("注销")
    label=tkinter.Label(roo4,text="请输入密码和用户名")
    label.grid(row=0,column=0)
    ent = tkinter.Entry(roo4, font=(None, 15))
    ent.grid(row=3,column=0)

    ent2 = tkinter.Entry(roo4, font=(None, 15))
    ent2.grid(row=6,column=0)

    nbt= tkinter.Button(roo4, text='提交' ,font=(None, 15), command=lambda:zhuxiaobox(ent.get(),ent2.get()))

    nbt.grid(row=8,column=0)

    
    roo4.mainloop()
def genggai():
    def genggaibox(x,y):
        def genggaibox2(x,y):
    
            if len(x)>1 and len(x)<10 and len(y)>1 and len(y)<10:
                an=messagebox.askyesno('确认操作', '确定执行？')
                
                if an ==True:
                    condition = {'name' : ans2}
                    pty={'$set' : {'name' : x,"password":y}}
                    result = coll.update_one(condition, pty)
                elif an==False:
                    roo5.destroy()
                    messagebox.showinfo('取消', '成功')
                
            else:
                roo5.destroy()
                messagebox.showerror('错误提示', '输入错误') 
        
       
        global ans2
        ans2=x
        find_post = coll.find_one({'name' : x})
        try:
            passw=find_post["password"]
            nam=find_post["name"]
        except TypeError:
            messagebox.showerror('错误提示', '此账户不存在')
            root4.destroy()
        else:
            passw=find_post["password"]
            nam=find_post["name"]
            if  x==nam and y== passw:
                root4.destroy()
                roo5=Toplevel()
                roo5.title("新的密码和名字")
                label=tkinter.Label(roo5,text="请输入新的密码和用户名")
                label.grid(row=0,column=0)
                ent = tkinter.Entry(roo5, font=(None, 15))
                ent.grid(row=3,column=0)

                ent2 = tkinter.Entry(roo5, font=(None, 15))
                ent2.grid(row=6,column=0)

                nbt= tkinter.Button(roo5, text='提交' ,font=(None, 15), command=lambda:genggaibox2(ent.get(),ent2.get()))

                nbt.grid(row=8,column=0)
                roo5.mainloop()
            else:
                root4.destroy()
                messagebox.showerror('错误提示', '用户名或密码错误')
        return ans2 
    

    root4=Toplevel()
    root4.title("更改")
    label=tkinter.Label(root4,text="请输入要更改的密码和用户名")
    label.grid(row=0,column=0)
    ent = tkinter.Entry(root4, font=(None, 15))
    ent.grid(row=3,column=0)

    ent2 = tkinter.Entry(root4, font=(None, 15))
    ent2.grid(row=6,column=0)

    nbt= tkinter.Button(root4, text='提交' ,font=(None, 15), command=lambda:genggaibox(ent.get(),ent2.get()))

    nbt.grid(row=8,column=0)

    
    root4.mainloop()
    
root2= tkinter.Tk()
root2.title("数据库")
nbtn= tkinter.Button(root2, text='注册' ,font=(None, 15), command=lambda: zhuce())

nbtn.grid(row=0,column=0)

nbtn1= tkinter.Button(root2, text='登录',font=(None, 15), command=lambda: denglu())

nbtn1.grid(row=0,column=2)

nbtn2= tkinter.Button(root2, text='更改',font=(None, 15), command=lambda: genggai())

nbtn2.grid(row=0,column=4)

nbtn3= tkinter.Button(root2, text='注销',font=(None, 15), command=lambda: zhuxiao())

nbtn3.grid(row=0,column=6)


root2.mainloop()