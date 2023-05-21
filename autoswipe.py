# -*- coding: utf-8 -*-
"""
Created on Wed Jun 23 23:56:03 2021
@author: Mert
"""

import undetected_chromedriver as uc
from selenium.common.exceptions import NoSuchElementException    
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import random
import atexit
import time
from timeit import default_timer as timer
 
global webdriver
#Bot Settings#
###########
CHROME_VERSION = 111
###########
url = "https://tinder.com/app/recs"
likeID = "button[class*='$g-ds-background-like']"
noThanksID = "button[class*='c1p6lbu0']"
noThanksSuperLikeID = "button[class*='button Lts($ls-s) Z(0) CenterAlign Mx(a) Cur(p) Tt(u) Ell Bdrs(100px) Px(24px) Px(20px)--s Py(0) Mih(40px) C($c-ds-text-secondary) C($c-ds-text-primary):h Fw($semibold) focus-button-style D(b) Mx(a)']"
swipeDelay = 0.3
###########

def checkButton(id):
    try:
        webdriver.find_element(By.CSS_SELECTOR, id)
    except NoSuchElementException:
        return False
    return True

def restart():
        import sys
        print("argv was",sys.argv)
        print("sys.executable was", sys.executable)
        print("restart now")

        import os
        os.execv(sys.executable, ['python'] + sys.argv)

def exit_handler():
    # telegram_send.send(messages=[errorMessage], disable_web_page_preview=True)
    webdriver.quit()
    restart()


def bot():
    print("BOT IS STARTING...")

    options = uc.ChromeOptions()
    options.add_argument('--log-level=3')
    options.add_argument('--user-data-dir=C:/Users/Mert/AppData/Local/Google/Chrome/User Data/')
    options.add_argument('--no-first-run --no-service-autorun --password-store=basic')
    options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36')
    global webdriver
    webdriver = uc.Chrome(options=options, version_main=CHROME_VERSION)  # version_main allows to specify your chrome version instead of following chrome global version
    webdriver.implicitly_wait(0.1)
    webdriver.maximize_window()
    atexit.register(exit_handler)
    webdriver.get(url)
    time.sleep(6)

    while True:
        time.sleep(swipeDelay)

        if (checkButton(noThanksID)):
            time.sleep(swipeDelay)
            webdriver.find_element(By.CSS_SELECTOR, noThanksID).click()
            time.sleep(swipeDelay)

        if (checkButton(noThanksSuperLikeID)):
            time.sleep(swipeDelay)
            webdriver.find_element(By.CSS_SELECTOR, noThanksSuperLikeID).click()
            time.sleep(swipeDelay)

        if (checkButton(likeID)):
            webdriver.find_element(By.CSS_SELECTOR, likeID).click()
            time.sleep(swipeDelay)
        else:
            webdriver.refresh()
            time.sleep(6)

#CODE RUN
if __name__ == "__main__": 
    bot()