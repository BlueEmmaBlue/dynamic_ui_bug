from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import os


chromedriver = r"C:\Program Files\Google\Chrome\Application\chromedriver.exe"
os.environ["webdriver.chrome.driver"] = chromedriver
mobile_emulation = {
    "deviceMetrics": {"width": 390, "height": 844, "pixelRatio": 3.0},  # 定义设备高宽，像素比
    "userAgent": "Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) "
                 "AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1"}  # 通过UA来模拟
chrome_options = Options()
chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
chrome_options.add_argument('headless')
driver = webdriver.Chrome(chromedriver,chrome_options=chrome_options)
driver.get("http://www.baidu.com")
time.sleep(1)

# 截全屏
driver.save_screenshot('baidu.png')

driver.close()
