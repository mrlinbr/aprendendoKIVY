from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from pytube import YouTube
import pytube
from kivy.core.window import Window


class Telap(Screen):
    pass

class Telatrad(Screen):
    pass

class Telaytdown(Screen):
    pass

class Musicplayer(Screen):
    pass

class Gerenciador(ScreenManager):
    pass

tl = Builder.load_file('variastelas.kv')

class rodarkv(App):
    def build(self):
        return tl

if __name__=='__main__':
    rodarkv().run()