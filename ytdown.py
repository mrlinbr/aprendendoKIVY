from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder

Builder.load_file('frontendpydow.kv')

class widgets(Widget):
    pass

class ytdown(App):
    def build(self):
        return widgets()

if __name__=='__main__':
    ytdown().run()