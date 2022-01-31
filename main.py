import kivy
import webbrowser
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.app import App
import requests
from bs4 import BeautifulSoup as BS
from webbrowser import open

r = requests.get('https://tgstat.ru/channel/@diskc_t')

html = BS(r.content, 'html.parser')

list_all = html.find_all('a', class_='ellipsis-link')

post = []
links = []
Finaly = []
start_link = 'https://ttttt.me/'


for i in list_all:
    post.append({
        'title': i.text,
        'url': i.get('href')})

for i in range(20):
    links.append(
        str(post[i]['url']).split('@'))

for i in range(20):
    word = str(links[i][1])
    Finaly.append([post[i]['title'], str(start_link + word)])


class Main(GridLayout):
    def __init__(self, **kwargs):
        super(Main, self).__init__(**kwargs)
        self.rows = 20
        self.cols = 2
        for i in range(20):
            self.add_widget(Label(text=str(i+1) + ': ' + str(Finaly[i][0])))
            self.add_widget(Button(text='перейти', size_hint_x=None, width=100))

# TODO: сделать рабочие кнопки


class MyApp(App):
    def build(self):
        return Main()


if __name__ == '__main__':
    MyApp().run()