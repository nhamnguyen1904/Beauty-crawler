from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--incognito")
chrome_options.add_argument("--window-size=1920x1080")

driver = webdriver.Chrome(chrome_options=chrome_options, executable_path="/HaiMat/chromedriver")
driver.get("https://www.google.com/")
driver.maximize_window()
