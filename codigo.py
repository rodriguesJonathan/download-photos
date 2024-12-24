from selenium import webdriver
from time import sleep
from random import randint
from json import dumps, load
from urllib import urlretrieve


def justOneSecond():
    sleep(3)

#login
browser = webdriver.Firefox()
browser.get("https://www.facebook.com/")
justOneSecond()
userBox = browser.find_element("name","email")
passBox = browser.find_element("name","pass")
loginButton = browser.find_element("name","login")

userBox.send_keys(input("Digite seu email: "))
passBox.send_keys(input("Digite sua senha: "))
loginButton.click()
justOneSecond()

#site of photos
browser.get("https://www.facebook.com/jonathan.rodrigues.eh.lindo/photos_of")
justOneSecond()
pathFirstPhoto = '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div/div[4]/div/div/div/div/div/div/div/div/div[3]/div[1]/div[1]/div/div/a'
linkPhoto = browser.find_element("xpath", pathFirstPhoto)
linkPhoto.click()
justOneSecond()

#download imagem




browser.get("https://www.facebook.com/jonathan.rodrigues.eh.lindo/photos_of")
path = "/html/body/div[1]/div/div/div[1]/div/div[3]/div[1]/div/div[2]/div/div/section/div[2]/table/tbody/tr[%d]/td[%d]"
dateString = browser.find_element("xpath",path%(1,1))

firstDateTime = datetime.strptime(dateString, '%b %d, %Y')
previousDays = 10
lastDateTime = firstDateTime - timedelta(previousDays-1)



columnsTitles = ["Date", "BTC Closing Value"]
columnsValues = [columnsTitles]

row = 1
focusDateTime = firstDateTime
while focusDateTime > lastDateTime:
    dateString  = browser.find_element("xpath",path%(row,1)).text
    closeString = browser.find_element("xpath",path%(row,5)).text
    focusDateTime =  datetime.strptime(dateString, '%b %d, %Y')
    
    columnsValues.append([dateString, closeString])
    print([dateString, closeString])
    row += 1



with open("eur_btc_rates.csv", "w") as f:

   data = writer(f)
   data.writerows(columnsValues)