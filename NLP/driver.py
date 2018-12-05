from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from utility import *
from selenium.webdriver.common.action_chains import ActionChains
import os

class Driver:
    def __init__(self, browser_name):
        dirname = os.path.dirname(__file__)	
        if browser_name.lower() == "chrome":
            self.driver = webdriver.Chrome(os.path.join(dirname, 'drivers/chromedriver.exe'))
    
    def load_url(self, url):
        self.driver.get("https://" + url)    
        
    def enter_text(self, text, field_name, field_kind):
        all_inputs = self.driver.find_elements_by_xpath("//input")
        for input in all_inputs:
            outer_html = input.get_attribute("outerHTML").lower()
            if field_name in outer_html and field_kind in ["field", "textbox", "box"] and input.get_attribute("type") == "text":
                print outer_html
                input.clear()
                input.send_keys(text)
                break
                
    def keyboard_action(self, key_action, key):
        if key_action in ["press", "hit"]:
                ActionChains(self.driver).key_down(get_key(key)).key_up(get_key(key)).perform()
                
    def click(self, name, kind):
        if kind == "link":
            all_links = self.driver.find_elements_by_xpath("//a")
            for link in all_links:
                inner_html = link.get_attribute("innerHTML").lower()
                if name in inner_html:
                        print inner_html
                        link.click()
                        break
        if kind == "button":
            all_buttons = self.driver.find_elements_by_xpath("//button")
            for button in all_buttons:
                inner_html = link.get_attribute("innerHTML").lower()
                if name in inner_html:
                        button.click()
                        break
        
    
    def get_driver(self):
         return self.driver
                
    def close_browser(self):
        self.driver.close()