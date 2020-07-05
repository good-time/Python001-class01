from selenium import webdriver
import time

try:
    browser = webdriver.Chrome()
    # 需要安装chrome driver, 和浏览器版本保持一致
    # http://chromedriver.storage.googleapis.com/index.html
    browser.get('https://shimo.im')
    time.sleep(1)
    btn = browser.find_element_by_xpath('//*[@class="login-button btn_hover_style_8"]')
    btn.click()

    browser.find_element_by_xpath('//*[@name="mobileOrEmail"]').send_keys('1421787775@qq.com')
    time.sleep(1)
    browser.find_element_by_xpath('//*[@name="password"]').send_keys('test1234')
    time.sleep(1)
    browser.find_element_by_xpath('//button[@class="sm-button submit sc-1n784rm-0 bcuuIb"]').click()

    cookies = browser.get_cookies() # 获取cookies
    print(cookies)
    time.sleep(3)
except Exception as e:
    print(e)
finally:    
    browser.close()