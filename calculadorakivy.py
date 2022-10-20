from unittest import result
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.core.window import Window

Window.size = (500,700)
Builder.load_file('calculadora.kv')
class calculadora(Widget):
    def clear(self):
        self.ids.calc_input.text='0'

    def button_press(self, Button):
        num = self.ids.calc_input.text

        if num == '0':
            self.ids.calc_input.text = ''
            self.ids.calc_input.text = f'{Button}'
        else:
            self.ids.calc_input.text=f'{num}{Button}'

    def add(self):
        num = self.ids.calc_input.text
        self.ids.calc_input.text= f'{num}+'

    def sub(self):
        num = self.ids.calc_input.text
        self.ids.calc_input.text= f'{num}-'

    def mult(self):
        num = self.ids.calc_input.text
        self.ids.calc_input.text= f'{num}*'

    def div(self):
        num = self.ids.calc_input.text
        self.ids.calc_input.text= f'{num}/'

    def calcular(self):
        expre=str(self.ids.calc_input.text)
        result=eval(expre)
        self.ids.calc_input.text= f'{result}'


class rodarcalc(App):
    def build(self):
        return calculadora()

if __name__=='__main__':
    rodarcalc().run()