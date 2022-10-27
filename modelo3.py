from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time
import csv

from selenium.webdriver.common.by import By
link = "https://www.youtube.com/watch?v=iFYWrDMfVNo"
chrome_options = Options()
driver = webdriver.Chrome(executable_path=r"C:\chromedriver.exe", options=chrome_options)
driver.maximize_window()
driver.get("https://www.youtube.com/watch?v=iFYWrDMfVNo")
time.sleep(6)
with open('dados.csv', 'w', encoding="utf-8") as csvfile:
    writer = csv.writer(csvfile);
    writer.writerow(['Link', 'Visualizações', 'Like', 'Comentário', 'Like_Comentarios', 'Qtd_Caracteres','Tipo', 'Emoji?'])
    driver.execute_script('window.scrollBy(0, 445)')
    time.sleep(6)
    i = 0
    #window.scrolBy para descer a página e carregar os comentários
    while i<3:
        i=i+1
        driver.execute_script('window.scrollBy(0, 2445)')
        time.sleep(2)


    #Pegar todoo o HTML da página atual e colocar no BeautifulSoup para que possamos fazer buscas
    soup = BeautifulSoup(driver.page_source, features="html.parser")

    #Pegar o número de visualizações e os likes
    dados = soup.find_all("yt-formatted-string", {"class": "factoid-value style-scope ytd-factoid-renderer"})
    likess = dados[0].get_text()
    visualizacoes = dados[1].get_text()

    #Realizamos uma busca em todas as Tags que contenham comentário, começando com TAG o identificador, Ex: "class", ou "id" e na frente o nome do respectivo campo
    comment = soup.find_all("yt-formatted-string", {"id": "content-text"})

    #Percorre os comentários e coleta todos os "spans" que é onde está localizado o texto dos comentários
    count = 0
    while count < len(comment):
        likeAndDeslike = soup.find_all("ytd-comment-action-buttons-renderer", {"id": "action-buttons"})[count].find_all("span")[0].get_text()
        opniao = True
        img = comment[count].find_all("img")
        if(len(img) > 0):
            temImagem = "SIM"
        else:
            temImagem = "NÃO"
        if comment[count].find_all("span") == []:
            caracteres = int(len(comment[count].get_text().replace(' ','')))
            if("<" in comment[count].get_text() or "==" in comment[count].get_text() or "div" in comment[count].get_text() or "()" in comment[count].get_text()):
                writer.writerow([link, visualizacoes, likess, comment[count].get_text().replace(",","-").strip(), likeAndDeslike.strip(), caracteres, 'Código', temImagem])
            else:
                writer.writerow([link, visualizacoes, likess, comment[count].get_text().replace(",","-").strip(), likeAndDeslike.strip(), caracteres, 'Opnião',temImagem])
        else:
            spans = comment[count].find_all("span")
            comentario = ""
            for s in spans:
                comentario = comentario + s.get_text().strip()
            caracteres = int(len(comentario.replace(' ','')))
            if ("<" in comentario or "==" in comentario or "div" in comentario or "()" in comentario):
                writer.writerow([link,visualizacoes,likess,comentario.replace(",","-").strip(),likeAndDeslike.strip(),caracteres,'Código',temImagem])
            else:
                writer.writerow([link,visualizacoes,likess,comentario.replace(",","-").strip(),likeAndDeslike.strip(),caracteres,'Opnião',temImagem])
        count = count + 1