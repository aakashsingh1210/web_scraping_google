import os
import os.path
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
import cred
import urllib.request
from test4 import testing

with open("test5.txt","r") as f:
    while True:
        line=f.readline().strip()
        if not line or line==" ":
            break
        a,b,c=line.split(",")
        testing(int(a),int(b),int(c))


