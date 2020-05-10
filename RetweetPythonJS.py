#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from selenium import webdriver
from bs4 import BeautifulSoup
import string
import time

import random

from random import randint

import os
import sys
import codecs
import pprint

from selenium.webdriver.common.keys import Keys
import selenium.webdriver.support.ui as ui
driver = webdriver.Chrome(executable_path="C:\chromedriver.exe")     

def test_search_in_python_org():
    driver.get("https://twitter.com/")
    time.sleep(2)

    driver.maximize_window()

    username = driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[2]/div/div[2]/div/div/div/div[1]/section/form/div/div[1]/div/label/div/div[2]/div/input')
    password = driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[2]/div/div[2]/div/div/div/div[1]/section/form/div/div[2]/div/label/div/div[2]/div/input')

    username.send_keys("immy74216186")
    password.send_keys("<Immy@123>")
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[2]/div/div[2]/div/div/div/div[1]/section/form/div/div[3]/div').click()
    time.sleep(2)

test_search_in_python_org()
while(True):
    try:
        driver.get('https://twitter.com/search?q=%23earthquake&src=trend_click')
        time.sleep(6)
        driver.execute_script('''
(() => {
  const retweetButtonQuery = '[data-testid="retweet"]';
  const retweetconfirmButtonQuery = '[data-testid="retweetConfirm"]';
  const sleep = ({ seconds }) =>
    new Promise(proceed => {
      console.log(`WAITING FOR ${seconds} SECONDS...`);
      setTimeout(proceed, seconds * 1000);
    });

  const nextBatch = async () => {
    try{
      window.scrollTo(0, document.body.scrollHeight);
      await sleep({ seconds: 1 });

      const retweetButtons = Array.from(document.querySelectorAll(retweetButtonQuery));
      const retweetButtonCount = retweetButtons.length;

      if (retweetButtonCount === 0) {
        console.log(`NO TWEETS FOUND, SO I THINK WE'RE DONE`);
        console.log(`RELOAD PAGE AND RE-RUN SCRIPT IF ANY WERE MISSED`);
        return;
      }

      await Promise.all(
        retweetButtons.map(async retweetButton => {
          retweetButton.click();
          await sleep({ seconds: 1 });
          const confirmButton = document.querySelector(retweetconfirmButtonQuery);
          confirmButton.click();
        })
      );

      await sleep({ seconds: 25 });
      nextBatch();
    }
    catch(e){
      console.log("Error ",e)
      nextBatch();
    }
  };

  nextBatch();
})();''')
        time.sleep(200)
    except Exception as e:
        print(e)
        time.sleep(20)
