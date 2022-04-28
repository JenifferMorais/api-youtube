import json
import requests
import pprint
import base64
from googleapiclient.discovery import build

api_key = 'AIzaSyA0oyyBrIM1hpY-z8swVuHdQbG_JehSx_A'


def video_comments(video_id):
    replies = []

    youtube = build('youtube', 'v3', developerKey=api_key)

    video_response = youtube.commentThreads().list(
        part='snippet,replies', videoId=video_id).execute()

    while video_response:

        for item in video_response['items']:
            comment = item['snippet']['topLevelComment']['snippet']['textDisplay']
            replycount = item['snippet']['totalReplyCount']
            if replycount > 0:
                for reply in item['replies']['comments']:
                    reply = reply['snippet']['textDisplay']
                    replies.append(reply)

            print(comment, replies, end='\n\n')
            analysis(comment)
            replies = []
        if 'nextPageToken' in video_response:
            video_response = youtube.commentThreads().list(
                part='snippet,replies', videoId=video_id).execute()
        else:
            break


def analysis(comment):
    url = 'https://api.gotit.ai/NLU/v1.5/Analyze'
    data = {"T": comment, "S": True, "EM": True}
    data_json = json.dumps(data)
    userAndPass = base64.b64encode(
        b"2274-jVwH/V0Q:gq3STLhSz2IY3Bey+btyOmN7xpo+HuK5kSRtLK+/").decode("ascii")
    headers = {'Content-type': 'application/json', "Authorization": "Basic %s" % userAndPass}
    response = requests.post(url, data=data_json, headers=headers)
    # pprint.pprint(response.json())
    write(comment, response.json())


def write(comment, analys):
    dictionary = {
        "comment": comment,
        "analysis": analys
    }
    json_object = json.dumps(dictionary, indent= 4, ensure_ascii=False)
    with open("comment.json", "a") as outfile:
        outfile.write(json_object)

if __name__ == '__main__':
    video_id = "suTdgiezIcs"
    video_comments(video_id)