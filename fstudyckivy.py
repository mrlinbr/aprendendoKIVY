from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder

Builder.load_file('meucoiso.kv')
def trocarnome(self):
    self.teste.text=self.turma
class minhatela(Widget):
    pass

class rodarkv(App):
    def build(self):
        return minhatela()

if __name__=='__main__':
    rodarkv().run()