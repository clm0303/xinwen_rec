# https://preview-pdf.xuexi.cn/5c26096099b6672f682e791a/92go8fxk2p6.pdf/doc/I/{}.format()


from selenium import webdriver
from selenium.webdriver import ActionChains
import csv
import codecs
import requests
import re
import json
import time
import random
import pymysql
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from lxml import etree

driver = webdriver.Chrome(r"C:\Program Files (x86)\Google\Chrome\Application\chromedriver")

for i in range(20, 30):
    driver.get('https://preview-pdf.xuexi.cn/5b6e84d8d3318a5436f6f9a0/bds19i1ck5t.pdf/doc/I/{}'.format(i))
    time.sleep(1)
driver.quit()
# driver.get('https://preview-pdf.xuexi.cn/5c26096099b6672f682e791a/92go8fxk2p6.pdf/doc/I/{}'.format(i))
# time.sleep(1)
