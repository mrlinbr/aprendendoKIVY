from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from pytube import YouTube
import pytube
from kivy.core.window import Window
from time import sleep
import os


class Telap(Screen):
    pass

class Telatrad(Screen):
    pass

class Escolherdiretorio(Screen):
    def escolhido(self,filename):
        try:
            print(filename[0])
        except:
            print('erro')

class Telaytdown(Screen):
    def baixar(self):
        sleep(8)
        print('saporra funfou krl')
        
        try:
            #aqui é para baixar o video, onde eu peço a melhor resolução que tiver ( pretendo melhorar isso, pois abre espaço para erros)
            self.vid = YouTube(self.video).streams.get_highest_resolution().download()
        except:
            #caso algo ocorra errado, ele muda o texto da label para isso
            self.ids.label.text='algo deu errado \n :( tente novamente'
        
    def escolhido(self,filename):
        print(filename[0])

    def get_video(self,stream):
        stream.download()

    def informacoes(self):
        self.video=self.ids.link.text
        self.ids.titulo.text= YouTube(self.video).title
        self.ids.thumb.source = YouTube(self.video).thumbnail_url
    def baixarmsc(self):
        self.videopmsc=self.ids.link.text
        yt= YouTube(self.videopmsc)
        try:
             stream =  YouTube(self.ids.link.text)
             self.get_video(stream.streams.get_audio_only(),3)
        except:
           print('erro :9')
        
class Musicplayer(Screen):
    def sla(self):
        self.path = "C:/kivygui"
        self.list = os.listdir(self.path)
        
        self.listamusicas = [x for x in self.list if x.endswith(('mp4'))]
        print(self.listamusicas)


class Gerenciador(ScreenManager):
    pass

tl = Builder.load_file('variastelas.kv')

class rodarkv(App):
    def build(self):
        return tl

if __name__=='__main__':
    rodarkv().run()
