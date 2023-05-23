from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
import random
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException
from selenium.webdriver.common.by import By
import pandas as pd
# 1. Khai báo browser
driver = webdriver.Chrome(ChromeDriverManager().install())

# 2. Mở URL của post
driver.get("https://www.foody.vn/ho-chi-minh/nha-hang-san-fu-lou/binh-luan")
sleep(random.randint(5,10))

review_count = driver.find_element("xpath","/html/body/div[2]/div[2]/div[2]/section/div/div/div/div/div[1]/div/div/div[1]/div/div[1]/div/ul/li[1]/a/span")
review_count = int(review_count.text)
click_count = int(review_count/10)
# 3. Lấy link hiện comment
print("show comment link")
for i in range(click_count):
    try:
        showcomment_link = driver.find_element("xpath", "/html/body/div[2]/div[2]/div[2]/section/div/div/div/div/div[1]/div/div/div[1]/div/div[2]/a")
        showcomment_link.click()
        print("i = " + str(i))
        sleep(random.randint(5,10))
    except NoSuchElementException:
        print("No Such Element Exception!" + str(i))
        
#acc_link = driver.find_element(By.XPATH, "//div[@class='ru-row']")
print("get link account member")
# get link account member
elems = driver.find_elements(By.CSS_SELECTOR , ".ru-row [href]")
account_name = [elem.text for elem in elems]
links = [elem.get_attribute('href') for elem in elems]

df1 = pd.DataFrame(list(zip(account_name, links)), columns = ['Tên tài khoản bình luận về nhà hàng này', 'Link đến tài khoản'])

df2_following = pd.DataFrame(list(zip([], [])), columns = ['Tên tài khoản bình luận về nhà hàng này', 'Link đến tài khoản'])
df2_follower = pd.DataFrame(list(zip([], [])), columns = ['Tên tài khoản bình luận về nhà hàng này', 'Link đến tài khoản'])
print("get activities number")
# get activities number
def get_activities(df):
    ##path of 'xx Hoạt động'
    activity = driver.find_element("xpath","/html/body/div[2]/div[6]/div/div[2]/div/div/div[1]/div/div/ul/li/span")
    activity_count = activity.text
    df['activity_count'][i] = activity_count
    print(str(i) + ": " + df['Tên tài khoản bình luận về nhà hàng này'][i])
    
    ## click button "Xem thêm" của hoạt động
    i1=i2=0
    ## activity_count = '10'
    ## vì lớn hơn 10 hoạt động mới có nút "Xem thêm". Nên bắt điều kiện. Từ 10 trở lại thì ko bắt điều kiện này
    if int(activity_count) > 10:
        i1 = (int(activity_count)-10)//10
        i2 = (int(activity_count)-10)%10
        #Nếu có dư tức là chắc chắn có 1 nút "Xem thêm" nữa. Nên cộng 1 để click thêm 1 nút
        if i2>0:
            i1 = i1+1
        # Quét button "Xem thêm" của hoạt động               
        for j in range(i1):
            try:
                ##path of 'Xem thêm' của hoạt động
                view_more_activities = driver.find_element("xpath", "/html/body/div[2]/div[6]/div/div[2]/div/div/div[2]/div/a")
                view_more_activities.click()
                print("j = " + str(j))
                sleep(random.randint(1,3))
            except ElementNotInteractableException:
                print("Element Not Interactable Exception!" + str(j))
    ## get account/restaurant/datetime/via/rating/cmt/view in activities
    account = []
    restaurant = []
    datetime = []
    via = []
    rating = []
    cmt = []
    view = []
    for k in range(int(activity_count)+1):
        try:
            #driver.get("https://www.foody.vn/thanh-vien/foodee_w8mf0hzu#/activities")
            #sleep(random.randint(5,10))
            print("restaurant_to_come: " + str(k))
            account_to_come = driver.find_element("xpath", "/html/body/div[2]/div[6]/div/div[2]/div/div/div[2]/ul/li[{}]/div[1]/div[2]/div[1]/a".format(k))
            account.append(account_to_come.text)
            print("restaurant_to_come: " + str(k))
            restaurant_to_come = driver.find_element("xpath", "/html/body/div[2]/div[6]/div/div[2]/div/div/div[2]/ul/li[{}]/div[1]/div[2]/div[2]/a".format(k))
            restaurant.append(restaurant_to_come.text)
            print("datetime_to_come: " + str(k))
            datetime_to_come = driver.find_element("xpath", "/html/body/div[2]/div[6]/div/div[2]/div/div/div[2]/ul/li[{}]/div[1]/div[2]/div[3]/span[1]".format(k))
            datetime.append(datetime_to_come.text)
            print("via_to_come: " + str(k))
            via_to_come = driver.find_element("xpath", "/html/body/div[2]/div[6]/div/div[2]/div/div/div[2]/ul/li[{}]/div[1]/div[2]/div[3]/a".format(k))
            via.append(via_to_come.text)
            print("rating_to_come: " + str(k))
            rating_to_come = driver.find_element("xpath", "/html/body/div[2]/div[6]/div/div[2]/div/div/div[2]/ul/li[{}]/div[1]/div[3]/span".format(k))
            rating.append(rating_to_come.text)                   
            print("cmt_to_come: " + str(k))                    
            cmt_to_come = driver.find_element("xpath", "/html/body/div[2]/div[6]/div/div[2]/div/div/div[2]/ul/li[{}]/div[2]/div/span".format(k))
            cmt.append(cmt_to_come.text)
            print("view_to_come: " + str(k))                  
            view_to_come = driver.find_element("xpath", "/html/body/div[2]/div[6]/div/div[2]/div/div/div[2]/ul/li[{}]/div[1]/div[2]/div[3]/span[2]".format(k))
            view.append(view_to_come.text)
            
            sleep(random.randint(1,3))
        except NoSuchElementException:
            print("No Such Element Exception!" + str(k))
            
    df3 = pd.DataFrame(list(zip(account, restaurant,datetime,via,rating,cmt,view)), 
                       columns = ['Tên tài khoản bình luận về nhà hàng này', 'Các địa điểm đã đến','Ngày Giờ review','Công cụ review','Chấm điểm','Nội dung bình luận','Số lượt xem nội dung bình luận'])

    return df3

# get following/follower number
def get_following_follower(fullXpath, df1_follow, df2):
    # access to following/follower
    friends_link = driver.find_element("xpath", fullXpath)
    friends_link.click()
    sleep(random.randint(1,3))
    ## click button "Xem thêm"
    while True:
        try:
            view_more = driver.find_element("xpath", "/html/body/div[2]/div[6]/div/div[2]/div/div/div[2]/a")
            view_more.click()
            print("Clicked!")
            sleep(random.randint(1,3))
        except ElementNotInteractableException:
            print("Element Not Interactable Exception!")
            break
    
    print("count friends in li")
    ## count friends in `li`
    html_list = driver.find_element(By.XPATH, "/html/body/div[2]/div[6]/div/div[2]/div/div/div[2]/ul")
    items = html_list.find_elements(By.CSS_SELECTOR , ".ng-scope")
    df1_follow['following - follower'][i] = len(items)
    
    #https://www.foody.vn/thanh-vien/katherinetruong#/friends/following - 
    ## click vào từng friend trong mục "Quan tâm"
    for l in range(int(len(items))+1):
        try:
            print("friend: " + str(l))
            following = driver.find_element("xpath", "/html/body/div[2]/div[6]/div/div[2]/div/div/div[2]/ul/li[{}]/div[1]/span".format(l))
            following.click()                 
    
            sleep(random.randint(1,3))
            
            #########Funtion get_activities for friend in "Quan tâm"
            df4 = get_activities(df2)
        
        except NoSuchElementException:
            print("No Such Element Exception!" + str(l)) 
    return df4, df1_follow
# ----------------------------
df1['activity_count'] = ""
df1['following - follower'] = ""
df1_follower = df1.copy()
df2_following['activity_count'] = ""
df2_follower['activity_count'] = ""
for i in range(len(links)):
    try:
        print("get activities number of member: " + links[i])
        # get activities number
        driver.get(links[i])
        sleep(random.randint(5,10))

        #########Funtion get_activities
        df3 = get_activities(df1)
        
        print("get following number")       
        #########Funtion get following/follower number
        
        #https://www.foody.vn/thanh-vien/katherinetruong#/friends/following - 
        ## click vào mục "Quan tâm"
        fullXpath_following = "/html/body/div[2]/div[6]/div/div[1]/div/div[2]/ul/li[1]/ul/li[3]/a"
        df4, df1_following = get_following_follower(fullXpath_following, df1, df2_following) 

        #https://www.foody.vn/thanh-vien/katherinetruong#/friends/follower - 
        ## click vào mục "Được Quan tâm"  
        fullXpath_follower = "/html/body/div[2]/div[6]/div/div[2]/div/div/div[1]/div/ul/li[2]/a"
        df5, df1_follower = get_following_follower(fullXpath_follower, df1_follower, df2_follower) 
        
        sleep(random.randint(1,3)) # dừng 1->3 để load tiếp trang khác
    except NoSuchElementException:
        df1['activity_count'][i] = "private account"
        df1_follower['activity_count'][i] = "private account"
        print("Private Account!")

# 6. Đóng browser
driver.close()