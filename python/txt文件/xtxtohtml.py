import tkinter as tk
from tkinter import filedialog,messagebox

def gettxt():
    txtpass.delete(0, tk.END)
    file = filedialog.askopenfilename(defaultextension ='txt',title = "选择路径")
    
    txtpass.insert("0",file)
def gethtml():
    htmlpass.delete(0, tk.END)
    file = filedialog.askdirectory() 
    htmlpass.insert("0",file)
def to():
    if txtpass.get() is None or htmlpass.get() is None:
        messagebox.showerror('错误', '选项不能为空')
    else:
        import os

        # path定义要获取的文件名称的目录（C盘除外）
        file_name=os.path.basename(txtpass.get())
        x,y=file_name.split(".")
        file1=txtpass.get()
        file2=htmlpass.get()
        with open(file1,"r",encoding="UTF-8") as f:
            file=f.read()
            f.close
        file2=f"{file2}/{x}.html"
        print(file)
        with open(file2,"a",encoding="UTF-8") as f :
            f.write(file)
            f.close
        messagebox.showinfo(title = "成功", message="转换完毕")

root = tk.Tk()
root.title("txt转html")
lbl =tk.Label(root, text="  txt文件路径")
lbl.grid(column=0, row=0)
txtpass = tk.Entry(root ,width=35,bd=5,font=(None,10))
txtpass.grid(columnspan=70,padx=10)
txtbtn= tk.Button(root, text='选择',width=4, height=1,font=(None, 15), command=lambda: gettxt())

txtbtn.grid(row=2,column=0)
lb2 =tk.Label(root, text="  html文件路径")
lb2.grid(column=0, row=4)
htmlpass = tk.Entry(root ,width=35,bd=5,font=(None,10))
htmlpass.grid(columnspan=70,padx=10)
htmlbtn= tk.Button(root, text='选择',width=4, height=1,font=(None, 15), command=lambda: gethtml())

htmlbtn.grid(row=6,column=0)
btn= tk.Button(root, text='转换',width=4, height=1,font=(None, 15), command=lambda: to())

btn.grid(row=8,column=0)
root.mainloop()
# file = filedialog.askopenfilename()