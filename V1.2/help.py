from tkinter import *   
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from tkinter import *   
from functools import partial  

def website_help():
    driver = webdriver.Firefox()
    driver.get("https://github.com/HSleymn/Pronote-API-Python/blob/master/README.md")

def help_page():
    window = Tk()
    window.title("Documentation")
    window.geometry("1080x720")
    window.minsize(480, 360)
    window.config(background='#1068a4')

    text_doc = Label(window, bg="#1068a4", fg="white", font=('Arial',"25", "bold"), text="Programme réalisé par HSleymn")
    text_doc.pack(expand=YES)

    btn_github_website = Button(window,text="Clique ici pour accéder à la documentation complète",activebackground="#1068a4", 
    bg="#1068a4", fg="white",font=('Arial',"20", "bold"), command=website_help, borderwidth=1, highlightthickness=0)

    btn_github_website.place(relx=0.5, rely=0.5, anchor=CENTER)

    window.mainloop()