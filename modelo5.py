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

    cleon1 = planilhaCleon(url_video, 1)
    cleon2 = planilhaCleon(url_video, 2)

    vLikeComentario = 0.0
    vCodigo = 0
    vOpniao = 0
    vEmoji = 0
    vCaracteres = 0.0
    vTristeza = 0.0
    vAlegria = 0.0
    vMedo = 0.0
    vAversao = 0.0
    vRaiva = 0.0
    vPontuacao = 0.0
    vResultado = 0.0


    quantidadeTristeza = 0.0
    quantidadeAlegria = 0.0
    quantidadeMedo = 0.0
    quantidadeAversao = 0.0
    quantidadeRaiva = 0.0
    quantidadePontuacao = 0.0
    quantidadeResultado = 0.0

    quantidade = 0

    with open('CSV/modelo5-final-media (4).csv', 'a', encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)
        # writer.writerow(['Visualizacoes', 'Like', 'Deslikes', 'Like Comentarios', 'Qtd Caracteres', 'Codigo',
        #                    'Opiniao', 'Emoji ', 'Densidade semantica', 'Dificuldade',
        #                    'Tristeza', 'Alegria', 'Medo', 'Aversao', 'Raiva', 'Pontuacao', 'Resultado'])
        driver.execute_script('window.scrollBy(0, 445)')
        time.sleep(6)
        i = 0
        #window.scrolBy para descer a página e carregar os comentários
        while i<5:
            i=i+1
            driver.execute_script('window.scrollBy(0, 2445)')
            time.sleep(2)


        #Pegar todoo o HTML da página atual e colocar no BeautifulSoup para que possamos fazer buscas
        soup = BeautifulSoup(driver.page_source, features="html.parser")

        #Pegar o número de visualizações e os likes
        dados = soup.find_all("yt-formatted-string", {"class": "factoid-value style-scope ytd-factoid-renderer"})
        deslikes = soup.find_all("span", {"id": "text"})[0].get_text()

        if ("," in deslikes):
            deslikes = deslikes.replace(" mil", "00").replace(",", "")
        else:
            deslikes = deslikes.replace(" mil", "000").replace("," ,"")

        likess = dados[0].get_text()
        if("," in likess):
            likess = likess.replace(" mil", "00").replace(",","")
        else:
            likess = likess.replace(" mil", "000").replace(",","")
        visualizacoes = dados[1].get_text()

        #Realizamos uma busca em todas as Tags que contenham comentário, começando com TAG o identificador, Ex: "class", ou "id" e na frente o nome do respectivo campo
        comment = soup.find_all("yt-formatted-string", {"id": "content-text"})

        #Percorre os comentários e coleta todos os "spans" que é onde está localizado o texto dos comentários
        count = 0
        while count < len(comment):
            likeAndDeslike = \
            soup.find_all("ytd-comment-action-buttons-renderer", {"id": "action-buttons"})[count].find_all("span")[
                0].get_text()
            img = comment[count].find_all("img")
            if (len(img) > 0):
                temImagem = 1
            else:
                temImagem = 0
            if comment[count].find_all("span") == []:
                caracteres = int(len(comment[count].get_text().replace(' ', '')))
                x = analise_sentimentos(comment[count].get_text().replace(",", "-").strip())

                if ("<" in comment[count].get_text() or "==" in comment[count].get_text() or "div" in comment[
                    count].get_text() or "()" in comment[count].get_text() or "print" in comment[
                    count].get_text() or "!=" in comment[count].get_text() or "+=" in comment[count].get_text()
                        or "<table>" in comment[count].get_text() or "<tr>" in comment[count].get_text() or "<td>" in
                        comment[count].get_text() or "+=" in comment[count].get_text()):

                    vCodigo = vCodigo + 1

                    quantidade = quantidade + 1
                    vLikeComentario = vLikeComentario + float(likeAndDeslike.strip())
                    vEmoji = vEmoji + temImagem

                    vCaracteres = vCaracteres + caracteres
                    vTristeza = vTristeza + x[0]
                    vAlegria = vAlegria + x[1]
                    vMedo = vMedo + x[2]
                    vAversao = vAversao + x[3]
                    vRaiva = vRaiva + x[4]
                    vPontuacao = vPontuacao + x[5]
                    vResultado = vResultado + x[6]

                    quantidadeTristeza = quantidadeTristeza + validacao(x[0])
                    quantidadeAlegria = quantidadeAlegria + validacao(x[1])
                    quantidadeMedo = quantidadeMedo + validacao(x[2])
                    quantidadeAversao = quantidadeAversao + validacao(x[3])
                    quantidadeRaiva = quantidadeRaiva + validacao(x[4])
                    quantidadePontuacao = quantidadePontuacao + validacao(x[5])
                    quantidadeResultado = quantidadeResultado + validacao(x[6])

                else:
                    vOpniao = vOpniao + 1

                    quantidade = quantidade + 1
                    vLikeComentario = vLikeComentario + float(likeAndDeslike.strip())
                    vEmoji = vEmoji + temImagem

                    vCaracteres = vCaracteres + caracteres
                    vTristeza = vTristeza + x[0]
                    vAlegria = vAlegria + x[1]
                    vMedo = vMedo + x[2]
                    vAversao = vAversao + x[3]
                    vRaiva = vRaiva + x[4]
                    vPontuacao = vPontuacao + x[5]
                    vResultado = vResultado + x[6]

                    quantidadeTristeza = quantidadeTristeza + validacao(x[0])
                    quantidadeAlegria = quantidadeAlegria + validacao(x[1])
                    quantidadeMedo = quantidadeMedo + validacao(x[2])
                    quantidadeAversao = quantidadeAversao + validacao(x[3])
                    quantidadeRaiva = quantidadeRaiva + validacao(x[4])
                    quantidadePontuacao = quantidadePontuacao + validacao(x[5])
                    quantidadeResultado = quantidadeResultado + validacao(x[6])

            else:
                spans = comment[count].find_all("span")
                comentario = ""
                for s in spans:
                    comentario = comentario + s.get_text().strip()
                caracteres = int(len(comentario.replace(' ', '')))
                x = analise_sentimentos(comentario.replace(",", "-").strip())

                if ("<" in comment[count].get_text() or "==" in comment[count].get_text() or "div" in comment[
                    count].get_text() or "()" in comment[count].get_text() or "print" in comment[
                    count].get_text() or "!=" in comment[count].get_text() or "+=" in comment[count].get_text()
                        or "<table>" in comment[count].get_text() or "<tr>" in comment[count].get_text() or "<td>" in
                        comment[count].get_text() or "+=" in comment[count].get_text()):

                    vCodigo = vCodigo + 1

                    quantidade = quantidade + 1
                    vLikeComentario = vLikeComentario + float(likeAndDeslike.strip())
                    vEmoji = vEmoji + temImagem

                    vCaracteres = vCaracteres + caracteres
                    vTristeza = vTristeza + x[0]
                    vAlegria = vAlegria + x[1]
                    vMedo = vMedo + x[2]
                    vAversao = vAversao + x[3]
                    vRaiva = vRaiva + x[4]
                    vPontuacao = vPontuacao + x[5]
                    vResultado = vResultado + x[6]

                    quantidadeTristeza = quantidadeTristeza + validacao(x[0])
                    quantidadeAlegria = quantidadeAlegria + validacao(x[1])
                    quantidadeMedo = quantidadeMedo + validacao(x[2])
                    quantidadeAversao = quantidadeAversao + validacao(x[3])
                    quantidadeRaiva = quantidadeRaiva + validacao(x[4])
                    quantidadePontuacao = quantidadePontuacao + validacao(x[5])
                    quantidadeResultado = quantidadeResultado + validacao(x[6])

                else:
                    vOpniao = vOpniao + 1

                    quantidade = quantidade + 1
                    vLikeComentario = vLikeComentario + float(likeAndDeslike.strip())
                    vEmoji = vEmoji + temImagem

                    vCaracteres = vCaracteres + caracteres
                    vTristeza = vTristeza + x[0]
                    vAlegria = vAlegria + x[1]
                    vMedo = vMedo + x[2]
                    vAversao = vAversao + x[3]
                    vRaiva = vRaiva + x[4]
                    vPontuacao = vPontuacao + x[5]
                    vResultado = vResultado + x[6]

                    quantidadeTristeza = quantidadeTristeza + validacao(x[0])
                    quantidadeAlegria = quantidadeAlegria + validacao(x[1])
                    quantidadeMedo = quantidadeMedo + validacao(x[2])
                    quantidadeAversao = quantidadeAversao + validacao(x[3])
                    quantidadeRaiva = quantidadeRaiva + validacao(x[4])
                    quantidadePontuacao = quantidadePontuacao + validacao(x[5])
                    quantidadeResultado = quantidadeResultado + validacao(x[6])

            count = count + 1

            if(quantidade == 20):
                result = [visualizacoes, likess, deslikes, mediaSentimento(vLikeComentario, quantidade),
                           mediaSentimento(vCaracteres, quantidade),
                           mediaSentimento(vCodigo, quantidade),
                           mediaSentimento(vOpniao, quantidade),
                           mediaSentimento(vEmoji, quantidade), cleon1[0], cleon1[1],
                           mediaSentimento(vTristeza, quantidadeTristeza),
                           mediaSentimento(vAlegria, quantidadeAlegria),
                           mediaSentimento(vMedo, quantidadeMedo),
                           mediaSentimento(vAversao, quantidadeAversao),
                           mediaSentimento(vRaiva, quantidadeRaiva),
                           mediaSentimento(vPontuacao, quantidadePontuacao),
                           mediaSentimento(vResultado, quantidadeResultado)]
                print(result)
                writer.writerow(result)

                result2 = [visualizacoes, likess, deslikes, mediaSentimento(vLikeComentario, quantidade),
                           mediaSentimento(vCaracteres, quantidade),
                           mediaSentimento(vCodigo, quantidade),
                           mediaSentimento(vOpniao, quantidade),
                           mediaSentimento(vEmoji, quantidade), cleon2[0], cleon2[1],
                           mediaSentimento(vTristeza, quantidadeTristeza),
                           mediaSentimento(vAlegria, quantidadeAlegria),
                           mediaSentimento(vMedo, quantidadeMedo),
                           mediaSentimento(vAversao, quantidadeAversao),
                           mediaSentimento(vRaiva, quantidadeRaiva),
                           mediaSentimento(vPontuacao, quantidadePontuacao),
                           mediaSentimento(vResultado, quantidadeResultado)]

                print(result2)
                writer.writerow(result2)

                vLikeComentario = 0.0
                vCodigo = 0
                vOpniao = 0
                vEmoji = 0
                vCaracteres = 0.0
                vTristeza = 0.0
                vAlegria = 0.0
                vMedo = 0.0
                vAversao = 0.0
                vRaiva = 0.0
                vPontuacao = 0.0
                vResultado = 0.0

                quantidadeTristeza = 0.0
                quantidadeAlegria = 0.0
                quantidadeMedo = 0.0
                quantidadeAversao = 0.0
                quantidadeRaiva = 0.0
                quantidadePontuacao = 0.0
                quantidadeResultado = 0.0

                quantidade = 0

        if(len(comment) < 20 or quantidade > 0):
            result = [visualizacoes, likess, deslikes, mediaSentimento(vLikeComentario, quantidade),
                           mediaSentimento(vCaracteres, quantidade),
                           mediaSentimento(vCodigo, quantidade),
                           mediaSentimento(vOpniao, quantidade),
                           mediaSentimento(vEmoji, quantidade), cleon1[0], cleon1[1],
                           mediaSentimento(vTristeza, quantidadeTristeza),
                           mediaSentimento(vAlegria, quantidadeAlegria),
                           mediaSentimento(vMedo, quantidadeMedo),
                           mediaSentimento(vAversao, quantidadeAversao),
                           mediaSentimento(vRaiva, quantidadeRaiva),
                           mediaSentimento(vPontuacao, quantidadePontuacao),
                           mediaSentimento(vResultado, quantidadeResultado)]
            print(result)
            writer.writerow(result)

            result2 = [visualizacoes, likess, deslikes, mediaSentimento(vLikeComentario, quantidade),
                           mediaSentimento(vCaracteres, quantidade),
                           mediaSentimento(vCodigo, quantidade),
                           mediaSentimento(vOpniao, quantidade),
                           mediaSentimento(vEmoji, quantidade), cleon2[0], cleon2[1],
                           mediaSentimento(vTristeza, quantidadeTristeza),
                           mediaSentimento(vAlegria, quantidadeAlegria),
                           mediaSentimento(vMedo, quantidadeMedo),
                           mediaSentimento(vAversao, quantidadeAversao),
                           mediaSentimento(vRaiva, quantidadeRaiva),
                           mediaSentimento(vPontuacao, quantidadePontuacao),
                           mediaSentimento(vResultado, quantidadeResultado)]

            print(result2)
            writer.writerow(result2)


def analise_sentimentos(comment):
    analysis_list = []
    result = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    if(comment != ""):
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

        #  'Tristeza', 'Alegria', 'Medo', 'Aversao', 'Raiva', 'Pontuacao', 'Resultado'
        result = [x[0].analysis.emotions.sadness,
                  x[0].analysis.emotions.joy,
                  x[0].analysis.emotions.fear,
                  x[0].analysis.emotions.disgust,
                  x[0].analysis.emotions.anger,
                  x[0].analysis.sentiment.score,
                  x[0].analysis.sentiment.label]


        if result[6] == 'POSITIVE':
            result[6] = 1
        if result[6] == 'MIXED' or result[6] == 'NEUTRAL':
            result[6] = 0
        if result[6] == 'NEGATIVE':
            result[6] = -1
        print(result)
    return result


def planilhaCleon(video, index):
    if(index == 1):
        if video == "https://www.youtube.com/watch?v=iFYWrDMfVNo":
            return [1, 2]
        if video == "https://www.youtube.com/watch?v=YUeiAhpPMjQ":
            return [5, 4]
        if video == "https://www.youtube.com/watch?v=XinLASYOJE4":
            return [3, 1]
        if video == "https://www.youtube.com/watch?v=MOXLCjL4Ik4":
            return [3, 2]
        if video == "https://www.youtube.com/watch?v=pMPlngyWHLM":
            return [4, 3]
        if video == "https://www.youtube.com/watch?v=PQzUj5Hd0jk":
            return [2, 3]
        if video == "https://www.youtube.com/watch?v=shBkovJfWpk":
            return [4, 3]
        if video == "https://www.youtube.com/watch?v=gisl6mK96Jg":
            return [2, 4]
        if video == "https://www.youtube.com/watch?v=Y2EJfB9DMLU":
            return [3, 3]
        if video == "https://www.youtube.com/watch?v=jtnLR8pA4YU":
            return [1, 2]
        if video == "https://www.youtube.com/watch?v=YpHxxLAQCdk":
            return [1, 3]
        if video == "https://www.youtube.com/watch?v=-9Nafr7zdJs":
            return [2, 3]
        if video == "https://www.youtube.com/watch?v=ZdU4wMyiTSs":
            return [5, 3]
        if video == "https://www.youtube.com/watch?v=ruOzUIA4rbs":
            return [2, 3]
        if video == "https://www.youtube.com/watch?v=r7f-aR7vgg0":
            return [1, 2]
        if video == "https://www.youtube.com/watch?v=SJzd9x2S2yg":
            return [3, 3]
        if video == "https://www.youtube.com/watch?v=AdyGxhYWhoM":
            return [2, 4]
        if video == "https://www.youtube.com/watch?v=pMPlngyWHLM":
            return [3, 2]
        if video == "https://www.youtube.com/watch?v=qiGTRJlCnlA":
            return [4, 2]
        if video == "https://www.youtube.com/watch?v=_HI7ltav9q4":
            return [2, 3]
        if video == "https://www.youtube.com/watch?v=19IGAeoFKlU":
            return [4, 2]
        if video == "https://www.youtube.com/watch?v=_PZldwo0vVo":
            return [3, 2]
        if video == "https://www.youtube.com/watch?v=SJzd9x2S2yg":
            return [3, 3]
        if video == "https://www.youtube.com/watch?v=oSQfzjl110k":
            return [2, 1]
        if video == "https://www.youtube.com/watch?v=jAzL4SE5-QM":
            return [2, 4]
        if video == "https://www.youtube.com/watch?v=EGmlFdwD4C4":
            return [3, 2]
        if video == "https://www.youtube.com/watch?v=7yBXNGVyN3Q":
            return [3, 2]
        if video == "https://www.youtube.com/watch?v=WgYW2TMwA9U":
            return [4, 3]
        if video == "https://www.youtube.com/watch?v=8qbqFsPov3g":
            return [2, 1]
        if video == "https://www.youtube.com/watch?v=DnHSTYuk-V4":
            return [4, 3]
        if video == "https://www.youtube.com/watch?v=iphqkUNXxek":
            return [5, 4]
        if video == "https://www.youtube.com/watch?v=mGLtyCOJe4A":
            return [2, 2]
        if video == "https://www.youtube.com/watch?v=D5QvQmes198":
            return [2, 2]
        if video == "https://www.youtube.com/watch?v=u5P_vryX0fo":
            return [1, 2]
        if video == "https://www.youtube.com/watch?v=NctjqlfKC0U":
            return [4, 3]
        if video == "https://www.youtube.com/watch?v=_Z-yaWEmV9c":
            return [4, 4]
        if video == "https://www.youtube.com/watch?v=FcrMEfjLxwg":
            return [3, 4]
    elif (index == 2):
        if video == "https://www.youtube.com/watch?v=iFYWrDMfVNo":
            return [2, 2]
        if video == "https://www.youtube.com/watch?v=YUeiAhpPMjQ":
            return [5, 4]
        if video == "https://www.youtube.com/watch?v=XinLASYOJE4":
            return [3, 2]
        if video == "https://www.youtube.com/watch?v=MOXLCjL4Ik4":
            return [3, 3]
        if video == "https://www.youtube.com/watch?v=pMPlngyWHLM":
            return [3, 3]
        if video == "https://www.youtube.com/watch?v=PQzUj5Hd0jk":
            return [3, 2]
        if video == "https://www.youtube.com/watch?v=shBkovJfWpk":
            return [2, 2]
        if video == "https://www.youtube.com/watch?v=gisl6mK96Jg":
            return [2, 4]
        if video == "https://www.youtube.com/watch?v=Y2EJfB9DMLU":
            return [3, 3]
        if video == "https://www.youtube.com/watch?v=jtnLR8pA4YU":
            return [1, 2]
        if video == "https://www.youtube.com/watch?v=YpHxxLAQCdk":
            return [3, 3]
        if video == "https://www.youtube.com/watch?v=-9Nafr7zdJs":
            return [3, 3]
        if video == "https://www.youtube.com/watch?v=ZdU4wMyiTSs":
            return [4, 3]
        if video == "https://www.youtube.com/watch?v=ruOzUIA4rbs":
            return [4, 4]
        if video == "https://www.youtube.com/watch?v=r7f-aR7vgg0":
            return [2, 1]
        if video == "https://www.youtube.com/watch?v=SJzd9x2S2yg":
            return [3, 3]
        if video == "https://www.youtube.com/watch?v=AdyGxhYWhoM":
            return [3, 3]
        if video == "https://www.youtube.com/watch?v=pMPlngyWHLM":
            return [4, 3]
        if video == "https://www.youtube.com/watch?v=qiGTRJlCnlA":
            return [3, 4]
        if video == "https://www.youtube.com/watch?v=_HI7ltav9q4":
            return [2, 2]
        if video == "https://www.youtube.com/watch?v=19IGAeoFKlU":
            return [3, 2]
        if video == "https://www.youtube.com/watch?v=_PZldwo0vVo":
            return [4, 3]
        if video == "https://www.youtube.com/watch?v=SJzd9x2S2yg":
            return [3, 3]
        if video == "https://www.youtube.com/watch?v=oSQfzjl110k":
            return [3, 2]
        if video == "https://www.youtube.com/watch?v=jAzL4SE5-QM":
            return [3, 3]
        if video == "https://www.youtube.com/watch?v=EGmlFdwD4C4":
            return [3, 2]
        if video == "https://www.youtube.com/watch?v=7yBXNGVyN3Q":
            return [3, 2]
        if video == "https://www.youtube.com/watch?v=WgYW2TMwA9U":
            return [3, 3]
        if video == "https://www.youtube.com/watch?v=8qbqFsPov3g":
            return [2, 2]
        if video == "https://www.youtube.com/watch?v=DnHSTYuk-V4":
            return [3, 3]
        if video == "https://www.youtube.com/watch?v=iphqkUNXxek":
            return [4, 4]
        if video == "https://www.youtube.com/watch?v=mGLtyCOJe4A":
            return [3, 3]
        if video == "https://www.youtube.com/watch?v=D5QvQmes198":
            return [3, 2]
        if video == "https://www.youtube.com/watch?v=u5P_vryX0fo":
            return [3, 3]
        if video == "https://www.youtube.com/watch?v=NctjqlfKC0U":
            return [3, 2]
        if video == "https://www.youtube.com/watch?v=_Z-yaWEmV9c":
            return [3, 3]
        if video == "https://www.youtube.com/watch?v=FcrMEfjLxwg":
            return [3, 2]
    return ['', '', '', '']

def validacao(valor):
    if(valor == 0.0 or valor == 0):
        return 0
    else:
        return 1

def mediaSentimento(valor, quantidade):
    if(quantidade == 0 or quantidade == 0.0):
        return quantidade
    else:
        return round((valor/quantidade), 3)

if __name__ == '__main__':
    dadoVideo("https://www.youtube.com/watch?v=_Z-yaWEmV9c")


