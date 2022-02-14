from selenium import webdriver
from selenium.common.exceptions import WebDriverException

import argparse
import logging
import random
import time

logger = logging.getLogger('InstaBOT')
logger.setLevel(logging.DEBUG)

class InstaBot():
    def __init__(self, chromedriver_path, username, password):
        self.__driver = webdriver.Chrome(chromedriver_path)
        self.__driver.implicitly_wait(15)
        self.__driver.get("https://www.instagram.com/accounts/login/?source=auth_switcher")
        self.login(username, password)
    
    def login(self, username_ig, password_ig):
        time.sleep(4)
        self.__driver.find_element_by_name('username').send_keys(username_ig)
        self.__driver.find_element_by_name('password').send_keys(password_ig)
        time.sleep(5)
        self.__driver.find_element_by_class_name('L3NKy       ').click()
        time.sleep(3)
    
    def like(self, keyword, number):
        self.__search(keyword)
        time.sleep(5)
        try:
            time.sleep(3)
            self.__driver.find_elements_by_class_name('_9AhH0')[10].click()
            self.__driver.find_element_by_class_name('fr66n').click()

        except WebDriverException:
            return
        
        for i in range(random.randint(int(number)-50, int(number)+50)):
            try:
                self.__driver.find_element_by_class_name('l8mY4').click()
                time.sleep(random.randint(random.randint(15, 18), random.randint(20, 22)))
            except:
                pass
            
            try:
                self.__driver.find_element_by_class_name('fr66n').click()
                time.sleep(5)
            except:
                pass
            
        
    
    def __search(self, keyword):
        self.__driver.get("https://www.instagram.com/explore/tags/" + keyword)
        
        

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-u', '--username', required=True, help="Instagram Username")
    parser.add_argument('-p', '--password', required=True, help="Instagram Password")
    parser.add_argument('-c', '--chromedriver', required=True, help="Chromedriver Path")
    parser.add_argument('-s', '--hashtag', required=True, help="HashTag to be actioned")
    parser.add_argument('-n', '--n_likes', default=100, help="Number of Likes")
    
    args = parser.parse_args()
    my_bot = InstaBot(chromedriver_path = args.chromedriver, 
                      username = args.username,
                      password = args.password
                    )
    my_bot.like(args.hashtag, args.n_likes)

if __name__ == '__main__':
    main()