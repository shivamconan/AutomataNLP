import nltk
from nltk.corpus import BracketParseCorpusReader
from tagger import *
from driver import *
from selenium import webdriver
import os

my_driver = None
def get_tagger():
    dirname = os.path.dirname(__file__)
    corpus_root = os.path.join(dirname, 'training_data')
    testcaselists = BracketParseCorpusReader(corpus_root, ['click.txt', 'enter_text.txt', 'browser.txt', 'load_url.txt', 'keyboard_actions.txt'])
    tagger = ConsecutivePosTagger(testcaselists.tagged_sents())
    return tagger

def get_action(tags):
    for (word, tag) in tags:
        if str(tag) == "A":
            return word.lower()
        
def get_action_item_name(tags):
    for (word, tag) in tags:
        if tag == 'AIN':
            return word.lower()

def get_action_item_kind(tags):
    for (word, tag) in tags:
        if tag == 'AIK':
            return word.lower()

def get_action_data(tags):
    for (word, tag) in tags:
        if tag == 'AD':
            return word.lower()
        
def perform_action(action, action_item_name, action_item_kind, action_data):
    print action, action_item_name, action_item_kind, action_data
    global my_driver
    if action_item_kind == "browser":
            my_driver = Driver(action_item_name)
    elif action == "load":
            if action_item_kind.lower() == "url" :
                if "www." in action_data:
                    my_driver.load_url(action_data)
    elif action == "enter" or action == "type":
            my_driver.enter_text(action_data, action_item_name, action_item_kind)
    elif action == "hit" or action == "press":
            my_driver.keyboard_action(action, action_data)
    elif action == "click":
            my_driver.click(action_item_name, action_item_kind)
              
tagger = get_tagger()                    
while True: 
    test_step = raw_input("Enter step")
    if test_step == "exit":
        my_driver.close_browser()
        break
    tags = tagger.tag(nltk.word_tokenize(test_step))
    print tags
    perform_action(get_action(tags), get_action_item_name(tags), get_action_item_kind(tags), get_action_data(tags))
        
    
     
    



