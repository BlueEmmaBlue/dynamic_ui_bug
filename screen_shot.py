from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.utils import ChromeType
import time
import os
import sys

DRIVER_PATH = '/home/zhangwei/utils/chromium/chromedriver'
SCREEN_SHOT_PATH = '/home/zhangwei/code/result'

def open_url(url,origin_url,timeout=5,screenshot=False):
    mobile_emulation = {
        "deviceMetrics": {"width": 390, "height": 844, "pixelRatio": 3.0},  # 定义设备高宽，像素比
        "userAgent": "Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) "
                     "AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1"}  # 通过UA来模拟
    chrome_options = Options()
    chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
    #chrome_options.add_argument('headless')
    chrome_options.add_argument('test-type')
    chrome_options.add_argument('window-size=390,844')
    chrome_options.add_argument('ignore-certificate-errors')
    chrome_options.add_argument('ignore-privacy-errors')
    chrome_options.add_argument('ignore-ssl-errors')
    chrome_options.add_argument('user-data-dir=/tmp/nonexistent$(date +%s%N)')
    driver = webdriver.Chrome(service=Service(DRIVER_PATH),options=chrome_options)
#    driver.execute_cdp_cmd("Network.setCacheDisabled", {"cacheDisabled":True})

    driver.set_page_load_timeout(60)

    try:
         driver.get(url)
         time.sleep(2)
    except Exception as e:
        print(f'error load {url} for {e}')
    finally:
        # 截全屏
        if screenshot:
            driver.save_screenshot(f'{SCREEN_SHOT_PATH}/{origin_url}/screenshot.png')
        driver.close()

def test_webdriver(url,origin_url,timeout=5,screenshot=False):
    mobile_emulation = {
        "deviceMetrics": {"width": 390, "height": 844, "pixelRatio": 3.0},  # 定义设备高宽，像素比
        "userAgent": "Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) "
                     "AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1"}  # 通过UA来模拟
    options = Options()
    options.add_experimental_option("mobileEmulation", mobile_emulation)
    options.add_argument('test-type')
    options.add_argument('window-size=390,844')
    options.add_argument('ignore-certificate-errors')
    options.add_argument('ignore-privacy-errors')
    options.add_argument('ignore-ssl-errors')
    options.add_argument('user-data-dir=/tmp/nonexistent$(date +%s%N)')
    driver = webdriver.Chrome(service=Service(DRIVER_PATH),options=options)

    driver.set_page_load_timeout(60)

    try:
         driver.get(url)
         time.sleep(2)
    except Exception as e:
        print(f'error load {url} for {e}')
    finally:
        # 截全屏
        driver.close()



def main():
    url = sys.argv[1].strip()
    origin_url = url
    if 'google' in url:
        url = f'{url}/ncr'
    if 'http' not in url:
        url = f'https://{url}'
    screenshot = False
    if len(sys.argv) > 2:
        screenshot = (sys.argv[2] == 'screenshot')
    timeout = 5
    if len(sys.argv) > 3:
        timeout = int(sys.argv[3])
    open_url(url,origin_url,timeout,screenshot)
    #test_webdriver(url,origin_url,timeout,screenshot)

if __name__ == '__main__':
    main()
