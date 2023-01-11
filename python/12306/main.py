import bs4
import requests
def get_tarin(fromStation,toStation,time):
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}  
#https://train.qunar.com/stationToStation.htm?fromStation=%E4%B8%8A%E6%B5%B7&toStation=%E5%8C%97%E4%BA%AC&date=2023-01-05&ex_track=auto_1SZE1U0s0t
    url=f"https://www.suanya.cn/pages/trainList?fromCn={fromStation}&toCn={toStation}&fromDate={time}"
    
    response = requests.get(url,headers=headers)
    response.encoding = "UTF-8"
    soup = bs4.BeautifulSoup(response.text,"lxml")
    data1 = soup.find_all(name="strong",data_v_71f8c87e="")
    data1=list(data1)
    
    data2=[]
    data3=[]
    for i in data1:
        data1.pop(data1.index(i))
        i=str(i)
        data2.append(i)
    for i in data2:
        if '余' not in i and ":" not in i and fromStation not in i and toStation not in i:
            data3.append(i)
    for i in data3:
        x=i[27:]
        print(x[0:-9])
get_tarin("北京","拉萨","2023-01-20")