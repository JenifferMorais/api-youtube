import time
from datetime import date

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import re

from selenium.webdriver.support import wait
from selenium.webdriver.support.wait import WebDriverWait

def stringToData(str):
    str = str.split(" ")

    if (str[1] == "Jan"):
        dataFinal = f"{str[0]}/01/{str[2]}"
    if (str[1] == "Feb"):
        dataFinal = f"{str[0]}/02/{str[2]}"
    if (str[1] == "Mar"):
        dataFinal = f"{str[0]}/03/{str[2]}"
    if (str[1] == "Apr"):
        dataFinal = f"{str[0]}/04/{str[2]}"
    if (str[1] == "May"):
        dataFinal = f"{str[0]}/05/{str[2]}"
    if (str[1] == "Jun"):
        dataFinal = f"{str[0]}/06/{str[2]}"
    if (str[1] == "Jul"):
        dataFinal = f"{str[0]}/07/{str[2]}"
    if (str[1] == "Aug"):
        dataFinal = f"{str[0]}/08/{str[2]}"
    if (str[1] == "Sep"):
        dataFinal = f"{str[0]}/09/{str[2]}"
    if(str[1] == "Oct"):
        dataFinal = f"{str[0]}/10/{str[2]}"
    if (str[1] == "Nov"):
        dataFinal = f"{str[0]}/11/{str[2]}"
    if(str[1] == "Dec"):
        dataFinal = f"{str[0]}/12/{str[2]}"
    return dataFinal



start_time = time.time()
chrome_options = Options()
driver = webdriver.Chrome(executable_path=r"C:\chromedriver.exe")
driver.get('https://www.oddsportal.com/soccer/')
driver.maximize_window()
time.sleep(5)
btn_login = driver.find_element(By.XPATH, '//*[@id="app"]/div/header/div[2]/div[5]/div[1]').click()
user_input = driver.find_element(By.XPATH, '//*[@id="login-username-sign"]')
password_input = driver.find_element(By.XPATH, '//*[@id="login-password-sign-m"]')
time.sleep(3)
user_input.send_keys("jcsmz")
password_input.send_keys("93218074jjK")
time.sleep(2)
btn_login_final = driver.find_element(By.XPATH, '//*[@id="loginDiv"]/div[2]/div/div/form/div[4]/span').click()
time.sleep(5)
test = 1
arquivo = open('anos 1.txt', 'r')
result = open("games.txt","w")
linksMenores = open("LinksMenores.txt", "w")
for f in arquivo:
    driver.get(f"https://www.google.com/")
    url = f.replace(',', '').strip()
    driver.get(url)
    time.sleep(6)
    driver.execute_script(f"window.scrollBy(0,2500)", "")
    time.sleep(2)
    driver.execute_script(f"window.scrollBy(2800,3400)", "")
    time.sleep(2)
    inicial = driver.page_source
    soupi = BeautifulSoup(inicial, features="html.parser")
    time.sleep(1)
    driver.execute_script(f"window.scrollBy(3000,0)", "")
    dia = soupi.find_all("div", {"class": "flex flex-col w-full text-xs eventRow"})
    print(f"QTD JOGOS: {len(dia)}")
    print(f"{url}\n")
    if(int(len(dia)) < 49 ):
        linksMenores.write(f"{url},\n")
    cont = 0
    while cont < int(len(dia)):
        a = soupi.find_all("div", {"class": "flex flex-col w-full text-xs eventRow"})[cont]
        horario = soupi.find_all("div", {"class": "flex flex-col w-full text-xs eventRow"})[cont].find_all("p", {"class": "whitespace-nowrap"})[0].getText()
        if("'" not in horario):
            try:
                data = soupi.find_all("div", {"class": "flex flex-col w-full text-xs eventRow"})[cont].find_all("div", {"class": "w-full text-xs font-normal leading-5 text-black-main font-main"})[0].getText()
                if ("Yesterday" in str(data)):
                    data = "19/02/2023"
                elif ("Today" in str(data)):
                    data = "20/02/2023"
                else:
                    data = stringToData(data.split(" - ")[0])
            except:
                pass

            try:
                timeHome = soupi.find_all("div", {"class": "flex flex-col w-full text-xs eventRow"})[cont].find_all("div", {"class": "relative block truncate whitespace-nowrap group-hover:underline next-m:!ml-auto text-[#000000]"})[0].getText()
            except:
                timeHome = soupi.find_all("div", {"class": "flex flex-col w-full text-xs eventRow"})[cont].find_all("div", {
                    "class": "relative block truncate whitespace-nowrap group-hover:underline font-bold next-m:!ml-auto text-[#000000]"})[
                    0].getText()
            try:
                timeAway = soupi.find_all("div", {"class": "flex flex-col w-full text-xs eventRow"})[cont].find_all("div", {"class": "relative block truncate whitespace-nowrap group-hover:underline font-bold text-[#000000]"})[0].getText()
            except:
                timeAway = soupi.find_all("div", {"class": "flex flex-col w-full text-xs eventRow"})[cont].find_all("div", {
                    "class": "relative block truncate whitespace-nowrap group-hover:underline text-[#000000]"})[
                    0].getText()

            try:
                resultado = soupi.find_all("div", {"class": "flex flex-col w-full text-xs eventRow"})[cont].find_all("div", {"class": "hidden flex-col items-center next-m:!flex justify-center gap-1 pt-1 pb-1 border-black-borders min-w-[60px]"})[0].getText()
            except:
                resultado = soupi.find_all("div", {"class": "flex flex-col w-full text-xs eventRow"})[cont].find_all("div", {"class": "hidden flex-col items-center next-m:!flex justify-center gap-1 pt-1 pb-1 border-black-main border-opacity-10 min-w-[60px]"})[0].getText()
            if("canc." not in str(resultado) and "award." not in str(resultado) and "w.o" not in str(resultado) and "abn" not in str(resultado)):
                if("pen" in str(resultado)):
                    resultado = resultado.replace("pen.", "")
                    resultado = resultado.split(" ")[0]
                    resultado = resultado.split(":")
                    if(int(resultado[0]) > int(resultado[1])):
                        resultado[0] = int(resultado[0]) - 1
                    if (int(resultado[1]) > int(resultado[0])):
                        resultado[1] = int(resultado[1]) - 1
                    golsHome = resultado[0]
                    golsAway = resultado[1]
                elif("ET" in str(resultado)):
                    resultado = resultado.split(" ")[0]
                    golsHome = resultado.split(":")[0]
                    golsAway = resultado.split(":")[1]
                else:

                    try:
                        golsHome = resultado.split(":")[0]
                        golsAway = resultado.split(":")[1]
                    except:
                        print(resultado)
                        golsHome = "-"
                        golsAway = "-"
                try:
                    oddHome = soupi.find_all("div", {"class": "flex flex-col w-full text-xs eventRow"})[cont].find_all("div", {
                    "class": "flex-center flex-col gap-1 pt-1 pb-1 border-black-borders min-w-[60px]"})[0].getText()
                except:
                    oddHome = soupi.find_all("div", {"class": "flex flex-col w-full text-xs eventRow"})[cont].find_all("div", {
                        "class": "flex-center flex-col gap-1 pt-1 pb-1 border-l border-black-borders min-w-[60px]"})[0].getText()
                try:
                    oddAway= soupi.find_all("div", {"class": "flex flex-col w-full text-xs eventRow"})[cont].find_all("div", {
                    "class": "flex-center flex-col gap-1 pt-1 pb-1 border-l border-black-main border-opacity-10 min-w-[60px]"})[2].getText()
                except:
                    oddAway = soupi.find_all("div", {"class": "flex flex-col w-full text-xs eventRow"})[cont].find_all("div", {
                        "class": "flex-center flex-col gap-1 pt-1 pb-1 border-l border-black-borders min-w-[60px]"})[
                        2].getText()
                try:
                    oddDraw = soupi.find_all("div", {"class": "flex flex-col w-full text-xs eventRow"})[cont].find_all("div", {
                    "class": "flex-center flex-col gap-1 pt-1 pb-1 border-l border-black-main border-opacity-10 min-w-[60px]"})[1].getText()
                except:
                    oddDraw = soupi.find_all("div", {"class": "flex flex-col w-full text-xs eventRow"})[cont].find_all("div", {
                        "class": "flex-center flex-col gap-1 pt-1 pb-1 border-l border-black-borders min-w-[60px]"})[
                        1].getText()
                result.write(f"{data},{horario},{timeHome}, {timeAway}, {golsHome}, {golsAway}, {oddHome},{oddDraw},{oddAway},\n")
        cont = cont + 1