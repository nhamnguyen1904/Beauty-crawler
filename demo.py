from selenium import webdriver


def get_product_images(url):
    # Khởi tạo trình điều khiển Selenium
    driver = webdriver.Chrome()  # hoặc webdriver.Firefox() nếu bạn sử dụng Firefox

    # Mở trang sản phẩm
    driver.get(url)

    # Tìm tất cả các thẻ hình ảnh trên trang
    image_elements = driver.find_elements_by_tag_name('img')

    # Lấy URL hình ảnh từ thuộc tính src của từng thẻ hình ảnh
    image_urls = [img.get_attribute('src') for img in image_elements]

    # Đóng trình điều khiển Selenium
    driver.quit()

    return image_urls


product_url = f"https://us.sulwhasoo.com/collections/new-korean-skin-care/products/timetreasure-invigorating-cream-set-2"
images = get_product_images(product_url)

for image_url in images:
    print(image_url)
