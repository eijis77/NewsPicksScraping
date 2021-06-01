# coding:utf-8
import time
from selenium.webdriver.common.keys import Keys
from selenium import webdriver

url_list = [
    # urlの配列
    '',
    '',
    ''
]

# ブラウザを開く。
browse = webdriver.Chrome(executable_path='/Users/Macのユーザー名/chromedriver')

# newspicksのトップページ
browse.get('https://newspicks.com/user/#######')
# 2秒待ちます
time.sleep(2)

#ログインボタンクリック
button_password = browse.find_element_by_id('login-id')
button_password.click()

# メールアドレス入力
email = browse.find_element_by_id('login-username')
email.click()
email.send_keys('メールアドレス')

# パスワード入力
password = browse.find_element_by_id('login-password')
password.click()
password.send_keys('パスワード')

# ログインボタンクリック
button_username = browse.find_element_by_id('login-btn-id')
button_username.click()

time.sleep(1)

for url in url_list:

    time.sleep(3)

    pick_button = browse.find_element_by_class_name("pick")
    pick_button.click()

    #time.sleep(1)

    text_field1 = browse.find_element_by_class_name("url-value")
    text_field1.send_keys(url)

    time.sleep(3)

    register_button = browse.find_element_by_class_name("pick-img")
    register_button.click()

    time.sleep(4)
