

win=[]
user1={}
user2={}
allblock={}
a=""
z0=[4, 0, 2, 6, 8, 1, 3, 5, 7]

def chushihua():
    global win,user1,user2,allblock
    win=[(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]
    user1={
        0:"0",1:"1",2:"2",
        3:"3",4:"4",5:"5",
        6:"6",7:"7",8:"8"
    }
    user2={
        0:"0",1:"1",2:"2",
        3:"3",4:"4",5:"5",
        6:"6",7:"7",8:"8"
    }
    allblock={
        0:" 0",1:" 1",2:" 2",
        3:" 3",4:" 4",5:" 5",
        6:" 6",7:" 7",8:" 8"
    }
def shengyu(x,x2):
    return 0 if x2[x] not in [" X", " O"] else 1
def legal_moves(board):
    
    """"返回可落子的位置列表"""
    return [i for i in board if i not in [" O", " X"]]

def panduan(x,y):
    return x in y
def computer(my,our,you):
    global win,z0,user2,allblock

    z=0
    y=0
    move=""
    our_copy=our.copy()
    my_copy =my.copy()
    you_copy=you.copy()
    while True:
        for move in legal_moves(our_copy):
                my_copy[y] = " O"
                if panduanwin(my_copy,win," O") and shengyu(y,allblock)==0:
                    z=1  # 判断是否获胜
                    return y

                y=y+1
                my_copy=my.copy()
                y=0




        if z == 1:
            break
        y=0
        for move in (legal_moves(our_copy)):
            you_copy[y] =" X"

            if panduanwin(you_copy,win," X") and shengyu(y,allblock)==0: 

                z=1 # 判断是否获胜
                return y
            y=y+1
            you_copy=you.copy()
            if z==1: 
                break
        y=0

        if z!=1:
            for move in z0 :

                if shengyu(move,our)==0:
                    z=1
                    user2[move]=" O"
                    allblock[move]=" O"

                    return move

        
        
    # 规则2： 某个位置玩家下一步落子可以获胜，则选择该位置
    
 


        # 规则3： 按照中心（4）、角（0， 2， 6， 8） 以及边（1， 3， 5， 7）
    


def panduanwin(x,y,z):
    nm=0
    k=1
    for i in y:
        for a in i:
            if x[a]==z:
                nm=nm+1
        if nm==3:
            k=0
            return nm == 3
        nm=0
        if k==0:
            break
            
def main():  # sourcery skip: low-code-quality
    global user1,user2,win,allblock,a,z0
    kbc=0
    tu=''
    tu=input("你是否愿意先出，y/n")
    while tu  not in {'y', 'n'}:
        tu=input("你是否愿意先出，y/n")
    while True:

        q=0
        nmb=0



        if tu=='y':
            for i in  allblock.values():
                print(i,end=" ")
                nmb+=1
                if nmb==3:
                    nmb=0
                    print("\n")
            a=input("一号玩家输入")
            a=int(a)
            if shengyu(a,allblock) ==0:
                user1[a]=" X"
                allblock[a]=" X"
                tu="n"



            else:
                while q==0:
                    for i in  allblock.values():
                        print(i,end=" ")
                        nmb+=1
                        if nmb==3:
                            nmb=0
                            print("\n")
                    a=int(input("一号玩家您输入的地方以被占据请重新输入"))
                    if shengyu(a,allblock) ==0:
                        q=1
                        user1[a]=" X"
                        tu='n'
                        allblock[a]=" X"


                        break


            q=0
            q=0
            kbc=0
            nmb=0
            for i in  allblock.values():
                print(i,end=" ")
                nmb+=1
                if nmb==3:
                    nmb=0
                    print("\n")
            if panduanwin(user1,win," X")==True:
                print("玩家一胜利")
                break
            if panduanwin(user2,win," O")==True:
                print("ai胜利")
                break
            for i in allblock.values():

                if i in [" X", " O"]:
                    kbc=kbc+1
            if kbc==9:
                print("平局")
                break 
            else:
                kbc=0
        if tu=='n':
            
            xz=computer(user2,allblock,user1)

            user2[xz]=" O"
            allblock[xz]=" O"
            tu='y'
            print("ai输入",xz)




            q=0
            kbc=0
            if panduanwin(user1,win," X")==True:
                print("玩家一胜利")
                break
            if panduanwin(user2,win," O")==True:
                print("ai胜利")
                break
            for i in allblock.values():
                if i in [" O", "  X"]:
                    kbc=kbc+1
            if kbc==9:
                print("平局")
                break
            else:
                kbc=0 

def new_func():
    kbc=0   

            

chushihua()
main()
