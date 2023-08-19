#IMPORTS
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

#VARIABLES
passw=input("password: ")
login=input("login: ")
reviewSingular = "Freundlicher Gast. Gerne wieder Willkommen."
reviewPlural = "Freundliche Gäste. Gerne wieder Willkommen."
FINALreview = ""

#FULLSCREEN BROWSER
options = Options()
options.add_experimental_option("detach", True)

#DRIVER INITIALIZATION
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),
                          options=options)

#FUNCTIONS
def getBack(): #GETS YOU BACK TO HOSTING SITE
    driver.get("https://www.airbnb.de/hosting")
    try:
        reviews = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div[5]/div/div/div[1]/div/div/div[4]/main/div/div[2]/div/div/div/div/div[2]/div/div/span[5]/label/div/span"))
        )
        reviews.click()
    except:
        driver.quit()

def startreview(): #DOES A FULL REVIEW FOR A CUSTOMER
    try:
        a1 = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "._e8i7phm.l1ovpqvx.dir.dir-ltr"))
        )
        a1.click()
    except:
        driver.quit()
    blackButton()
    fivestar()
    blackButton()
    time.sleep(2)
    fivestar()
    blackButton()
    time.sleep(2)
    fivestar()
    blackButton()
    textmessage()
    blackButton()
    try:
        a3 = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div[5]/div/div/div[1]/div/div/main/section/div/div/div/div/div/div[3]/div/div[2]/label[1]"))
        )
        a3.click()
    except:
        driver.quit()
    blackButton()
    try:
        a2 = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".l1ovpqvx.b1luh1ah.c1j7xk73.dir.dir-ltr"))
        )
        a2.click()
    except:
        driver.quit()
    getBack()
    getBack()

def checkNumber(): #CHECKS IF ITS MORE THAN ONE PERSON AND CHANGES VARIABLE
    try:
        click = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "._9m9ayv"))
        )
        click.click()
    except:
        driver.quit()
    try:
        check = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".ll4r2nl.dir.dir-ltr"))
        )
        a = check.text
        finden = a.find("Gäste")
        global FINALreview
        if finden != -1:
            FINALreview = reviewPlural
        else:
            FINALreview = reviewSingular
    except:
        driver.quit()

def blackButton(): #CLICKS ON BLACK NEXT BUTTON
    try:
        a2 = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".l1ovpqvx.bmx2gr4.c1ih3c6.dir.dir-ltr"))
        )
        a2.click()
    except:
        driver.quit()

def fivestar(): #DOES A FIVESTAR REVIEW
    try:
        a3 = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div[5]/div/div/div[1]/div/div/main/section/div/div/div/div/div/div[3]/fieldset/div/label[5]"))
        )
        a3.click()
    except:
        print()

def textmessage(): #DEFINES REVIEW MESSAGE
    try:
        a3 = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "cid:public_review_text_area"))
        )
        a3.send_keys(FINALreview)
    except:
        driver.quit()


#PROGRAM SEQUENCE
driver.get("https://www.airbnb.de/login")
driver.maximize_window()
switchemail = driver.find_element(By.XPATH, "/html/body/div[5]/div/div/div[1]/div/div[2]/div[1]/main/div/div/div/div/div/div[3]/div/div[4]/button/div/div[2]")
switchemail.click()
search = driver.find_element(By.ID, 'email-login-email')
search.send_keys(login)
search.send_keys(Keys.RETURN)
try:
    search1 = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "email-signup-password"))
    )
    search1.send_keys(passw)
    search1.send_keys(Keys.RETURN)
except:
    driver.quit()
time.sleep(3)  
for i in range(6):
    getBack()
    checkNumber()
    getBack()
    startreview()


