import requests
from bs4 import BeautifulSoup
import pandas as pd

def convertPrice(price: str):
    result = 0
    if 'tỉ' in price:
        temp1 = price.split(' tỉ ')
        result = result + int(temp1[0]) * 10**9

        temp2 = temp1[1].split(' ')
        result = result + int(temp2[0]) * 10**6
    else:
        temp3 = price.split(' ')
        result = result + int(temp3[0]) * 10**6

    return result

name = []
price = []
year = []
style = []
stat = []

dict = {'Tên xe': name, 'Giá': price, 'Năm sản xuất': year, 'Kiểu dáng': style,'Tình trạng': stat}  

listCarLinks = []
baseUrl = 'https://www.shiseido.com.vn/'

current = 0

def processingData(link: str):
    try:
        link = baseUrl + link
        response = requests.get(link)
        soup = BeautifulSoup(response.content, "html.parser")

        carTitle = soup.select_one('.group-title-detail > .title-detail').get_text().split(' - ')
        TenXe = carTitle[0]
        Gia = convertPrice(carTitle[1])
        if TenXe == '':
            print(link)

        carInfos = soup.select('.box-info-detail > .list-info > li')
        carInforTitles = ['Năm sản xuất', 'Kiểu dáng', 'Tình trạng', 'Xuất xứ', 'Số km đã đi', 'Tỉnh thành', 'Hộp số', 'Nhiên liệu']

        name.append(TenXe)
        price.append(Gia)
        year.append('')
        style.append('')
        stat.append('')

        for carInfo in carInfos:
            for carInforTitle in carInforTitles:
                if carInforTitle in carInfo.get_text():
                    dict.get(carInforTitle)[-1] = carInfo.get_text().replace(carInforTitle, '').replace(' ', '')
        
        current = current + 1
        print(current)
    except:
        pass

for i in range(0, 2):
    try:
        response = requests.get('https://www.shiseido.com.vn/vi/axe_suncare/' + str(i))
        soup = BeautifulSoup(response.content, "html.parser")

        links = soup.select('.item-car > .photo > a')
        for link in links:
            if link['href']:
                listCarLinks.append(link['href'])
        
        print('done: ' + str(i), response.status_code)
    except:
        pass

for link in listCarLinks:
    print(link)
    processingData(link)

df = pd.DataFrame(dict)
df.to_csv('data.csv', encoding='utf-8-sig')
