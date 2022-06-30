
from tkinter import EXCEPTION
import pymongo
client = pymongo.MongoClient(host= '127.0.0.1', port=27017)
db = client.testdb
coll = db.get_collection("namedb")
print("请执行以下操作 更改 登录 注销 或 注册")
ans=input("/// ")
if ans=="注册":
    print("请输入用户名1---10")
    ans2=input("/// ")
    print("请输入密码1---10")
    ans3=input("/// ")
    find_post = coll.find_one({'name' : ans2})
    
    try:
        upk=len(find_post["name"] )
    except TypeError:
        
        if len(ans2)>1 and len(ans2)<10 and len(ans3)>1 and len(ans3)<10:
            longo={"name":ans2,"password":ans3}
            result = coll.insert_one(longo)
                
        else:
            print("cuopwu")
    else:
        print("被占用")

elif ans=="登录":
    print("请输入密码")
    ans2=input("/// ")
    find_post = coll.find_one({'password' : ans2})
    try:
        passw=find_post["password"]
    except TypeError:
        print("您所要登陆的账户不存在")
    else:
        passw=find_post["password"]
        if passw==ans2:
            print("欢迎"+find_post["name"])
        else:
            print("错误")
elif ans=="注销":
    print("请输入用户名")
    ans2=input("/// ")
    print("请输入密码")
    ans3=input("/// ")
    find_post = coll.find_one({'name' : ans2})
    try:
        passw=find_post["password"]
    except TypeError:
        print("您所要注销的账户不存在")
    else:
        passw=find_post["password"]
        if passw==ans3:
            print("您确定要这么做么、此操作不可逆(y,n)")
            ans4=input("/// ")
            if ans4=="y":
                result = coll.delete_many({'name' : ans2})
            elif ans4=="n":
                print("成功")
            else:
                print("错误")
        else:
            print("错误")
elif ans =="更改":
    print("请输入用户名")
    ans2=input("/// ")
    print("请输入密码")
    ans3=input("/// ")
    find_post = coll.find_one({'name' : ans2})
    try:
        passw=find_post["password"]
        nam=find_post["name"]
    except TypeError:
        print("您所要更改的账户不存在")
    else:
        if  ans2==nam and ans3== passw:
            print("请输入您的新名称1--10")
            ansn2=input("/// ")
            print("请输入您的新密码1--10")
            ansn3=input("/// ")
            if len(ans2)>1 and len(ans2)<10 and len(ans3)>1 and len(ans3)<10:
                print("您确定哟这么做么、此操作不可逆(y,n)")
                an=input("// ")
                if an =="y":
                    condition = {'name' : ans2}
                    pty={'$set' : {'name' : ansn2,"password":ansn3}}
                    result = coll.update_one(condition, pty)
                elif an=="n":
                    print("成功")
                else:
                    print("错误")
            else:
                print("无效")
        else:
            print("错误")
else:
    print("错误")


    
    