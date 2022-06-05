

from click import password_option
import jieba
import os, sys
from flask import Flask,render_template,request,abort,render_template_string,flash
import webbrowser as web

import pymongo
from tkinter import W, messagebox
app = Flask(__name__)
client = pymongo.MongoClient(host= '127.0.0.1', port=27017)
db = client.testdb
coll = db.get_collection("userdb")
clien = pymongo.MongoClient(host= '127.0.0.1', port=27017)
d= clien.testdb
col= d.get_collection("bookdb")
x=""
wrd=[]
mat=0
wd=[]
namelist=[]
db=[]
password_=[]
namewo=[]
namelist2=[]
@app.route('/')
def index():
    
        
  
    return render_template('index.html')

@app.route("/login")
def login():
    global password_,namewo
    
    password_,namewo=[],[]
        
    word = request.values.get("word")
    ward=request.values.get("ward")
   
    for i in coll.find():
        namewo.append(i['name'])
        password_.append(i['password'])

    if ward not in namewo and word not in password_:
        print(word,ward) 
        if ward!=None  and word!=None and ward!="" and word!="" and word.lower()!="admin":
    
    
    
            longo={"name":word,"password":ward}
            result = coll.insert_one(longo)
            return '''
            <link rel="stylesheet" href="https://cdn.staticfile.org/twitter-bootstrap/4.1.0/css/bootstrap.min.css">
            <script src="https://cdn.staticfile.org/jquery/3.2.1/jquery.min.js"></script>
            <script src="https://cdn.staticfile.org/popper.js/1.12.5/umd/popper.min.js"></script>
            <script src="https://cdn.staticfile.org/twitter-bootstrap/4.1.0/js/bootstrap.min.js"></script>
            <div class="alert alert-success alert-dismissible">
                <button type="button" class="close" data-dismiss="alert">&times;</button>
                <strong>注册成功!</strong>
            </div>
            '''
        else:
            pass
                    
    else:
        abort(401)
    return render_template('login.html') 

@app.route("/register")
def regiser():
    global x
    werd = request.values.get("werd")
    wrrd=request.values.get("wrrd")
    if wrrd!=None  and werd!=None and werd!="" and wrrd!="":
        try:
            post = coll.find_one({'name' : werd})
            W=len(post['password'])
        except  TypeError:
            abort(401)
        else:
            if post["name"]==werd and post["password"]==wrrd:
                x=post['name']
                return  '''
            <link rel="stylesheet" href="https://cdn.staticfile.org/twitter-bootstrap/4.1.0/css/bootstrap.min.css">
            <script src="https://cdn.staticfile.org/jquery/3.2.1/jquery.min.js"></script>
            <script src="https://cdn.staticfile.org/popper.js/1.12.5/umd/popper.min.js"></script>
            <script src="https://cdn.staticfile.org/twitter-bootstrap/4.1.0/js/bootstrap.min.js"></script>
            <div class="alert alert-success alert-dismissible">
                <button type="button" class="close" data-dismiss="alert">&times;</button>
                <strong>登录成功!</strong>
            </div>
            '''
                
            else:
                return '<link rel="stylesheet" href="https://cdn.staticfile.org/twitter-bootstrap/4.1.0/css/bootstrap.min.css"><script src="https://cdn.staticfile.org/jquery/3.2.1/jquery.min.js"></script><script src="https://cdn.staticfile.org/popper.js/1.12.5/umd/popper.min.js"></script><script src="https://cdn.staticfile.org/twitter-bootstrap/4.1.0/js/bootstrap.min.js"></script><div class="alert alert-danger alert-dismissible"><button type="button" class="close" data-dismiss="alert">&times;</button><strong>登陆失败</strong> </div>'   
                
    return render_template('register.html')

@app.route("/logout")
def logout():
    werd = request.values.get("wzrd")
    wrrd=request.values.get("wkrd")
    if wrrd!=None  and werd!=None and werd!="" and wrrd!="":
        try:
            post = coll.find_one({'name' : werd})
            W=len(post['password'])
        except  TypeError:
            abort(401)
        else:
            if post["name"]==werd and post["password"]==wrrd:
                    
                result = coll.delete_many({'name' :werd})
                return '''
                    <div class="container">
                        <script src="https://cdn.staticfile.org/jquery/3.2.1/jquery.min.js"></script>
                        <script src="https://cdn.staticfile.org/popper.js/1.12.5/umd/popper.min.js"></script>
                            <script src="https://cdn.staticfile.org/twitter-bootstrap/4.1.0/js/bootstrap.min.js"></script>
                            <div class="alert alert-success alert-dismissible">
                                <button type="button" class="close" data-dismiss="alert">&times;</button>
                                <strong>注销成功!</strong> 
                            </div>
                    </div>'''
            else:
                return '<link rel="stylesheet" href="https://cdn.staticfile.org/twitter-bootstrap/4.1.0/css/bootstrap.min.css"><script src="https://cdn.staticfile.org/jquery/3.2.1/jquery.min.js"></script><script src="https://cdn.staticfile.org/popper.js/1.12.5/umd/popper.min.js"></script><script src="https://cdn.staticfile.org/twitter-bootstrap/4.1.0/js/bootstrap.min.js"></script><div class="alert alert-danger alert-dismissible"><button type="button" class="close" data-dismiss="alert">&times;</button><strong>注销失败</strong> </div>'   
            
    return render_template('log out.html') 

@app.route("/search") 
def search(): 
    global mat,wd,aaa,namelist,db,wordlist,namelist
    namelist,namelist2=[],[]
    wvrd = request.values.get("wvrd")
    db=[]
    if wvrd!=None  and wvrd!=None and wvrd!="" and wvrd!="":
        
        aaa=jieba.lcut(wvrd)
        print(aaa)
        for w in col.find():
            namelist2.append(w['name'])
            print(w)

            for x in aaa:
                if x in w['name']:
                    mat=mat+1
            print(mat)
            if mat*2==len(aaa) or mat*2>len(aaa):
                
                find_word = col.find_one({'name' : w['name']})
                wordlist={
                    "题目":find_word["name"],
                    "作者":find_word['man'],
                    "内容":find_word['word']

                    }
                db.append(wordlist)
               
            
            mat=0
        if len(db)==0:
            abort(404)
        else:
            print("________________________________________________")
            print(db)
            return render_template('book.html',word=db)
     
         
        
            
        
        
        
    else:
        pass

                

    wordlist={} 
    db=[]  
    return render_template('book.html',word=db) 

@app.route("/wriet")
def wriet():
    global x,namelist2
    namelist2=[]
    ord = request.values.get("ord")
    ard=request.values.get("ard")
    for w in col.find():
        namelist2.append(w['name'])
    print(ard,ord,x)
    if ord!=None  and ard!=None and ord!="" and ard!="" and x!="" and x!=None:
        if ord not in namelist2:
            wordlist2={
                "name":ord,
                "man":x,
                "word":ard

            }
            print(wordlist2)
            result = col.insert_one(wordlist2)
        else:
            abort(401)  
    
            
    return render_template('book2.html') 

    

@app.errorhandler(404)
def page_unauthorized(error):
    return render_template('404.html')
@app.errorhandler(401)
def page_unauthorized(error):
    return render_template('401.html')
@app.errorhandler(401)
def page_unauthorized(error):
    return render_template('400.html')
@app.route("/singout")
def singout():
    global x
    x=""
    return render_template('singout.html')

# 项目根路径
BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, BASE_PATH)  # 将项目根路径临时加入环境变量，程序退出后失效

if __name__ == '__main__':
    # host为主机ip地址，port指定访问端口号，debug=True设置调试模式打开
    app.run(host="0.0.0.0", port=5000, debug=True)