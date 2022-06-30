


import os
import sys
from datetime import timedelta
from wsgiref.simple_server import make_server

import jieba
import pymongo
from flask import (Flask, abort, flash, render_template,
                   render_template_string, request, session)

app = Flask(__name__)

app.config['SECRET_KEY'] = os.urandom(24)
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(days=7)

client = pymongo.MongoClient(host= '127.0.0.1', port=27017)
db = client.testdb
coll = db.get_collection("userdb")
clien = pymongo.MongoClient(host= '127.0.0.1', port=27017)
d= clien.testdb
col= d.get_collection("bookdb")
def takcoll(x):
    wordlist2 = [{"题目": i["name"], "内容": i["word"]} for i in col.find() if x == i["man"]]

    return wordlist2 or [{"题目":"无","内容":"无"}]
def weijin():
    weijin=[]
    with open("D:\\违禁.txt","r",encoding='UTF-8') as f:
        for i in f:
            i=i.replace('\n' , '')
            weijin.append(i)
    return weijin
x=""
wrd=[]
def alluser():
    return [i["name"] for i in coll.find()]
def allpassword():
    return [i["password"] for i in coll.find()]
mat=0
wd=[]
namelist=[]
db=[]
wordlist3=[]
password_=[]
namewo=[]
namelist2=[]
@app.route('/')
def index():
    
        
  
    return render_template('index.html')

@app.route("/register",methods = ['POST','GET'])
def register():
    global wordlist3
    if request.method == 'POST':
        word = request.values.get("word")
        ward=request.values.get("ward")
        print(alluser)
        print(allpassword)
        if ward not in allpassword() and word not in  alluser():
            print(word,ward)
            if ward!=None  and word!=None and ward!="" and word!="" and word.lower()!="admin":



                print(wordlist3)
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
            return '<link rel="stylesheet" href="https://cdn.staticfile.org/twitter-bootstrap/4.1.0/css/bootstrap.min.css"><script src="https://cdn.staticfile.org/jquery/3.2.1/jquery.min.js"></script><script src="https://cdn.staticfile.org/popper.js/1.12.5/umd/popper.min.js"></script><script src="https://cdn.staticfile.org/twitter-bootstrap/4.1.0/js/bootstrap.min.js"></script><div class="alert alert-danger alert-dismissible"><button type="button" class="close" data-dismiss="alert">&times;</button><strong>密码和用户名不能为空</strong> </div>'
        else:
            abort(401)
    return render_template('register.html') 

@app.route("/longin", methods = ['POST','GET'])
def login():
    global werd,wrrd,wordlist3
    if request.method == 'POST':
        werd = request.values.get("werd")
        wrrd=request.values.get("wrrd")
        if wrrd is None or werd is None or werd == "" or wrrd == "":
            return '<link rel="stylesheet" href="https://cdn.staticfile.org/twitter-bootstrap/4.1.0/css/bootstrap.min.css"><script src="https://cdn.staticfile.org/jquery/3.2.1/jquery.min.js"></script><script src="https://cdn.staticfile.org/popper.js/1.12.5/umd/popper.min.js"></script><script src="https://cdn.staticfile.org/twitter-bootstrap/4.1.0/js/bootstrap.min.js"></script><div class="alert alert-danger alert-dismissible"><button type="button" class="close" data-dismiss="alert">&times;</button><strong>密码和用户名不能为空</strong> </div>'
        if werd not in alluser() or wrrd not in allpassword():
            abort(401)
        else:
            usertInfo= coll.find_one({'password' : wrrd})
            if usertInfo["name"]==werd and usertInfo["password"]==wrrd:
                session['userName']=usertInfo['name']
                session['isLogin']=True
                wordlist3=takcoll(usertInfo['name'])
                return render_template('userindex.html', namee=werd, passworde=wrrd, wordlist=wordlist3) if session.get('userName') != "" and werd != "" and wrrd != "" else render_template('userindex.html', namee="未登录", passworde="未登录")



            else:
                return '<link rel="stylesheet" href="https://cdn.staticfile.org/twitter-bootstrap/4.1.0/css/bootstrap.min.css"><script src="https://cdn.staticfile.org/jquery/3.2.1/jquery.min.js"></script><script src="https://cdn.staticfile.org/popper.js/1.12.5/umd/popper.min.js"></script><script src="https://cdn.staticfile.org/twitter-bootstrap/4.1.0/js/bootstrap.min.js"></script><div class="alert alert-danger alert-dismissible"><button type="button" class="close" data-dismiss="alert">&times;</button><strong>登陆失败</strong> </div>'
    return render_template('longin.html')

@app.route("/logout",methods = ['POST','GET'])
def logout():
    if not (isLogin := session.get('isLogin')):
        return '<link rel="stylesheet" href="https://cdn.staticfile.org/twitter-bootstrap/4.1.0/css/bootstrap.min.css"><script src="https://cdn.staticfile.org/jquery/3.2.1/jquery.min.js"></script><script src="https://cdn.staticfile.org/popper.js/1.12.5/umd/popper.min.js"></script><script src="https://cdn.staticfile.org/twitter-bootstrap/4.1.0/js/bootstrap.min.js"></script><div class="alert alert-danger alert-dismissible"><button type="button" class="close" data-dismiss="alert">&times;</button><strong>请先登录</strong> </div>' 

    if request.method == 'POST':
        wefrd = request.values.get("wzrd")
        wrfrd=request.values.get("wkrd")
        print(werd,wrrd)
        if wefrd is None or wrfrd is None :
            return '<link rel="stylesheet" href="https://cdn.staticfile.org/twitter-bootstrap/4.1.0/css/bootstrap.min.css"><script src="https://cdn.staticfile.org/jquery/3.2.1/jquery.min.js"></script><script src="https://cdn.staticfile.org/popper.js/1.12.5/umd/popper.min.js"></script><script src="https://cdn.staticfile.org/twitter-bootstrap/4.1.0/js/bootstrap.min.js"></script><div class="alert alert-danger alert-dismissible"><button type="button" class="close" data-dismiss="alert">&times;</button><strong>用户名和密码不能为空</strong> </div>'   

        if wefrd not in alluser() or wrfrd not in allpassword():
            abort(401)
        post1= coll.find_one({'password' : wrfrd})
        if post1["name"] != wefrd or post1["password"] != wrfrd:
            return '<link rel="stylesheet" href="https://cdn.staticfile.org/twitter-bootstrap/4.1.0/css/bootstrap.min.css"><script src="https://cdn.staticfile.org/jquery/3.2.1/jquery.min.js"></script><script src="https://cdn.staticfile.org/popper.js/1.12.5/umd/popper.min.js"></script><script src="https://cdn.staticfile.org/twitter-bootstrap/4.1.0/js/bootstrap.min.js"></script><div class="alert alert-danger alert-dismissible"><button type="button" class="close" data-dismiss="alert">&times;</button><strong>注销失败</strong> </div>'
        result = coll.delete_many({'name' :wefrd})
        print(result)
        return '''
                <link rel="stylesheet" href="https://cdn.staticfile.org/twitter-bootstrap/4.1.0/css/bootstrap.min.css">
                <script src="https://cdn.staticfile.org/jquery/3.2.1/jquery.min.js"></script>
                <script src="https://cdn.staticfile.org/popper.js/1.12.5/umd/popper.min.js"></script>
                <script src="https://cdn.staticfile.org/twitter-bootstrap/4.1.0/js/bootstrap.min.js"></script>
                <div class="alert alert-success alert-dismissible">
                    <button type="button" class="close" data-dismiss="alert">&times;</button>
                    <strong>注销成功!</strong>
                </div>
              '''
    return render_template('logout.html') 

@app.route("/search",methods = ['POST','GET'])
def search(): 
    global mat,wd,aaa,namelist,db,wordlist,namelist
    if not (isLogin := session.get('isLogin')):
        return '<link rel="stylesheet" href="https://cdn.staticfile.org/twitter-bootstrap/4.1.0/css/bootstrap.min.css"><script src="https://cdn.staticfile.org/jquery/3.2.1/jquery.min.js"></script><script src="https://cdn.staticfile.org/popper.js/1.12.5/umd/popper.min.js"></script><script src="https://cdn.staticfile.org/twitter-bootstrap/4.1.0/js/bootstrap.min.js"></script><div class="alert alert-danger alert-dismissible"><button type="button" class="close" data-dismiss="alert">&times;</button><strong>请先登录</strong> </div>'
    if request.method == 'POST':
        
        wvrd = request.values.get("wvrd")
        db=[]
        if wvrd not in [None, ""]:

            aaa=jieba.lcut(wvrd)
            print(aaa)
            namelist,namelist2=[],[]
            for w in col.find():
                print(w)
                namelist2.append(w['name'])
                print(w)

                for x in aaa:
                    if x in w['name']:
                        mat=mat+1
                print(mat)
                if mat*2==len(aaa) or mat*2>len(aaa):

                    if find_word := col.find_one({'name': w['name'], 'staus': '2'}):
                        wordlist={
                            "题目":find_word["name"],
                            "作者":find_word['man'],
                            "内容":find_word['word']

                            }
                        db.append(wordlist)


                mat=0
            if not db:
                abort(404)
            else:
                print("________________________________________________")
                print(db)
                return render_template('book.html',word=db)
    return render_template('book.html',word=db) 
u=0
@app.route("/wriet",methods = ['POST','GET'])
def wriet():
    global u
    u=0
    if not (isLogin := session.get('isLogin')):
        return '<link rel="stylesheet" href="https://cdn.staticfile.org/twitter-bootstrap/4.1.0/css/bootstrap.min.css"><script src="https://cdn.staticfile.org/jquery/3.2.1/jquery.min.js"></script><script src="https://cdn.staticfile.org/popper.js/1.12.5/umd/popper.min.js"></script><script src="https://cdn.staticfile.org/twitter-bootstrap/4.1.0/js/bootstrap.min.js"></script><div class="alert alert-danger alert-dismissible"><button type="button" class="close" data-dismiss="alert">&times;</button><strong>请先登录</strong> </div>'
  # sourcery skip: avoid-builtin-shadow
    global namelist2
    if request.method == 'POST':
        ord = request.values.get("ord")
        ard=request.values.get("ard")
        namelist2 = [w['name'] for w in col.find()]
        print(ard,ord)
        if ord!=None  and ard!=None and ord!="" and ard!="":
            if ord   in namelist2:
                pass

            else:
                for i in weijin():
                    if i in ord or i in ard:
                        u=1
                        break
                        
                if u!=1:
                    if len(ord)<20 and len(ard)<400:
                        print(request.remote_addr)
                        wordlist2={
                            "name":ord,
                            "man":session['userName'],
                            "word":ard,
                            "status":'1',
                            "userIp":request.headers['X-ReaL—Ip'] 
                        }
                        print(wordlist2)
                        result = col.insert_one(wordlist2)
                    else:
                        return '<link rel="stylesheet" href="https://cdn.staticfile.org/twitter-bootstrap/4.1.0/css/bootstrap.min.css"><script src="https://cdn.staticfile.org/jquery/3.2.1/jquery.min.js"></script><script src="https://cdn.staticfile.org/popper.js/1.12.5/umd/popper.min.js"></script><script src="https://cdn.staticfile.org/twitter-bootstrap/4.1.0/js/bootstrap.min.js"></script><div class="alert alert-danger alert-dismissible"><button type="button" class="close" data-dismiss="alert">&times;</button><strong>您的题目或内容超长</strong> </div>' 
                else: return '<link rel="stylesheet" href="https://cdn.staticfile.org/twitter-bootstrap/4.1.0/css/bootstrap.min.css"><script src="https://cdn.staticfile.org/jquery/3.2.1/jquery.min.js"></script><script src="https://cdn.staticfile.org/popper.js/1.12.5/umd/popper.min.js"></script><script src="https://cdn.staticfile.org/twitter-bootstrap/4.1.0/js/bootstrap.min.js"></script><div class="alert alert-danger alert-dismissible"><button type="button" class="close" data-dismiss="alert">&times;</button><strong>涉嫌违禁词语</strong> </div>' 
        
        
        else:
             return '<link rel="stylesheet" href="https://cdn.staticfile.org/twitter-bootstrap/4.1.0/css/bootstrap.min.css"><script src="https://cdn.staticfile.org/jquery/3.2.1/jquery.min.js"></script><script src="https://cdn.staticfile.org/popper.js/1.12.5/umd/popper.min.js"></script><script src="https://cdn.staticfile.org/twitter-bootstrap/4.1.0/js/bootstrap.min.js"></script><div class="alert alert-danger alert-dismissible"><button type="button" class="close" data-dismiss="alert">&times;</button><strong>题目或内容不能能为空</strong> </div>' 
        
    return render_template('book2.html') 
@app.route("/userindex")
def uesrindex():
    if not (isLogin := session.get('isLogin')):
        return '<link rel="stylesheet" href="https://cdn.staticfile.org/twitter-bootstrap/4.1.0/css/bootstrap.min.css"><script src="https://cdn.staticfile.org/jquery/3.2.1/jquery.min.js"></script><script src="https://cdn.staticfile.org/popper.js/1.12.5/umd/popper.min.js"></script><script src="https://cdn.staticfile.org/twitter-bootstrap/4.1.0/js/bootstrap.min.js"></script><div class="alert alert-danger alert-dismissible"><button type="button" class="close" data-dismiss="alert">&times;</button><strong>请先登录</strong> </div>' 

    return render_template('userindex.html', namee=werd, passworde=wrrd, wordlist=wordlist3) if session.get('userName') != "" and werd != "" and wrrd != "" else render_template('userindex.html', namee="未登录", passworde="未登录")


@app.errorhandler(404)
def page_unauthorized(error):
    return render_template('404.html')
@app.errorhandler(401)
def page_unauthorized(error):
    return render_template('401.html')
@app.errorhandler(400)
def page_unauthorized(error):
    return render_template('400.html')
@app.route("/singout")
def singout():
    session.clear
    
   
    return render_template('singout.html')

# 项目根路径
BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, BASE_PATH)  # 将项目根路径临时加入环境变量，程序退出后失效

if __name__ == '__main__':
    # host为主机ip地址，port指定访问端口号，debug=True设置调试模式打开
    #app.run(host="0.0.0.0", port=5000, debug=True)
    sever=make_server('0.0.0.0',5000,app)
    sever.serve_forever()
  
    app.run(debug=True,ssl_text=()) 
    