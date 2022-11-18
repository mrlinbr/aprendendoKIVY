from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivy.core.audio import SoundLoader
from tkinter import filedialog
from pytube import YouTube
import pytube

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
            self.vid = YouTube(self.video).streams.get_highest_resolution().download()
        except:
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
        try:
            self.path = self.ids.caminho.text
            self.list = os.listdir(self.path)
            
            self.listamusicas = [x for x in self.list if x.endswith(('mp3'))]
            print(self.listamusicas)
            self.num_musicas = len(self.listamusicas)
        except:
            self.ids.caminho.text = 'ocorreu algum erro, tente reformular o diretorio'

    def tocarmusica(self, obj):
        from random import randrange
        self.msctitulo = self.song[randrange(0,self.num_musicas)]
        self.msc = SoundLoader.load('{}/{}'.format(self.path,self.msctitulo))

        self.msc.play()

    def pararmusica(self,obj):
        self.msc.stop()

class Gerenciador(ScreenManager):
    pass

tl = Builder.load_file('variastelas.kv')

class rodarkv(App):
    def build(self):
        return tl

if __name__=='__main__':
    rodarkv().run()
