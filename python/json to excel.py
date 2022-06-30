from re import L
import pandas as pd
import pymongo
import xlwt
ke=[]
va=[]
j=0
l=0
i=1
book = xlwt.Workbook(encoding='utf-8',style_compression=0)
sheet = book.add_sheet('json',cell_overwrite_ok=True)
client = pymongo.MongoClient(host= '127.0.0.1', port=27017)
db = client.testdb
coll = db.get_collection("namedb")
find_post = coll.find_one({'_id' : '10'})
for key,value in find_post.items():
    ke.clear()
    ke.extend((key, value))
    print(ke)
    i=1
    l=l+1
    for i in range(len(ke)):

        print(ke[i])

        sheet.write(l,i,ke[i])

savepath = 'D:\\excel表格3.xls'
book.save(savepath)