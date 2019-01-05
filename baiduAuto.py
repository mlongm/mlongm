#coding:utf-8
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import json
import time

op = webdriver.FirefoxOptions()
address = "https://tieba.baidu.com/index.html" 

#使用cookies登陆签到
def Qiandao(address):
    #指令模拟网页登陆。（无头模式）
    op.add_argument("--headless")   #等效于 ———— op.set_headless()
    op.add_argument("--disable-gpu")    #禁用GPU加速
    driver = webdriver.Firefox(firefox_options = op)
    driver.get(address) #这里必须先加载一下。
    #读取cookies
    with open('cookies.txt','r',encoding = 'utf-8') as f:
        cookie = f.read()
        cookie =json.loads(cookie)
    for c in cookie:
        driver.add_cookie(c)
    driver.refresh()
    #自动签到
    driver.implicitly_wait(5)
    trg = driver.find_element_by_xpath('//*[@id="onekey_sign"]/a')
    trg.click()
    driver.implicitly_wait(5)
    trg = driver.find_element_by_xpath('//*[@id="dialogJbody"]/div/div/div[1]/a')
    trg.click()
    driver.implicitly_wait(10)
    trg = driver.find_element_by_xpath('/html/body/div[7]/div/div[2]/div/div/div')
    msg = trg.text
    driver.close()
    return msg 

#main()
try:
    msg = Qiandao(address)
    st = msg.splitlines(True)
    with open('BD_sign_in.log','a',encoding = 'utf-8') as f:
        for i in range(4):
            f.write(st[i])
        f.write(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time())))
    print('签到信息已记录在本目录下BD_sign_in.log文件，可供查看。')
except:
    print("网页登陆错误，签到失败。")