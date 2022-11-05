from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

import time
import csv
import json
import os
from collections import namedtuple

import requests
import base64
from googleapiclient.discovery import build

from selenium.webdriver.common.by import By
def dadoVideo(url_video):
    link = url_video
    chrome_options = Options()
    chrome_options.add_argument("user-data-dir=C:/Users/jeniffer.morais/AppData/Local/Google/Chrome/User Data")
    driver = webdriver.Chrome(executable_path=r"C:\chromedriver.exe", options=chrome_options)
    driver.maximize_window()
    driver.get(url_video)
    time.sleep(6)
    with open('CSV/resultado.csv', 'a', encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile);
        writer.writerow(['Link', 'Visualizações', 'Like', 'Deslikes', 'Comentário', 'Like_Comentarios', 'Qtd_Caracteres','Código', 'Opinião','Emoji?', 'Tristeza', 'Alegria', 'Medo', 'Aversao', 'Raiva', 'Pontuacao', 'Resultado'])
        driver.execute_script('window.scrollBy(0, 445)')
        time.sleep(6)
        i = 0
        #window.scrolBy para descer a página e carregar os comentários
        while i<15:
            i=i+1
            driver.execute_script('window.scrollBy(0, 2445)')
            time.sleep(2)


        #Pegar todoo o HTML da página atual e colocar no BeautifulSoup para que possamos fazer buscas
        soup = BeautifulSoup(driver.page_source, features="html.parser")

        #Pegar o número de visualizações e os likes
        dados = soup.find_all("yt-formatted-string", {"class": "factoid-value style-scope ytd-factoid-renderer"})
        deslikes = soup.find_all("span", {"id": "text"})[0].get_text()

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
                if (len(img) > 0):
                    temImagem = "SIM"
                else:
                    temImagem = "NÃO"
                if comment[count].find_all("span") == []:
                    caracteres = int(len(comment[count].get_text().replace(' ', '')))
                    x = analise_sentimentos(comment[count].get_text().replace(",", "-").strip())

                    if ("<" in comment[count].get_text() or "==" in comment[count].get_text() or "div" in comment[
                        count].get_text() or "()" in comment[count].get_text() or "print" in comment[
                        count].get_text() or "!=" in comment[count].get_text() or "+=" in comment[count].get_text()
                            or "<table>" in comment[count].get_text() or "<tr>" in comment[count].get_text() or "<td>" in
                            comment[count].get_text() or "+=" in comment[count].get_text()):
                        writer.writerow([link, visualizacoes, likess, deslikes, comment[count].get_text().replace(",", "-").strip(),
                                         likeAndDeslike.strip(), caracteres, 'Sim', 'Não', temImagem, str(x[0]), str(x[1]), str(x[2]), str(x[3]), str(x[4]), str(x[5]), str(x[6])])
                    else:
                        writer.writerow([link, visualizacoes, likess, deslikes, comment[count].get_text().replace(",", "-").strip(),
                                         likeAndDeslike.strip(), caracteres, 'Não', 'Sim', temImagem, str(x[0]), str(x[1]), str(x[2]), str(x[3]), str(x[4]), str(x[5]), str(x[6])])
                else:
                    spans = comment[count].find_all("span")
                    comentario = ""
                    for s in spans:
                        comentario = comentario + s.get_text().strip()
                    caracteres = int(len(comentario.replace(' ', '')))
                    x = analise_sentimentos(comentario.replace(",", "-").strip())

                    if ("<" in comentario or "==" in comentario or "div" in comentario or "()" in comentario):
                        writer.writerow(
                            [link, visualizacoes, likess, deslikes, comentario.replace(",", "-").strip(), likeAndDeslike.strip(),
                             caracteres, 'Sim', 'Não', temImagem, str(x[0]), str(x[1]), str(x[2]), str(x[3]), str(x[4]), str(x[5]), str(x[6])])
                    else:
                        writer.writerow(
                            [link, visualizacoes, likess, deslikes, comentario.replace(",", "-").strip(), likeAndDeslike.strip(),
                             caracteres, 'Não', 'Sim', temImagem, str(x[0]), str(x[1]), str(x[2]), str(x[3]), str(x[4]), str(x[5]), str(x[6])])
                count = count + 1

def analise_sentimentos(comment):
    analysis_list = []
    result = ['0.0', '0.0', '0.0', '0.0', '0.0', '0.0', '0.0']
    if (comment != ""):
        url = 'https://api.gotit.ai/NLU/v1.5/Analyze'
        data = {"T": comment, "S": True, "EM": True}

        data_json = json.dumps(data)
        userAndPass = base64.b64encode(
            b"2274-jVwH/V0Q:gq3STLhSz2IY3Bey+btyOmN7xpo+HuK5kSRtLK+/").decode("ascii")
        headers = {'Content-type': 'application/json', "Authorization": "Basic %s" % userAndPass}
        response = requests.post(url, data=data_json, headers=headers)

        # print(comment, '\n', dict(response.json())['sentiment']['label'], end=('\n' * 2))

        dictionary = {"comment": comment, "analysis": response.json()}
        analysis_list.append(dictionary)

        analysis_json = json.dumps(analysis_list, indent=4, ensure_ascii=False)
        x = json.loads(analysis_json, object_hook=lambda d: namedtuple('X', d.keys())(*d.values()))

        # 'Sadness', 'Joy', 'Fear', 'Disgust', 'Anger', 'Score', 'Label'
        result = [x[0].analysis.emotions.sadness,
                x[0].analysis.emotions.joy,
                x[0].analysis.emotions.fear,
                x[0].analysis.emotions.disgust,
                x[0].analysis.emotions.anger,
                x[0].analysis.sentiment.score,
                x[0].analysis.sentiment.label]

    return result

if __name__ == '__main__':
    dadoVideo("https://www.youtube.com/watch?v=XinLASYOJE4")