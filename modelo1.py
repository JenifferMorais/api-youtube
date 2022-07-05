import csv
import json
import os
from collections import namedtuple

import requests
import base64
from googleapiclient.discovery import build

DEVELOPER_KEY = os.environ["DEVELOPER_KEY"] = 'AIzaSyA0oyyBrIM1hpY-z8swVuHdQbG_JehSx_A'

analysis_list = []

# Resgata Comentários
def video_comments(url_video):

    video_id = handler_video(url_video)

    youtube = build('youtube', 'v3', developerKey=DEVELOPER_KEY)
    video_response = youtube.commentThreads().list(
        part='snippet,replies', videoId=video_id).execute()

    while video_response:
        for item in video_response['items']:
            comment = item['snippet']['topLevelComment']['snippet']['textDisplay']
            if(len(comment) > 0):
                analysis(comment)
        else:
            break

# Analisa comentario
def analysis(comment):
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

# Trata URL resgatando apenas ID
def handler_video(url_video):
    video_id = str(url_video).split("=")[1]
    return video_id


# Método para gerar aquivo JSON
def writeJSON(url_video):
    analysis_json = json.dumps(analysis_list, indent=4, ensure_ascii=False)
    with open("JSON/commentFINAL.json", "a", encoding="utf-8") as outfile:
      outfile.write("Vídeo:")
      outfile.write(url_video)
      outfile.write(analysis_json)

#Metodo de limpeza para o proximo vídeo
def clear():
    analysis_list.clear()

# Método para gerar aquivo CSV sem o comentario
def writeCSV(url_video):
    analysis_json = json.dumps(analysis_list, indent=4, ensure_ascii=False)
    x = json.loads(analysis_json, object_hook=lambda d:namedtuple('X', d.keys())(*d.values()))
    aux = 0

    with open('CSV/emotionsFINAL.csv', 'a', encoding = 'utf-8') as f:
       writer = csv.writer(f, lineterminator="\n")
       header = ['Video']
       data = [url_video]
       while aux < len(x):
           header.extend(['Sadness', 'Joy', 'Fear', 'Disgust', 'Anger', 'Score', 'Label'])
           data.extend([x[aux].analysis.emotions.sadness, x[aux].analysis.emotions.joy,
                   x[aux].analysis.emotions.fear, x[aux].analysis.emotions.disgust, x[aux].analysis.emotions.anger,
                   x[aux].analysis.sentiment.score, x[aux].analysis.sentiment.label])
           aux = aux + 1
       writer.writerow(header)
       writer.writerow(data)
       writer.writerow("\n")

       f.close()

def inicio(url_video):
    video_comments(url_video)
    # Escreve arquivo csv somente com as emoções
    writeCSV(url_video)
    # Escreve arquivo JSON completo
    writeJSON(url_video)
    clear()

if __name__ == '__main__':
    # url_video = input("Link do Vídeo? ")
    url_video = "https://www.youtube.com/watch?v=EGmlFdwD4C4"
    inicio(url_video)





