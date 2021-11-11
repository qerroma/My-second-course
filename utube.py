from pytube import YouTube
from pytube import Channel
def getCharList(str): return [char for char in str]
chan= str(input('Введите название канала'))
c = Channel('https://www.youtube.com/c/{}/videos'.format(chan))
i = 0
url_list = []
for url in c.video_urls[:10]:
    yt = YouTube(url)
    print('[',i+1,']')
    print(yt.title)
    url_list.append(url)
    i = i+1
number = (input("Введите номер видео: "))
number = number.split(';')
new_elem = []
for elem in number:
    if len(getCharList(elem)) > 1 :
        min_el = elem [0]
        max_el = elem [2]
    else:
        new_elem = elem
        yt_number = YouTube(url_list[int(new_elem)-1])
        streams = yt_number.streams
        video_best = streams.order_by('resolution').desc().first()
        video_best.download()
k = int(min_el)
while k<int(max_el)+1:
    yt_number = YouTube(url_list[k-1])
    streams = yt_number.streams
    video_best = streams.order_by('resolution').desc().first()
    video_best.download()
    k = k+1