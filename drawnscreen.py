from random import random
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.graphics import Color, Ellipse,Line
class mypaintwidget(Widget):
    def on_touch_down(self, touch):
        color=(random(),random(),random())
        with self.canvas:
            Color(*color)
            d = 30
            Ellipse(pos=(touch.x-d/2, touch.y-d//2), size=(d,d))
            touch.ud['line'] = Line(points = (touch.x, touch.y))
    def on_touch_move(self, touch):
        touch.ud['line'].points += [touch.x, touch.y]
class mypaintapp(App):
    def build(self):
        mu=Widget()
        self.painter = mypaintwidget()
        clearbtn = Button(text='Clear')
        clearbtn.bind(on_release=self.clear_canvas)
        mu.add_widget(self.painter)
        mu.add_widget(clearbtn)
        return mu
    
    def clear_canvas(self,obj):
        self.painter.canvas.clear()
if __name__== '__main__':
    mypaintapp().run()