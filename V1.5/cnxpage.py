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
from prout import *

window = Tk()
window.title("Page de connexion")
window.geometry("480x360")
window.minsize(480, 360)
window.config(background='#1068a4')

username_id = StringVar()
password_id = StringVar()
entryusername = Entry(window, textvariable=username_id)
entryusername.pack()

entrypassword = Entry(window, textvariable=password_id)
entrypassword.pack()
feuvert = partial(prout, username_id, password_id)
CnxBut = Button(window,bg="#1068a4",activebackground="#1068a4", command=feuvert)
CnxBut.pack(expand=YES)

window.mainloop()
