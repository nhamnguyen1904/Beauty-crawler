from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import csv

#Kết nối với trình duyệt
browser= webdriver.Chrome(service=Service(ChromeDriverManager().install()))


# Create a CSV file to write the product data to
csv_file = open('product.csv', 'w', newline='', encoding='utf-8')#tạo file product.csv để import sản phẩm
writer = csv.writer(csv_file,delimiter='@', quotechar='"', quoting=csv.QUOTE_MINIMAL) #viết vô file csv và ngăn cách các trường bởi @
writer.writerow(["Tiêu đề", "Giá", "Ảnh", "Màu"]) #viết vào file csv dòng đầu tiên tiêu đề giá ảnh


#Tìm 5 link sản phẩm

for i in range(1, 6):
    # construct URL
    url = f"https://moji.vn/van-phong-pham-pc158151.html?page={i}"

    # load page
    browser.get(url) 
    # Thời gian hiển thị web
    sleep(2)

    # Tìm thẻ chứa các sản phẩm
    products=browser.find_elements(by=By.CLASS_NAME,value='product-item') #lấy ra các sản phẩm
    #Lấy link sản phẩm
    link_products=[]
    for product in products: #lọc qua từng sản phẩm
        link=product.find_element(by=By.CSS_SELECTOR, value='.image a').get_attribute('href') #lấy link từng sản phẩm
        link_products.append(link) #nối link vừa lấy được vào mảng 

    #Loop qua từng link sản phẩm
    for link in link_products:
        browser.get(link)
        title=browser.find_element(by=By.CSS_SELECTOR, value='.blk-code .title').text #Lấy title
        price=browser.find_element(by=By.CSS_SELECTOR, value='.blk-price .price').text #Lấy giá
        price=price.replace(",","")
        color_list=browser.find_elements(by=By.CSS_SELECTOR, value='.blk-att a') #Lấy màu
        colors = []
        for color in color_list:
            name = color.get_attribute("title")
            if name:
                colors.append(name)
        colors=','.join(colors)
        images=browser.find_elements(by=By.CSS_SELECTOR, value='.thumbnailUri')#Lấy ảnh

        image_urls = []
        for image in images:
            url = image.get_attribute("data-src")
            if url:
                image_urls.append(url)
        image_urls=','.join(image_urls)
        # Write the product data to the CSV file
        writer.writerow([title, price, image_urls, colors])


# sleep(5)
# Close the CSV file and web driver
csv_file.close()
browser.quit()


