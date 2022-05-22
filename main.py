import json
import os
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
    print(comment, '\n', dict(response.json())['sentiment']['label'], end=('\n' * 2))

    dictionary = {"comment": comment, "analysis": response.json()}
    analysis_list.append(dictionary)


# Trata URL resgatando apenas ID
def handler_video(url_video):
    video_id = str(url_video).split("=")[1]
    return video_id


# Método para gerar aquivo JSON
def write():
    analysis_json = json.dumps(analysis_list, indent=4, ensure_ascii=False)
    print(analysis_json)
    with open("comment.json", "a", encoding="utf-8") as outfile:
        outfile.write("Vídeo:")
        outfile.write(url_video)
        outfile.write(analysis_json)


if __name__ == '__main__':
    url_video = input("Link do Vídeo? ")
    video_comments(url_video)
    write()
