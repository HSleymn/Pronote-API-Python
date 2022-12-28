from tkinter import *   
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from functools import partial  
import time
from replace import *
from xpathsbase import *

def prout(usernameid, passwordid):
    username = usernameid.get()
    password = passwordid.get()

    driver = webdriver.Firefox(executable_path="geckodriver.exe")
    driver.get("https://0950646l.index-education.net/pronote/eleve.html?identifiant=9W7u2z7V5ZfJxYrV")

    time.sleep(8)

    print("Page est prête")

    id_bar = driver.find_element_by_id('email')
    id_bar.send_keys(username)
    print(username)
    pswd_bar = driver.find_element_by_id("password")
    pswd_bar.send_keys(password)
    print(password)
    connection_btn = driver.find_element_by_class_name("flex-magnet-bottom-right")
    connection_btn.click()

    delay = 10
    time.sleep(16)

    average_menu_btn = driver.find_element_by_id("GInterface.Instances[0].Instances[1]_Combo2")
    driver.execute_script("arguments[0].click();", average_menu_btn)

    print("Accès à Notes")

    delay = 10
    time.sleep(1)

    trimestre_menu_btn = driver.find_element_by_id("GInterface.Instances[2].Instances[0]_2")
    driver.execute_script("arguments[0].click();", trimestre_menu_btn)


    delay = 10
    time.sleep(10)

    list_grade = []

    score1 = driver.find_element_by_xpath(notesxpaths[0]).get_attribute("innerHTML")
    score1 = replace(score1,",",".")
    print(score1)
    list_grade.append(score1)
  

    score2 = driver.find_element_by_xpath(notesxpaths[1]).get_attribute("innerHTML")
    score2 = replace(score2,",",".")
    print(score2)
    list_grade.append(score2)

    score3 = driver.find_element_by_xpath(notesxpaths[2]).get_attribute("innerHTML")
    score3 = replace(score3,",",".")
    print(score3)
    list_grade.append(score3)   

    score4 = driver.find_element_by_xpath(notesxpaths[3]).get_attribute("innerHTML")
    score4 = replace(score4,",",".")
    print(score4)
    list_grade.append(score4)   

    score5 = driver.find_element_by_xpath(notesxpaths[4]).get_attribute("innerHTML")
    score5 = replace(score5,",",".")
    print(score5)
    list_grade.append(score5)   

    score6 = driver.find_element_by_xpath(notesxpaths[5]).get_attribute("innerHTML")
    score6 = replace(score6,",",".")
    print(score6)
    list_grade.append(score6)   

    score7 = driver.find_element_by_xpath(notesxpaths[6]).get_attribute("innerHTML")
    score7 = replace(score7,",",".")
    print(score7)
    list_grade.append(score7)   

    score8 = driver.find_element_by_xpath(notesxpaths[7]).get_attribute("innerHTML")
    score8 = replace(score8,",",".")
    print(score8)
    list_grade.append(score8)  

    score9 = driver.find_element_by_xpath(notesxpaths[8]).get_attribute("innerHTML")
    score9 = replace(score9,",",".")
    print(score9)
    list_grade.append(score9)   

    score10 = driver.find_element_by_xpath(notesxpaths[9]).get_attribute("innerHTML")
    score10 = replace(score10,",",".")
    print(score10)
    list_grade.append(score10)   

    score11 = driver.find_element_by_xpath(notesxpaths[10]).get_attribute("innerHTML")
    score3 = replace(score11,",",".")
    print(score11)
    list_grade.append(score11)   

    score12 = driver.find_element_by_xpath(notesxpaths[11]).get_attribute("innerHTML")
    score12 = replace(score12,",",".")
    print(score12)
    list_grade.append(score12)   


    moyenne = score1 + score2
    print(moyenne)