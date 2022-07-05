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
            analysis(comment)
            if 'nextPageToken' in video_response:
              video_response = youtube.commentThreads().list(part='snippet, replies', videoId= video_id).execute()
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

    dictionary = {"comment": comment, "analysis": response.json()}
    analysis_list.append(dictionary)


# Trata URL resgatando apenas ID
def handler_video(url_video):
    video_id = str(url_video).split("=")[1]
    return video_id

#Metodo de limpeza para o proximo vídeo
def clear():
    analysis_list.clear()


# Método para gerar aquivo JSON
def write(url_video):
    analysis_json = json.dumps(analysis_list, indent=4, ensure_ascii=False)

    # with open("comment.json", "a", encoding="utf-8") as outfile:
    #   outfile.write("Vídeo:")
    #   outfile.write(url_video)
    #   outfile.write(analysis_json)

    x = json.loads(analysis_json, object_hook=lambda d:namedtuple('X', d.keys())(*d.values()))
    aux = 0
    # print(x[3].analysis.emotions.disgust)
    header = ['Video', 'Comment', 'Sadness', 'Joy', 'Fear', 'Disgust', 'Anger', 'Score', 'Label']


    with open('csv_file.csv', 'a',errors='replace') as f:
       writer = csv.writer(f, lineterminator="\n")
       # writer.writerow(header)
       while aux < len(x):
           data = [url_video, x[aux].comment.replace(","," ").replace("  &lt","").replace("<br>","").replace("\n", "").replace(" &lt;3","").replace("&lt","").replace(";","")," "," "," "," ",x[aux].analysis.emotions.sadness, x[aux].analysis.emotions.joy,
                   x[aux].analysis.emotions.fear, x[aux].analysis.emotions.disgust, x[aux].analysis.emotions.anger,
                   x[aux].analysis.sentiment.score, x[aux].analysis.sentiment.label]
           writer.writerow(data)
           aux = aux + 1
       f.close()


def inicio(url_video):
    video_comments(url_video)
    # Escreve arquivo csv somente com as emoções
    write(url_video)
    clear()

if __name__ == '__main__':
    # while(x):
       # url_video = input("Link do Vídeo? ")
       # if(url_video == 0):
       #     x = False
    url_video= ("https://www.youtube.com/watch?v=_PZldwo0vVo")
    inicio(url_video)

