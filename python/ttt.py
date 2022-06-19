

win=[]
user1={}
user2={}
allblock={}

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
    return 0 if x2[x] not in list("012345678") else 1

def panduan(x,y):
    return x in y

def panduanwin(x,y,z):
    nm=0
    for i in y:
        for a in i:
            if x[a]==z:
                nm=nm+1
        if nm==3:
            
            return nm == 3
        nm=0
            
def main():  # sourcery skip: low-code-quality
    global user1,user2,win,allblock
    kbc=0
    while True:
        q=0
        nmb=0
        for i in  allblock.values():
            print(i,end=" ")
            nmb+=1
            if nmb==3:
                nmb=0
                print("\n")
            
        
        
        a=int(input("一号玩家输入"))
        if shengyu(a,allblock) ==0:
            user1[a]=" X"
            allblock[a]=" X"
            
            
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

                    allblock[a]=" X"
                    
                    
                    break
        
        
        q=0
        q=0
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
            print("玩家二胜利")
            break
        for i in allblock.values():
            if i in list("012345678"):
                kbc=kbc+1
        if kbc==9:
            print("平局")
            break 
        else:
            kbc=0
        
        
        a=int(input("二号玩家输入"))
        if shengyu(a,allblock) ==0:
            user1[a]=" O"
            allblock[a]=" O"
            
            
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
                    user1[a]=" O"

                    allblock[a]=" O"
                    
                    
                    break
        
        
        
        q=0
        
        if panduanwin(user1,win," X")==True:
            print("玩家一胜利")
            break
        if panduanwin(user2,win," O")==True:
            print("玩家二胜利")
            break
        for i in allblock.values():
            if i in list("012345678"):
                kbc=kbc+1
        if kbc==9:
            print("平局")
            break
        else:
            kbc=0    

        
        
chushihua()
main()
