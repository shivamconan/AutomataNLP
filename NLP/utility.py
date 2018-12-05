# -*- coding: utf-8 -*-
"""
Created on Sun Dec 02 19:27:53 2018

@author: HP
"""
from selenium.webdriver.common.keys import Keys

def get_key(user_input_key):
    if user_input_key == "enter":
        return Keys.ENTER
    
