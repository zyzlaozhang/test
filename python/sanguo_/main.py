import jieba
import pandas as pd
def l(name):
    with open(name,"r", encoding='UTF-8') as file:
        word_=file.read()
        file.close
    word_list=jieba.lcut(word_)
    word_list_number={}
    for i in word_list:
        if i in word_list_number:
            word_list_number[i]+=1
        else:
            word_list_number[i]=1
    del word_list_number["------------"]
    del word_list_number["\n"]
    del word_list_number[" "]
    del word_list_number["，"]
    del word_list_number["。"]
    del word_list_number["："]
    del word_list_number["”"]
    del word_list_number["“"]
    del word_list_number["、"]
    del word_list_number["；"]
    del word_list_number["？"]
    del word_list_number["！"]

    word_list_number={"word":word_list_number.keys(),"number":word_list_number.values()}

    # myvar = word_list_number.DataFrame(data="number",ascending=False)
    # print(myvar)
    df=pd.DataFrame(data=word_list_number)
    myvar= df.sort_values("number",ascending=False) 
    print(myvar)
    myvar.to_excel("1.xlsx")
l("171182.txt")