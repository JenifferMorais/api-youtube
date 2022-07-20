# -*- coding: utf-8 -*-

# Sample Python code for youtube.commentThreads.list
# See instructions for running these code samples locally:
# https://developers.google.com/explorer-help/code-samples#python

import os

import googleapiclient.discovery

def main():
    # Disable OAuthlib's HTTPS verification when running locally.
    # *DO NOT* leave this option enabled in production.
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    api_service_name = "youtube"
    api_version = "v3"
    DEVELOPER_KEY = "AIzaSyA0oyyBrIM1hpY-z8swVuHdQbG_JehSx_A"

    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, developerKey = DEVELOPER_KEY)

    video_response = youtube.commentThreads().list(
        part="snippet,replies",
        maxResults=100,
        videoId="eJO62WkGzcU"
    )

    while video_response:
        for item in video_response['items']:
            comment = item['snippet']['topLevelComment']['snippet']['textDisplay']

            if 'nextPageToken' in video_response:
                video_response = youtube.commentThreads().list(part='snippet, replies', videoId="eJO62WkGzcU").execute()
        else:
            break



if __name__ == "__main__":
    main()