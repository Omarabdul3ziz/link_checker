from threading import Thread
import requests

valid_links = ['https://www.facebook.com/',
               'https://www.google.com/',
               'https://www.youtube.com/',
               'https://docs.python.org/',
               'https://realpython.com',
               'https://www.imdb.com/']


class Check(Thread):
    def __init__(self, link):
        Thread.__init__(self)
        self.link = link

    def run(self):
        response = requests.get(self.link)
        status = response.status_code
        if status == 200:
            print(self.link +': Success')
        else:
            print(self.link +': Not found')


ths = [Check(link) for link in valid_links]
[th.start() for th in ths]
[th.join() for th in ths]


