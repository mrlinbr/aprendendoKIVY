from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from pytube import YouTube
import pytube


Builder.load_file('gridtest.kv')

class minhatela(Widget):
    def pressionar(self):
        #inputa é o TextInput onde eu digito o link
        #Aqui eu digo'hei! "self.video" é o mesmo que o texto(link) que está lá no arquivo.kv, no "inputa"'
        self.video=self.ids.inputa.text
        #Função para baixar o video, onde eu '''Youtubonizo''' o link (oriundo do inputa) e peço o titulo dele
        self.ids.label.text= YouTube(self.video).title
        #aqui eu digo que o source do AsyncImage (olhar os comentário do arquivo.kv para mais detalhes) é a...
        #URL do self.video, faço isso usando uma função do pytube (pytube nunca errou)
        self.ids.imagemcoisada.source = YouTube(self.video).thumbnail_url
        #Bom, aqui eu uso o try e except para lidar com erro da parte humana (se o usuario colocar o link de froma errada por exemplo)
        #O programa tenta fazer a função normalmente
        try:
            #aqui é para baixar o video, onde eu peço a melhor resolução que tiver ( pretendo melhorar isso, pois abre espaço para erros)
            self.vid = YouTube(self.video).streams.get_highest_resolution().download()
        except:
            #caso algo ocorra errado, ele muda o texto da label para isso
            self.ids.label.text='algo deu errado \n :( tente novamente'

    def get_infos(self):
        #self.ids.likes.text=YouTube(self.video).views
        print(YouTube(self.video).views)


class rodarkv(App):
    def build(self):
        return minhatela()

if __name__=='__main__':
    rodarkv().run()