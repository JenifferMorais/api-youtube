import main


def videos():
    v = 0
    url = ["https://www.youtube.com/watch?v=iFYWrDMfVNo",
           "https://www.youtube.com/watch?v=YUeiAhpPMjQ",
           "https://www.youtube.com/watch?v=XinLASYOJE4",
           "https://www.youtube.com/watch?v=MOXLCjL4Ik4",
           "https://www.youtube.com/watch?v=pMPlngyWHLM",
           "https://www.youtube.com/watch?v=PQzUj5Hd0jk",
           "https://www.youtube.com/watch?v=shBkovJfWpk",
           "https://www.youtube.com/watch?v=gisl6mK96Jg",
           "https://www.youtube.com/watch?v=Y2EJfB9DMLU",
           "https://www.youtube.com/watch?v=jtnLR8pA4YU",
           "https://www.youtube.com/watch?v=YpHxxLAQCdk",
           "https://www.youtube.com/watch?v=-9Nafr7zdJs",
           "https://www.youtube.com/watch?v=ZdU4wMyiTSs",
           "https://www.youtube.com/watch?v=ruOzUIA4rbs",
           "https://www.youtube.com/watch?v=r7f-aR7vgg0",
           "https://www.youtube.com/watch?v=SJzd9x2S2yg",
           "https://www.youtube.com/watch?v=AdyGxhYWhoM",
           "https://www.youtube.com/watch?v=pMPlngyWHLM",
           "https://www.youtube.com/watch?v=qiGTRJlCnlA",
           "https://www.youtube.com/watch?v=_HI7ltav9q4",
           "https://www.youtube.com/watch?v=OJwzsL3of8k",
           "https://www.youtube.com/watch?v=19IGAeoFKlU",
           "https://www.youtube.com/watch?v=_PZldwo0vVo",
           "https://www.youtube.com/watch?v=SJzd9x2S2yg",
           "https://www.youtube.com/watch?v=oSQfzjl110k",
           "https://www.youtube.com/watch?v=jAzL4SE5-QM",
           "https://www.youtube.com/watch?v=EGmlFdwD4C4",
           "https://www.youtube.com/watch?v=7yBXNGVyN3Q",
           "https://www.youtube.com/watch?v=WgYW2TMwA9U",
           "https://www.youtube.com/watch?v=8qbqFsPov3g",
           "https://www.youtube.com/watch?v=DnHSTYuk-V4",
           "https://www.youtube.com/watch?v=iphqkUNXxek",
           "https://www.youtube.com/watch?v=mGLtyCOJe4A",
           "https://www.youtube.com/watch?v=D5QvQmes198",
           "https://www.youtube.com/watch?v=u5P_vryX0fo",
           "https://www.youtube.com/watch?v=NctjqlfKC0U",
           "https://www.youtube.com/watch?v=_Z-yaWEmV9c",
           "https://www.youtube.com/watch?v=FcrMEfjLxwg"]

    while v < len(url):
           try:
               main.inicio(url[v])
               print(v+1,"Sucesso no vídeo:", url[v])
           except:
               print(v+1,"Erro no vídeo:", url[v])
           v = v + 1


if __name__ == '__main__':
    videos()
