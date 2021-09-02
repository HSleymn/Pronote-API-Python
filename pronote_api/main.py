from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from tkinter import *   
from functools import partial  


def average_result(result_label, n1,n2, n3):
    num1 = (n1.get())
    num2 = (n2.get())
    num3 = (n3.get())
    try:
        result =(int(num1) + int(num2) + int(num3))/3
    except:
        try:
            DeleteErrorMessage()
        except:
            pass

        ValueErrorEx()
    else:
        try:
            DeleteErrorMessage()
        except:
            pass

        result_label.config(text=f"Votre moyenne est de {result} .")

def ValueErrorEx():
    global VEX
    VEX = Label(window, bg="#1068a4", fg="white", font=('Arial',"30", "bold"), text="Merci d'insérer des nombres")
    VEX.pack()

def DeleteErrorMessage():
   VEX.after(0, VEX.destroy())

def DeleteLabelResult():
    labelResult.config(text="")

window = Tk()
window.title("Average Calculator")
window.geometry("1080x720")
window.minsize(480, 360)
window.config(background='#1068a4')

wlcm_message = Label(window, bg='#1068a9', fg='white', font=('Arial',"75", "bold"), text="Bienvenue à toi ! ")
wlcm_message.place(relx=0.5, rely=0.5, anchor=CENTER) 
wlcm_message.pack(expand=YES)

number_1 = StringVar()
number_2 = StringVar()
number_3 = StringVar()

labelNum1 = Label(window, bg="#1068a4", fg="white", font=('Arial',"30", "bold"),text="Note numéro 1 :", borderwidth=0, highlightthickness=0)
labelNum1.pack(expand=YES)


entryNum1 = Entry(window, textvariable=number_1)
entryNum1.pack(expand=YES)

labelNum2 = Label(window, bg="#1068a4",fg="white", font=('Arial',"30", "bold"), text="Note numéro 2 :", borderwidth=0, highlightthickness=0)
labelNum2.pack(expand=YES)
entryNum2 = Entry(window, textvariable=number_2 )
entryNum2.pack(expand=YES)

labelNum3 = Label(window, bg="#1068a4",fg="white", font=('Arial',"30", "bold"), text="Note numéro 3 :", borderwidth=0, highlightthickness=0)
labelNum3.pack(expand=YES)
entryNum3 = Entry(window, textvariable=number_3 )
entryNum3.pack(expand=YES)

labelResult = Label(window, bg="#1068a4", fg="white",font=('Arial',"30", "bold"))
labelResult.pack(expand=YES)

average_result = partial(average_result, labelResult, number_1, number_2, number_3)

click_btn_img = PhotoImage(file='button.jpg')
img_label= Label(image=click_btn_img)

CalculateBut = Button(window, image= click_btn_img,bg="#1068a4",activebackground="#1068a4", command=average_result, height=150, width=500, borderwidth=0, highlightthickness=0)
CalculateBut.pack(expand=YES)



window.mainloop()

